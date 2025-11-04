import React, { useState } from 'react';
import './XRayResearchPlatform.css';

const XRayResearchPlatform = () => {
  const [currentFile, setCurrentFile] = useState(null);
  const [analysisState, setAnalysisState] = useState('idle');
  const [analysisProgress, setAnalysisProgress] = useState(0);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      setCurrentFile(file);
      setAnalysisState('idle');
      setAnalysisProgress(0);
    }
  };

  const handleRemoveFile = () => {
    setCurrentFile(null);
    setAnalysisState('idle');
    setAnalysisProgress(0);
  };

  const simulateAnalysis = () => {
    if (!currentFile) return;

    setAnalysisState('processing');
    setAnalysisProgress(0);

    // Simulate progress
    const interval = setInterval(() => {
      setAnalysisProgress(prev => {
        const newProgress = prev + 10;
        if (newProgress >= 100) {
          clearInterval(interval);
          setAnalysisState('success');
          return 100;
        }
        return newProgress;
      });
    }, 200);
  };

  return (
    <div className="research-platform">
      <header className="platform-header">
        <h1>RESEARCH AND DEVELOPMENT PROTOTYPE</h1>
      </header>
      
      <div className="disclaimer-banner">
        <span>⚠️ NOT FOR CLINICAL USE - NOT FOR DIAGNOSIS - EXPERIMENTAL ONLY</span>
      </div>

      <div className="platform-title">
        <h2>X-ray ML Analysis Research Platform</h2>
        <p>This system is for academic research and technology development only.</p>
      </div>

      <div className="upload-section">
        <h3>Upload Research Image</h3>
        <div className="upload-area">
          <input 
            type="file" 
            id="fileInput"
            onChange={handleFileSelect}
            accept=".jpg,.jpeg,.png,.dcm"
            style={{ display: 'none' }}
          />
          <label htmlFor="fileInput" className="upload-label">
            <div className="upload-icon">📁</div>
            <p>Click to select an image</p>
            <p className="file-requirements">Supported formats: JPG, PNG, DICOM</p>
          </label>
        </div>
        
        {currentFile && (
          <div className="accepted-file">
            <div className="file-info">
              <span>📄</span>
              <span className="file-name">{currentFile.name}</span>
            </div>
            <button className="remove-file-btn" onClick={handleRemoveFile}>
              ✕
            </button>
          </div>
        )}
      </div>

      <div className="analysis-section">
        <button 
          className="analyze-btn" 
          onClick={simulateAnalysis} 
          disabled={!currentFile || analysisState === 'processing'}
        >
          {analysisState === 'processing' ? 'Analyzing...' : 'Analyze (Research Only)'}
        </button>
        
        {analysisState === 'processing' && (
          <div className="progress-container">
            <div className="progress-bar">
              <div 
                className="progress-fill" 
                style={{ width: `${analysisProgress}%` }}
              ></div>
            </div>
            <span>Progress: {analysisProgress}%</span>
          </div>
        )}
        
        {analysisState === 'success' && (
          <div className="success-message">
            <h4>Analysis Complete</h4>
            <p>Results are experimental and for research purposes only.</p>
            <div className="results">
              <p><strong>Findings:</strong> No significant abnormalities detected</p>
              <p><strong>Confidence:</strong> 92%</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default XRayResearchPlatform;
