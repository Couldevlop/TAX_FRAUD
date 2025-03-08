import React from "react";
import { FaFacebook, FaTwitter, FaLinkedin, FaEnvelope } from "react-icons/fa"; // Icônes pour les liens sociaux

function Footer() {
  return (
    <footer className="bg-gradient-to-r from-blue-600 to-purple-600 text-white py-8 mt-auto">
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Section À propos */}
          <div className="text-center md:text-left">
            <h3 className="text-xl font-bold mb-4">About Us</h3>
            <p className="text-sm">
              Tax Fraud Detection is a cutting-edge platform designed to help
              businesses detect and prevent tax fraud using advanced AI
              technology.
            </p>
          </div>

          {/* Section Liens rapides */}
          <div className="text-center">
            <h3 className="text-xl font-bold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <a
                  href="/about"
                  className="hover:text-gray-200 transition duration-300"
                >
                  About
                </a>
              </li>
              <li>
                <a
                  href="/contact"
                  className="hover:text-gray-200 transition duration-300"
                >
                  Contact
                </a>
              </li>
              <li>
                <a
                  href="/privacy"
                  className="hover:text-gray-200 transition duration-300"
                >
                  Privacy Policy
                </a>
              </li>
              <li>
                <a
                  href="/terms"
                  className="hover:text-gray-200 transition duration-300"
                >
                  Terms of Service
                </a>
              </li>
            </ul>
          </div>

          {/* Section Newsletter */}
          <div className="text-center md:text-right">
            <h3 className="text-xl font-bold mb-4">
              Subscribe to Our Newsletter
            </h3>
            <form className="flex justify-center md:justify-end">
              <input
                type="email"
                placeholder="Your email"
                className="p-2 rounded-l-lg focus:outline-none text-gray-800"
              />
              <button
                type="submit"
                className="bg-blue-500 px-4 py-2 rounded-r-lg hover:bg-blue-600 transition duration-300"
              >
                <FaEnvelope />
              </button>
            </form>
          </div>
        </div>

        {/* Section Réseaux sociaux */}
        <div className="flex justify-center space-x-6 mt-8">
          <a
            href="https://facebook.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-white hover:text-gray-200 transition duration-300"
          >
            <FaFacebook size={24} />
          </a>
          <a
            href="https://twitter.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-white hover:text-gray-200 transition duration-300"
          >
            <FaTwitter size={24} />
          </a>
          <a
            href="https://linkedin.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-white hover:text-gray-200 transition duration-300"
          >
            <FaLinkedin size={24} />
          </a>
        </div>

        {/* Section Droits d'auteur */}
        <div className="text-center mt-8 border-t border-gray-700 pt-4">
          <p className="text-sm">
            &copy; {new Date().getFullYear()} Tax Fraud Detection. All rights
            reserved.
          </p>
          <p className="text-sm mt-2">
            Powered by{" "}
            <a
              href="https://openlabconsulting.com"
              target="_blank"
              rel="noopener noreferrer"
              className="underline hover:text-gray-200 transition duration-300"
            >
              OPENLAB CONSULTING
            </a>
          </p>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
