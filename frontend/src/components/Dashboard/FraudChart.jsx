import React from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

const Navbar = () => {
  const { isAuthenticated, logout } = useAuth();

  return (
    <nav className="bg-gray-800 p-4 text-white">
      <div className="container mx-auto flex justify-between">
        <Link to="/" className="text-xl font-bold">
          Tax Fraud Detection
        </Link>
        {isAuthenticated && (
          <div>
            <Link to="/" className="mr-4">
              Home
            </Link>
            <Link to="/dashboard" className="mr-4">
              Dashboard
            </Link>
            <Link to="/declaration" className="mr-4">
              Declarations
            </Link>
            <button onClick={logout} className="bg-red-500 px-3 py-1 rounded">
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
