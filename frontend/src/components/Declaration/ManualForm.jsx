import React, { useState } from "react";
import { createDeclaration } from "../../services/api";

const ManualForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    company_name: "",
    declaration_type: "income",
    amount: "",
    sector: "",
    region: "",
    fiscal_year: 2023,
  });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await createDeclaration(formData);
      onSubmit(response.data);
      setFormData({
        company_name: "",
        declaration_type: "income",
        amount: "",
        sector: "",
        region: "",
        fiscal_year: 2023,
      });
      setError("");
    } catch (err) {
      setError("Submission failed. Please check your input.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="p-4 bg-white shadow-md rounded">
      <h3 className="text-xl mb-4">Manual Declaration Entry</h3>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <div className="mb-4">
        <label className="block mb-1">Company Name</label>
        <input
          name="company_name"
          value={formData.company_name}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        />
      </div>
      <div className="mb-4">
        <label className="block mb-1">Type</label>
        <select
          name="declaration_type"
          value={formData.declaration_type}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        >
          <option value="income">Income</option>
          <option value="vat">VAT</option>
          <option value="corporate">Corporate</option>
        </select>
      </div>
      <div className="mb-4">
        <label className="block mb-1">Amount</label>
        <input
          name="amount"
          type="number"
          value={formData.amount}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block mb-1">Sector</label>
        <input
          name="sector"
          value={formData.sector}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        />
      </div>
      <div className="mb-4">
        <label className="block mb-1">Region</label>
        <input
          name="region"
          value={formData.region}
          onChange={handleChange}
          className="w-full p-2 border rounded"
        />
      </div>
      <div className="mb-4">
        <label className="block mb-1">Fiscal Year</label>
        <input
          name="fiscal_year"
          type="number"
          value={formData.fiscal_year}
          onChange={handleChange}
          className="w-full p-2 border rounded"
          required
        />
      </div>
      <button
        type="submit"
        className="bg-blue-500 text-white p-2 rounded hover:bg-blue-600"
      >
        Submit
      </button>
    </form>
  );
};

export default ManualForm;
