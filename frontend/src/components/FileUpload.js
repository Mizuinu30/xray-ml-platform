import React, { useState } from 'react';
import { uploadImage } from '../services/api';
import './XRayResearchPlatform.css';

const FileUpload = ({ onAnalysisComplete }) => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
    setError(null);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    if (!selectedFile) {
      setError('Please select a file first');
      return;
    }

    setIsLoading(true);
    try {
      const results = await uploadImage(selectedFile);
      onAnalysisComplete(results);
    } catch (err) {
      setError('Error processing image. Please try again.');
      console.error('Upload error:', err);
    }
    setIsLoading(false);
  };

  return (
    <div className="file-upload">
      <h2>Upload X-Ray Image</h2>
      <form onSubmit={handleSubmit}>
        <div className="upload-container">
          <input
            type="file"
            accept="image/*"
            onChange={handleFileSelect}
            disabled={isLoading}
          />
          <button type="submit" disabled={!selectedFile || isLoading}>
            {isLoading ? 'Processing...' : 'Analyze Image'}
          </button>
        </div>
        {error && <div className="error-message">{error}</div>}
      </form>
    </div>
  );
};

export default FileUpload;