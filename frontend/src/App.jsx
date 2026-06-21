import { useState } from "react";
import axios from "axios";

function Section({ title, data }) {
  return (
    <div
      style={{
        marginTop: "20px",
        padding: "15px",
        border: "1px solid #444",
        borderRadius: "8px",
        backgroundColor: "#ffffff",
      }}
    >
      <h2
        style={{
          color: "#222",
          marginBottom: "10px",
        }}
      >
        {title}
      </h2>

      <pre
        style={{
          textAlign: "left",
          overflow: "auto",
          whiteSpace: "pre-wrap",
          color: "#333",
        }}
      >
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}

function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateApp = async () => {
    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/generate",
        {
          prompt,
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);
      alert("Backend connection failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        padding: "30px",
        maxWidth: "1200px",
        margin: "auto",
      }}
    >
      <h1>AI App Compiler</h1>

      <textarea
        rows="6"
        style={{
          width: "100%",
          padding: "10px",
        }}
        placeholder="Describe the application..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <br />
      <br />

      <button
        onClick={generateApp}
        style={{
          padding: "10px 20px",
          cursor: "pointer",
        }}
      >
        {loading ? "Generating..." : "Generate"}
      </button>

      {result && (
        <>
          <Section
            title="Intent Extraction"
            data={result.intent}
          />

          <Section
            title="System Design"
            data={result.design}
          />

          <Section
            title="UI Schema"
            data={result.ui}
          />

          <Section
            title="API Schema"
            data={result.api}
          />

          <Section
            title="Database Schema"
            data={result.db}
          />

          <Section
            title="Authentication Rules"
            data={result.auth}
          />

          <Section
            title="Validation Status"
            data={
              result.validation.length === 0
                ? "Validation Passed"
                : result.validation
            }
          />

          <Section
            title="Execution Results"
            data={result.execution}
          />
        </>
      )}
    </div>
  );
}

export default App;