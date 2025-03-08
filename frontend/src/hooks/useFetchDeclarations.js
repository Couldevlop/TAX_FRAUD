import { useState, useEffect } from "react";
import { fetchDeclarations } from "../services/api";

const useFetchDeclarations = () => {
  const [declarations, setDeclarations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchDeclarations();
        setDeclarations(data);
        setLoading(false);
      } catch (err) {
        setError("Failed to fetch declarations");
        setLoading(false);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 30000); // Mise à jour toutes les 30 secondes
    return () => clearInterval(interval);
  }, []);

  return { declarations, loading, error };
};

export default useFetchDeclarations;
