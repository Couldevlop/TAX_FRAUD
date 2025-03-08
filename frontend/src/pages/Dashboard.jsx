import React from "react";
import FraudChart from "../components/Dashboard/FraudChart";
import DeclarationTable from "../components/Dashboard/DeclarationTable";
import useFetchDeclarations from "../hooks/useFetchDeclarations";

const Dashboard = () => {
  const { declarations, loading, error } = useFetchDeclarations();

  if (loading) return <p className="text-center">Loading...</p>;
  if (error) return <p className="text-center text-red-500">{error}</p>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      <div className="grid grid-cols-1 gap-6">
        <FraudChart data={declarations} />
        <DeclarationTable declarations={declarations} />
      </div>
    </div>
  );
};

export default Dashboard;
