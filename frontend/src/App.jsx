import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [textResult, setTextResult] = useState("");

  const [image, setImage] = useState(null);
  const [imageResult, setImageResult] = useState("");

  const handleTextSubmit = async () => {
    try {
      const response = await axios.post("http://localhost:5000/predict-text", {
        text: text,
      });
      setTextResult(response.data.prediction);
    } catch (error) {
      console.error("Error predicting text:", error);
      setTextResult("Error");
    }
  };

  const handleImageSubmit = async () => {
    try {
      const formData = new FormData();
      formData.append("image", image);

      const response = await axios.post("http://localhost:5000/predict-image", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      setImageResult(response.data.prediction);
    } catch (error) {
      console.error("Error predicting image:", error);
      setImageResult("Error");
    }
  };

  return (
    <div className="container">
      <h1>AIn’t - AI vs Human Detector</h1>

      <div className="section">
        <h2>Text Classification</h2>
        <div className="centered">
          <textarea
            placeholder="Paste your text here..."
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </div>
        <button onClick={handleTextSubmit}>Check Text</button>
        {textResult && <p className="result">Result: <strong>{textResult}</strong></p>}
      </div>


      <div className="section">
        <h2>Image Classification</h2>
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setImage(e.target.files[0])}
        />
        <button onClick={handleImageSubmit}>Check Image</button>
        {imageResult && <p className="result">Result: <strong>{imageResult}</strong></p>}
      </div>
    </div>
  );
}

export default App;
