// src/App.jsx
import React, { useState } from 'react';
import PDFDropzone from './components/PDFDropzone';
import LoadingSpinner from './components/LoadingSpinner';
import DetailsDisplay from './components/DetailsDisplay';
import useCVUploader from './hooks/useCVUploader';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const { uploadCV, data, loading, error } = useCVUploader();
  const handleFileAccepted = async (file) => {
    setSelectedFile(file);
    await uploadCV(file);
  };
  return (
    <div className="fixed inset-0 bg-gray-100 overflow-auto p-4">
      <div className="max-w-3xl mx-auto text-center">
        <h1 className="text-3xl text-primary mb-6 pt-8">Carica Curriculum</h1>

        {!selectedFile && <PDFDropzone onFileAccepted={handleFileAccepted} />}
        {loading && <LoadingSpinner />}
        {error && <p className="text-red-500 mt-4">{error}</p>}
        {data && <DetailsDisplay details={data} />}
      </div>
    </div>
  );
}

export default App;



