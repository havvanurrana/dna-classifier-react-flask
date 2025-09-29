import { useState } from "react";

function App() {
  const [sequence, setSequence] = useState(""); // inputu tutacak state
  const [result, setResult] = useState("");     // sonucu tutacak state

  const handlePredict = async () => {
      const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sequence }), // DNA dizisini gönderiyoruz
    });

    const data = await response.json();
    setResult(data.prediction); // Flask’tan gelen cevabı ekrana yaz
  };

  return (
    <div style={{ margin: "2rem" }}>
      <h1>DNA Classifier</h1>

      <input
        type="text"
        placeholder="DNA sequence (ATCG...)"
        value={sequence}
        onChange={(e) => setSequence(e.target.value)}
        style={{ padding: "0.5rem", width: "300px" }}
      />

      <button
        onClick={handlePredict}
        style={{ marginLeft: "1rem", padding: "0.5rem 1rem" }}
      >
        Predict
      </button>

      {result && (
        <h2 style={{ marginTop: "1rem" }}>
          Prediction: <span>{result}</span>
        </h2>
      )}
    </div>
  );
}

export default App;
