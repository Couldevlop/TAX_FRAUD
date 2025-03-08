import React from "react";

const Home = () => {
  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-50 to-purple-50 py-12">
      {/* Section Héros */}
      <div className="container mx-auto px-4 text-center">
        <h1 className="text-5xl font-bold text-gray-800 mb-6 animate-fade-in">
          Welcome to Tax Fraud Detection
        </h1>
        <p className="text-xl text-gray-600 mb-8 animate-fade-in delay-100">
          Empowering businesses to detect and prevent tax fraud with
          cutting-edge AI technology.
        </p>
        <button className="bg-blue-600 text-white px-8 py-3 rounded-lg shadow-lg hover:bg-blue-700 transition duration-300 animate-fade-in delay-200">
          Get Started
        </button>
      </div>

      {/* Section Fonctionnalités */}
      <div className="container mx-auto px-4 mt-16">
        <h2 className="text-3xl font-bold text-gray-800 text-center mb-8 animate-fade-in delay-300">
          Key Features
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Carte 1 */}
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition duration-300 animate-fade-in delay-400">
            <div className="text-blue-600 text-4xl mb-4">📊</div>
            <h3 className="text-xl font-semibold mb-4">Advanced Analytics</h3>
            <p className="text-gray-600">
              Analyze declarations with powerful machine learning models to
              detect anomalies.
            </p>
          </div>

          {/* Carte 2 */}
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition duration-300 animate-fade-in delay-500">
            <div className="text-purple-600 text-4xl mb-4">📂</div>
            <h3 className="text-xl font-semibold mb-4">File Upload</h3>
            <p className="text-gray-600">
              Easily upload CSV or JSON files for quick and accurate fraud
              detection.
            </p>
          </div>

          {/* Carte 3 */}
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition duration-300 animate-fade-in delay-600">
            <div className="text-green-600 text-4xl mb-4">📈</div>
            <h3 className="text-xl font-semibold mb-4">Real-Time Dashboard</h3>
            <p className="text-gray-600">
              Monitor fraud detection results in real-time with dynamic charts
              and tables.
            </p>
          </div>
        </div>
      </div>

      {/* Section Statistiques */}
      <div className="container mx-auto px-4 mt-16">
        <h2 className="text-3xl font-bold text-gray-800 text-center mb-8 animate-fade-in delay-700">
          Why Choose Us?
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="text-center">
            <div className="text-5xl font-bold text-blue-600">95%</div>
            <p className="text-gray-600">Accuracy Rate</p>
          </div>
          <div className="text-center">
            <div className="text-5xl font-bold text-purple-600">10K+</div>
            <p className="text-gray-600">Declarations Analyzed</p>
          </div>
          <div className="text-center">
            <div className="text-5xl font-bold text-green-600">24/7</div>
            <p className="text-gray-600">Support Available</p>
          </div>
        </div>
      </div>

      {/* Section Témoignages */}
      {/* <div className="container mx-auto px-4 mt-16">
        <h2 className="text-3xl font-bold text-gray-800 text-center mb-8 animate-fade-in delay-800">
          What Our Users Say
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <p className="text-gray-600 italic">
              "This platform has revolutionized how we detect tax fraud. Highly
              recommended!"
            </p>
            <p className="text-gray-800 font-semibold mt-4">- John Doe, CFO</p>
          </div>
          <div className="bg-white p-8 rounded-lg shadow-md hover:shadow-lg transition duration-300">
            <p className="text-gray-600 italic">
              "The real-time dashboard is a game-changer for our team."
            </p>
            <p className="text-gray-800 font-semibold mt-4">
              - Jane Smith, Tax Analyst
            </p>
          </div>
        </div>
      </div> */}
    </div>
  );
};

export default Home;
