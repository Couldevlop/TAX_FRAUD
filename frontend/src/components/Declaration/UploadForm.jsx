import React, { useState } from "react";
import { uploadDeclarations } from "../../services/api";

const UploadForm = ({ onUpload }) => {
  const [file, setFile] = useState(null);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setError("Please select a file");
      return;
    }
    try {
      const formData = new FormData();
      formData.append("file", file);
      const response = await uploadDeclarations(formData);
      onUpload(response.data);
      setFile(null);
      setError("");
    } catch (err) {
      setError("Upload failed. Please try again.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 bg-white shadow-md rounded">
      <h3 className="text-xl mb-4">Upload Declaration File</h3>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
        accept=".csv,.json"
      />
      <button
        type="submit"
        className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
      >
        Upload
      </button>
    </form>
  );
};

export default UploadForm;
