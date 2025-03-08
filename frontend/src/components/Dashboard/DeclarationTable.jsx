import React from "react";

const DeclarationTable = ({ declarations }) => {
  return (
    <div className="bg-white p-4 shadow-md rounded">
      <h3 className="text-xl mb-4">Recent Declarations</h3>
      <table className="w-full border-collapse">
        <thead>
          <tr className="bg-gray-200">
            <th className="p-2">ID</th>
            <th className="p-2">Company</th>
            <th className="p-2">Type</th>
            <th className="p-2">Amount</th>
            <th className="p-2">Status</th>
            <th className="p-2">Fraud Score</th>
          </tr>
        </thead>
        <tbody>
          {declarations.map((dec) => (
            <tr key={dec.id} className="border-t">
              <td className="p-2">{dec.id}</td>
              <td className="p-2">{dec.company_name || "N/A"}</td>
              <td className="p-2">{dec.declaration_type}</td>
              <td className="p-2">${dec.amount.toLocaleString()}</td>
              <td className="p-2">{dec.status}</td>
              <td className="p-2">
                {dec.fraudPrediction?.ensemble_score.toFixed(2) || "N/A"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default DeclarationTable;
