import google.generativeai as genai
import PIL.Image
import io
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
# It's recommended to use environment variables for security
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables or .env file.")

genai.configure(api_key=api_key)

# --- Configuration ---
# Use the gemini-2.0-flash-lite model which supports multimodal input
MODEL_NAME = "gemini-2.0-flash-lite"
# Path to your image file
IMAGE_PATH = "img/breaded-chicken-mashed-potatos-broccoli.jpeg" # <-- CHANGE THIS TO YOUR IMAGE FILE

# Prompt asking for macronutrients as JSON
# Being very explicit about the JSON format is important
PROMPT = """
Analyze the food item(s) in this image.
Provide the approximate macronutrient breakdown (Calories, Protein, Carbohydrates, Fat) per typical serving size or per 100g if serving size is ambiguous.
Return the information strictly as a JSON object with keys: "calories", "protein", "carbohydrates", and "fat".
For example: {"calories": "740", "protein": "20g", "carbohydrates": "30g", "fat": "15g"}.
Only output the JSON object, do not include any additional text or markdown formatting outside the JSON block.
If the food is not recognizable or nutritional info cannot be determined, return an empty JSON object {}.
"""

# --- Function to load and analyze image ---
def analyze_food_image(image_path: str, prompt: str, model_name: str = MODEL_NAME):
    """
    Loads an image, sends it to the Gemini API with a prompt,
    and attempts to parse the JSON response.

    Args:
        image_path: Path to the image file.
        prompt: The text prompt to send with the image.
        model_name: The name of the Gemini model to use.

    Returns:
        A dictionary containing the parsed JSON response, or None if parsing fails,
        or an error message string.
    """
    try:
        # Load the image using Pillow
        img = PIL.Image.open(image_path)

        # Create the content list for the API call (image and text)
        # The order matters - placing the image first is often good practice
        content = [img, prompt]

        # Initialize the generative model
        model = genai.GenerativeModel(model_name)

        print(f"Sending image '{image_path}' to model '{model_name}' for analysis...")
        print("Prompt:", prompt)

        # Generate content from the model
        # Use stream=True for potentially faster initial response, but False is simpler here
        response = model.generate_content(content)

        # Check if the response contains text content
        if not response or not response.candidates or not response.candidates[0].content or not response.candidates[0].content.parts:
             return "API response did not contain any content."

        # Extract the text part of the response
        response_text = response.text.strip()
        print("\nRaw API Response Text:")
        print(response_text)

        # Attempt to parse the response text as JSON
        # The model might wrap JSON in markdown code blocks (```json ... ```)
        # We'll try to find and extract just the JSON part
        try:
            # Simple check: does it start with { or [ and end with } or ]?
            if response_text.startswith('{') and response_text.endswith('}'):
                 # Directly parse if it looks like pure JSON
                 parsed_json = json.loads(response_text)
            elif '```json' in response_text and '```' in response_text:
                 # Extract content within ```json ... ```
                 json_start = response_text.find('```json') + len('```json')
                 json_end = response_text.find('```', json_start)
                 json_string = response_text[json_start:json_end].strip()
                 parsed_json = json.loads(json_string)
            else:
                 # If it doesn't look like JSON, maybe it's conversational or an empty object
                 # Try parsing directly just in case, otherwise return text
                 try:
                     parsed_json = json.loads(response_text)
                 except json.JSONDecodeError:
                     return f"API response did not appear to be valid JSON. Response: {response_text}"


            print("\nParsed JSON Output:")
            return parsed_json

        except json.JSONDecodeError as e:
            return f"Failed to decode JSON from response: {e}\nResponse text was:\n{response_text}"
        except Exception as e:
            return f"An unexpected error occurred during JSON parsing: {e}\nResponse text was:\n{response_text}"


    except FileNotFoundError:
        return f"Error: Image file not found at {image_path}"
    except Exception as e:
        return f"An error occurred during the API call or image processing: {e}"

# --- Main execution ---
if __name__ == "__main__":
    # Replace with the actual path to your image file
    # You can test with different food images.
    # Example: Download a picture of pizza, a salad, or a piece of fruit.
    image_file = "img/breaded-chicken-mashed-potatos-broccoli.jpeg" # Ensure this path is correct!

    result = analyze_food_image(image_file, PROMPT, MODEL_NAME)

    if isinstance(result, dict):
        print("\nAnalysis Result (JSON):")
        print(json.dumps(result, indent=4))
    else:
        print("\nAnalysis failed or returned non-JSON:")
        print(result)