import React from 'react';
import './XRayResearchPlatform.css';

const AnalysisResults = ({ results }) => {
  if (!results) return null;

  return (
    <div className="analysis-results">
      <h2>Analysis Results</h2>
      <div className="results-container">
        <div className="confidence-score">
          <h3>Confidence Score</h3>
          <div className="score">{(results.confidence_score * 100).toFixed(1)}%</div>
        </div>
        
        <div className="findings">
          <h3>Findings</h3>
          <ul>
            {results.findings.map((finding, index) => (
              <li key={index}>{finding}</li>
            ))}
          </ul>
        </div>
        
        <div className="recommendations">
          <h3>Recommendations</h3>
          <ul>
            {results.recommendations.map((rec, index) => (
              <li key={index}>{rec}</li>
            ))}
          </ul>
        </div>
        
        <div className="metadata">
          <h3>Metadata</h3>
          <table>
            <tbody>
              {Object.entries(results.metadata).map(([key, value]) => (
                <tr key={key}>
                  <td>{key}:</td>
                  <td>{value}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default AnalysisResults;