import google.generativeai as genai
import PIL.Image
import json
import os
from typing import Dict, Optional, Union
from dotenv import load_dotenv
from ..models.food import FoodAnalysis

# Load environment variables
load_dotenv()

class FoodAnalysisService:
    """Service for analyzing food images using Gemini AI"""
    
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model_name = "gemini-2.0-flash-lite"
        self.default_prompt = """
        Analyze the food item(s) in this image.
        Provide the approximate macronutrient breakdown (Calories, Protein, Carbohydrates, Fat) per typical serving size or per 100g if serving size is ambiguous.
        Return the information strictly as a JSON object with keys: "calories", "protein", "carbohydrates", and "fat".
        For example: {"calories": "740", "protein": "20g", "carbohydrates": "30g", "fat": "15g"}.
        Only output the JSON object, do not include any additional text or markdown formatting outside the JSON block.
        If the food is not recognizable or nutritional info cannot be determined, return an empty JSON object {}.
        """
    
    def analyze_food_image(self, image_path: str, prompt: Optional[str] = None) -> Union[FoodAnalysis, str]:
        """
        Analyze a food image and return nutritional information
        
        Args:
            image_path: Path to the image file
            prompt: Custom prompt (optional)
            
        Returns:
            FoodAnalysis object or error message string
        """
        try:
            # Load image
            img = PIL.Image.open(image_path)
            
            # Use custom prompt or default
            analysis_prompt = prompt or self.default_prompt
            
            # Create content for API call
            content = [img, analysis_prompt]
            
            # Initialize model
            model = genai.GenerativeModel(self.model_name)
            
            # Generate response
            response = model.generate_content(content)
            
            if not response or not response.candidates or not response.candidates[0].content:
                return "API response did not contain any content."
            
            # Extract response text
            response_text = response.text.strip()
            
            # Parse JSON response
            parsed_json = self._parse_json_response(response_text)
            
            if isinstance(parsed_json, dict):
                return FoodAnalysis(**parsed_json)
            else:
                return parsed_json
                
        except FileNotFoundError:
            return f"Error: Image file not found at {image_path}"
        except Exception as e:
            return f"An error occurred during analysis: {e}"
    
    def _parse_json_response(self, response_text: str) -> Union[Dict, str]:
        """Parse JSON from API response"""
        try:
            # Check if it's pure JSON
            if response_text.startswith('{') and response_text.endswith('}'):
                return json.loads(response_text)
            
            # Check for markdown code blocks
            elif '```json' in response_text and '```' in response_text:
                json_start = response_text.find('```json') + len('```json')
                json_end = response_text.find('```', json_start)
                json_string = response_text[json_start:json_end].strip()
                return json.loads(json_string)
            
            # Try parsing directly
            else:
                try:
                    return json.loads(response_text)
                except json.JSONDecodeError:
                    return f"API response did not appear to be valid JSON. Response: {response_text}"
                    
        except json.JSONDecodeError as e:
            return f"Failed to decode JSON from response: {e}\nResponse text was:\n{response_text}"
        except Exception as e:
            return f"An unexpected error occurred during JSON parsing: {e}\nResponse text was:\n{response_text}" 