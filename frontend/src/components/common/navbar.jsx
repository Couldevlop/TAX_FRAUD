import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import { FaHome, FaChartLine, FaFileAlt, FaSignOutAlt } from "react-icons/fa"; // Icônes pour les liens

const Navbar = () => {
  const { isAuthenticated, logout } = useAuth();
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <nav className="bg-gradient-to-r from-blue-600 to-purple-600 shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          {/* Logo et nom de l'application */}
          <Link
            to="/"
            className="text-xl font-bold text-white flex items-center"
          >
            <img
              src="/logo.PNG" // Remplacez par le chemin de votre logo
              alt="Logo"
              className="h-8 w-8 mr-2"
            />
            Tax Fraud Detection
          </Link>

          {/* Menu pour les grands écrans */}
          {isAuthenticated && (
            <div className="hidden md:flex items-center space-x-6">
              <Link
                to="/"
                className="text-white hover:text-gray-200 transition duration-300 flex items-center"
              >
                <FaHome className="mr-2" />
                Home
              </Link>
              <Link
                to="/dashboard"
                className="text-white hover:text-gray-200 transition duration-300 flex items-center"
              >
                <FaChartLine className="mr-2" />
                Dashboard
              </Link>
              <Link
                to="/declaration"
                className="text-white hover:text-gray-200 transition duration-300 flex items-center"
              >
                <FaFileAlt className="mr-2" />
                Declarations
              </Link>
              <button
                onClick={logout}
                className="bg-red-500 px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300 flex items-center"
              >
                <FaSignOutAlt className="mr-2" />
                Logout
              </button>
            </div>
          )}

          {/* Menu pour les petits écrans */}
          {isAuthenticated && (
            <div className="md:hidden">
              <button
                onClick={() => setIsMenuOpen(!isMenuOpen)}
                className="text-white focus:outline-none"
              >
                <svg
                  className="h-6 w-6"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M4 6h16M4 12h16m-7 6h7"
                  />
                </svg>
              </button>
            </div>
          )}
        </div>

        {/* Menu déroulant pour les petits écrans */}
        {isAuthenticated && isMenuOpen && (
          <div className="md:hidden mt-4 pb-4">
            <Link
              to="/"
              className="block text-white hover:text-gray-200 transition duration-300 py-2 flex items-center"
            >
              <FaHome className="mr-2" />
              Home
            </Link>
            <Link
              to="/dashboard"
              className="block text-white hover:text-gray-200 transition duration-300 py-2 flex items-center"
            >
              <FaChartLine className="mr-2" />
              Dashboard
            </Link>
            <Link
              to="/declaration"
              className="block text-white hover:text-gray-200 transition duration-300 py-2 flex items-center"
            >
              <FaFileAlt className="mr-2" />
              Declarations
            </Link>
            <button
              onClick={logout}
              className="w-full bg-red-500 px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300 flex items-center justify-center mt-2"
            >
              <FaSignOutAlt className="mr-2" />
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
