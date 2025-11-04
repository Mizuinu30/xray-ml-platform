const API_BASE_URL = 'http://localhost:8000';

export const analyzeXRay = async (file) => {
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch(`${API_BASE_URL}/api/analyze`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Analysis failed');
    }

    return response.json();
  } catch (error) {
    throw new Error('Analysis failed: ' + error.message);
  }
};

export const healthCheck = async () => {
  const response = await fetch(`${API_BASE_URL}/health`);
  return response.json();
};