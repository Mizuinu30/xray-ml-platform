import React, { useState } from 'react';
import { Upload, FileText, AlertTriangle, Activity, CheckCircle, XCircle, ImageIcon } from 'lucide-react';

const XRayResearchPlatform = () => {
  const [currentFile, setCurrentFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [analysisState, setAnalysisState] = useState('idle');
  const [analysisProgress, setAnalysisProgress] = useState(0);

  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    if (file) {
      setCurrentFile(file);
      setAnalysisState('idle');
      setAnalysisProgress(0);
      
      // Create preview
      const reader = new FileReader();
      reader.onload = (e) => setPreviewUrl(e.target.result);
      reader.readAsDataURL(file);
    }
  };

  const handleRemoveFile = () => {
    setCurrentFile(null);
    setPreviewUrl(null);
    setAnalysisState('idle');
    setAnalysisProgress(0);
  };

  const simulateAnalysis = () => {
    if (!currentFile) return;

    setAnalysisState('processing');
    setAnalysisProgress(0);

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
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900">
      {/* Medical Header */}
      <header className="bg-slate-900/80 backdrop-blur-sm border-b border-cyan-500/20 shadow-lg">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-cyan-500 to-blue-600 rounded-lg flex items-center justify-center">
                <Activity className="w-6 h-6 text-white" />
              </div>
              <div>
                <h1 className="text-xl font-semibold text-white tracking-tight">RadiologyAI Platform</h1>
                <p className="text-xs text-cyan-400">Research & Development System</p>
              </div>
            </div>
            <div className="flex items-center gap-2 px-3 py-1.5 bg-red-500/10 border border-red-500/30 rounded-md">
              <div className="w-2 h-2 bg-red-500 rounded-full animate-pulse"></div>
              <span className="text-xs font-medium text-red-400">EXPERIMENTAL</span>
            </div>
          </div>
        </div>
      </header>

      {/* Critical Disclaimer Banner */}
      <div className="bg-gradient-to-r from-amber-500/20 to-red-500/20 border-y border-amber-500/30">
        <div className="max-w-7xl mx-auto px-6 py-3">
          <div className="flex items-center gap-3">
            <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0" />
            <p className="text-sm font-medium text-amber-100">
              <strong>IMPORTANT:</strong> This system is NOT approved for clinical use or medical diagnosis. 
              For research and technology development purposes only.
            </p>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-6 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          
          {/* Left Panel - Upload & Controls */}
          <div className="space-y-6">
            
            {/* Upload Card */}
            <div className="bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700/50 shadow-xl overflow-hidden">
              <div className="bg-gradient-to-r from-cyan-600/10 to-blue-600/10 border-b border-slate-700/50 px-6 py-4">
                <h2 className="text-lg font-semibold text-white flex items-center gap-2">
                  <Upload className="w-5 h-5 text-cyan-400" />
                  Image Upload
                </h2>
                <p className="text-sm text-slate-400 mt-1">Select medical imaging file for analysis</p>
              </div>

              <div className="p-6">
                {!currentFile ? (
                  <div>
                    <input 
                      type="file" 
                      id="fileInput"
                      onChange={handleFileSelect}
                      accept=".jpg,.jpeg,.png,.dcm"
                      className="hidden"
                    />
                    <label 
                      htmlFor="fileInput" 
                      className="block cursor-pointer"
                    >
                      <div className="border-2 border-dashed border-slate-600 hover:border-cyan-500/50 rounded-lg p-12 text-center transition-all duration-300 hover:bg-slate-700/30">
                        <div className="w-16 h-16 mx-auto mb-4 bg-gradient-to-br from-cyan-500/20 to-blue-500/20 rounded-full flex items-center justify-center">
                          <ImageIcon className="w-8 h-8 text-cyan-400" />
                        </div>
                        <p className="text-white font-medium mb-2">Drop file or click to browse</p>
                        <p className="text-sm text-slate-400">
                          Supported: JPG, PNG, DICOM
                        </p>
                        <p className="text-xs text-slate-500 mt-2">Max file size: 16MB</p>
                      </div>
                    </label>
                  </div>
                ) : (
                  <div className="space-y-4">
                    <div className="bg-slate-700/30 border border-slate-600/50 rounded-lg p-4">
                      <div className="flex items-center justify-between">
                        <div className="flex items-center gap-3 flex-1 min-w-0">
                          <div className="w-10 h-10 bg-cyan-500/20 rounded-lg flex items-center justify-center flex-shrink-0">
                            <FileText className="w-5 h-5 text-cyan-400" />
                          </div>
                          <div className="flex-1 min-w-0">
                            <p className="text-white font-medium truncate">{currentFile.name}</p>
                            <p className="text-xs text-slate-400">
                              {(currentFile.size / 1024).toFixed(1)} KB
                            </p>
                          </div>
                        </div>
                        <button 
                          onClick={handleRemoveFile}
                          className="w-8 h-8 flex items-center justify-center rounded-lg bg-red-500/10 hover:bg-red-500/20 border border-red-500/30 text-red-400 transition-all flex-shrink-0 ml-3"
                        >
                          <XCircle className="w-4 h-4" />
                        </button>
                      </div>
                    </div>

                    <button 
                      onClick={simulateAnalysis}
                      disabled={analysisState === 'processing'}
                      className="w-full py-3 px-4 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 disabled:from-slate-600 disabled:to-slate-600 text-white font-medium rounded-lg transition-all duration-300 shadow-lg disabled:cursor-not-allowed flex items-center justify-center gap-2"
                    >
                      {analysisState === 'processing' ? (
                        <>
                          <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></div>
                          Processing Analysis...
                        </>
                      ) : (
                        <>
                          <Activity className="w-4 h-4" />
                          Run Analysis
                        </>
                      )}
                    </button>
                  </div>
                )}
              </div>
            </div>

            {/* Analysis Progress */}
            {analysisState === 'processing' && (
              <div className="bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700/50 shadow-xl p-6">
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-10 h-10 bg-cyan-500/20 rounded-lg flex items-center justify-center">
                    <Activity className="w-5 h-5 text-cyan-400 animate-pulse" />
                  </div>
                  <div>
                    <h3 className="text-white font-semibold">Processing</h3>
                    <p className="text-sm text-slate-400">Analyzing image data...</p>
                  </div>
                </div>
                <div className="space-y-2">
                  <div className="flex justify-between text-sm">
                    <span className="text-slate-400">Progress</span>
                    <span className="text-cyan-400 font-medium">{analysisProgress}%</span>
                  </div>
                  <div className="h-2 bg-slate-700 rounded-full overflow-hidden">
                    <div 
                      className="h-full bg-gradient-to-r from-cyan-500 to-blue-500 transition-all duration-300 ease-out"
                      style={{ width: `${analysisProgress}%` }}
                    ></div>
                  </div>
                </div>
              </div>
            )}

            {/* Results */}
            {analysisState === 'success' && (
              <div className="bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700/50 shadow-xl overflow-hidden">
                <div className="bg-gradient-to-r from-emerald-600/10 to-green-600/10 border-b border-slate-700/50 px-6 py-4">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 bg-emerald-500/20 rounded-lg flex items-center justify-center">
                      <CheckCircle className="w-5 h-5 text-emerald-400" />
                    </div>
                    <div>
                      <h3 className="text-white font-semibold">Analysis Complete</h3>
                      <p className="text-sm text-slate-400">Results generated successfully</p>
                    </div>
                  </div>
                </div>

                <div className="p-6 space-y-4">
                  <div className="bg-amber-500/5 border border-amber-500/20 rounded-lg p-4">
                    <p className="text-xs text-amber-400 font-medium mb-1">⚠️ RESEARCH RESULTS ONLY</p>
                    <p className="text-xs text-slate-400">
                      These findings are experimental and must not be used for clinical decisions.
                    </p>
                  </div>

                  <div className="space-y-3">
                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <p className="text-xs text-slate-400 mb-1">PRIMARY FINDINGS</p>
                      <p className="text-white font-medium">No significant abnormalities detected</p>
                    </div>

                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <p className="text-xs text-slate-400 mb-2">MODEL CONFIDENCE</p>
                      <div className="flex items-center gap-3">
                        <div className="flex-1 h-2 bg-slate-700 rounded-full overflow-hidden">
                          <div className="h-full bg-gradient-to-r from-emerald-500 to-green-500 w-[92%]"></div>
                        </div>
                        <span className="text-emerald-400 font-semibold text-sm">92%</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>

          {/* Right Panel - Image Viewer */}
          <div className="bg-slate-800/50 backdrop-blur-sm rounded-xl border border-slate-700/50 shadow-xl overflow-hidden">
            <div className="bg-gradient-to-r from-slate-700/50 to-slate-800/50 border-b border-slate-700/50 px-6 py-4">
              <h2 className="text-lg font-semibold text-white flex items-center gap-2">
                <ImageIcon className="w-5 h-5 text-cyan-400" />
                Image Viewer
              </h2>
              <p className="text-sm text-slate-400 mt-1">PACS-style medical image display</p>
            </div>

            <div className="p-6">
              {previewUrl ? (
                <div className="bg-black rounded-lg overflow-hidden border border-slate-700">
                  <img 
                    src={previewUrl} 
                    alt="X-ray preview" 
                    className="w-full h-auto"
                    style={{ imageRendering: 'crisp-edges' }}
                  />
                </div>
              ) : (
                <div className="aspect-square bg-slate-900/50 rounded-lg border-2 border-dashed border-slate-700 flex items-center justify-center">
                  <div className="text-center">
                    <div className="w-16 h-16 mx-auto mb-4 bg-slate-700/50 rounded-full flex items-center justify-center">
                      <ImageIcon className="w-8 h-8 text-slate-500" />
                    </div>
                    <p className="text-slate-400 font-medium">No image loaded</p>
                    <p className="text-sm text-slate-500 mt-1">Upload an image to view</p>
                  </div>
                </div>
              )}

              {previewUrl && (
                <div className="mt-4 grid grid-cols-3 gap-2 text-xs">
                  <div className="bg-slate-700/30 rounded p-2">
                    <p className="text-slate-400">Patient ID</p>
                    <p className="text-white font-mono">N/A</p>
                  </div>
                  <div className="bg-slate-700/30 rounded p-2">
                    <p className="text-slate-400">Study Date</p>
                    <p className="text-white font-mono">{new Date().toLocaleDateString()}</p>
                  </div>
                  <div className="bg-slate-700/30 rounded p-2">
                    <p className="text-slate-400">Modality</p>
                    <p className="text-white font-mono">XR</p>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Footer Disclaimer */}
        <div className="mt-8 bg-slate-800/30 backdrop-blur-sm rounded-xl border border-slate-700/30 p-6">
          <div className="flex items-start gap-3">
            <AlertTriangle className="w-5 h-5 text-amber-400 flex-shrink-0 mt-0.5" />
            <div className="text-sm text-slate-400 space-y-1">
              <p className="font-medium text-slate-300">Research System Disclaimer</p>
              <p>This platform is an experimental research prototype for academic and technology development purposes. It is NOT FDA-approved, NOT validated for clinical use, and must NOT be used for patient diagnosis or treatment decisions. All results are for research evaluation only and require validation by qualified medical professionals using clinically approved systems.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default XRayResearchPlatform;
