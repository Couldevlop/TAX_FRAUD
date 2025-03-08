import React, { useState } from "react";
import UploadForm from "../components/Declaration/UploadForm";
import ManualForm from "../components/Declaration/ManualForm";

const Declaration = () => {
  const [mode, setMode] = useState("upload"); // 'upload' ou 'manual'
  const [newDeclarations, setNewDeclarations] = useState([]);

  const handleUpload = (data) =>
    setNewDeclarations([...newDeclarations, ...data]);
  const handleManualSubmit = (data) =>
    setNewDeclarations([...newDeclarations, data]);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Submit Declarations</h1>
      <div className="mb-6">
        <button
          onClick={() => setMode("upload")}
          className={`mr-4 p-2 ${
            mode === "upload" ? "bg-blue-500 text-white" : "bg-gray-200"
          }`}
        >
          Upload File
        </button>
        <button
          onClick={() => setMode("manual")}
          className={`p-2 ${
            mode === "manual" ? "bg-blue-500 text-white" : "bg-gray-200"
          }`}
        >
          Manual Entry
        </button>
      </div>
      {mode === "upload" ? (
        <UploadForm onUpload={handleUpload} />
      ) : (
        <ManualForm onSubmit={handleManualSubmit} />
      )}
      {newDeclarations.length > 0 && (
        <div className="mt-6">
          <h3 className="text-xl mb-4">Submitted Declarations</h3>
          <ul className="list-disc pl-5">
            {newDeclarations.map((dec, idx) => (
              <li key={idx}>
                {dec.company_name || "N/A"} - ${dec.amount}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Declaration;
