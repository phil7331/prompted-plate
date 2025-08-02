import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import './ImageUpload.css';

const ImageUpload = () => {
  const [uploadedImage, setUploadedImage] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [prompt, setPrompt] = useState('');

  const onDrop = useCallback((acceptedFiles) => {
    const file = acceptedFiles[0];
    if (file) {
      setUploadedImage(file);
      setAnalysis(null);
      setError(null);
      
      // Create a preview URL for the image
      const previewUrl = URL.createObjectURL(file);
      setUploadedImage({ file, previewUrl });
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.gif', '.bmp']
    },
    multiple: false
  });

  const handleAnalyze = async () => {
    if (!uploadedImage) return;

    setLoading(true);
    setError(null);

    try {
      const formData = new FormData();
      formData.append('file', uploadedImage.file);
      if (prompt) {
        formData.append('prompt', prompt);
      }

      const response = await axios.post('http://localhost:8000/food/analyze-upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setAnalysis(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to analyze image');
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setUploadedImage(null);
    setAnalysis(null);
    setError(null);
    setPrompt('');
  };

  return (
    <div className="image-upload-container">
      <h2>Food Image Analysis</h2>
      <p>Drag and drop a food image to analyze its nutritional content</p>
      
      <div className="upload-section">
        <div {...getRootProps()} className={`dropzone ${isDragActive ? 'active' : ''}`}>
          <input {...getInputProps()} />
          {uploadedImage ? (
            <div className="image-preview">
              <img src={uploadedImage.previewUrl} alt="Uploaded food" />
              <p>{uploadedImage.file.name}</p>
            </div>
          ) : (
            <div className="dropzone-content">
              {isDragActive ? (
                <p>Drop the image here...</p>
              ) : (
                <div>
                  <p>Drag & drop an image here, or click to select</p>
                  <p className="file-types">Supports: JPEG, PNG, GIF, BMP</p>
                </div>
              )}
            </div>
          )}
        </div>

        {uploadedImage && (
          <div className="controls">
            <div className="prompt-section">
              <label htmlFor="prompt">Custom Prompt (optional):</label>
              <input
                type="text"
                id="prompt"
                value={prompt}
                onChange={(e) => setPrompt(e.target.value)}
                placeholder="e.g., 'Analyze this meal for calories and macros'"
                className="prompt-input"
              />
            </div>
            
            <div className="button-group">
              <button 
                onClick={handleAnalyze} 
                disabled={loading}
                className="analyze-btn"
              >
                {loading ? 'Analyzing...' : 'Analyze Image'}
              </button>
              <button 
                onClick={handleReset}
                className="reset-btn"
              >
                Reset
              </button>
            </div>
          </div>
        )}
      </div>

      {error && (
        <div className="error-message">
          <p>Error: {error}</p>
        </div>
      )}

      {analysis && (
        <div className="analysis-results">
          <h3>Analysis Results</h3>
          <div className="nutrition-grid">
            <div className="nutrition-item">
              <span className="label">Calories:</span>
              <span className="value">{analysis.calories} kcal</span>
            </div>
            <div className="nutrition-item">
              <span className="label">Protein:</span>
              <span className="value">{analysis.protein}g</span>
            </div>
            <div className="nutrition-item">
              <span className="label">Fat:</span>
              <span className="value">{analysis.fat}g</span>
            </div>
            <div className="nutrition-item">
              <span className="label">Carbohydrates:</span>
              <span className="value">{analysis.carbs}g</span>
            </div>
          </div>
          {analysis.description && (
            <div className="description">
              <h4>Description:</h4>
              <p>{analysis.description}</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default ImageUpload; 