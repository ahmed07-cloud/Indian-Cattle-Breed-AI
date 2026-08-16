import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  // ============================================================
  // PREDICTION STATES
  // ============================================================

  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // ============================================================
  // BREED EXPLORER STATES
  // ============================================================

  const [breeds, setBreeds] = useState([]);
  const [showBreeds, setShowBreeds] = useState(false);
  const [breedsLoading, setBreedsLoading] = useState(false);

  const [selectedBreed, setSelectedBreed] = useState(null);
  const [breedDetailsLoading, setBreedDetailsLoading] = useState(false);

  // ============================================================
  // STEP 2 - BREED SEARCH
  // ============================================================

  const [breedSearch, setBreedSearch] = useState("");

  // ============================================================
  // IMAGE SELECTION
  // ============================================================

  const handleFileChange = (event) => {
    const file = event.target.files?.[0];

    if (!file) return;

    if (!file.type.startsWith("image/")) {
      setError("Please select a valid image file.");
      return;
    }

    setSelectedFile(file);
    setPreview(URL.createObjectURL(file));

    setResult(null);
    setError("");
  };

  // ============================================================
  // PREDICT BREED
  // ============================================================

  const handlePredict = async () => {
    if (!selectedFile) {
      setError("Please select a cattle image first.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", selectedFile);

    try {
      const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        body: formData,
      });

      let data;

      try {
        data = await response.json();
      } catch {
        throw new Error("Backend returned an invalid response.");
      }

      if (!response.ok) {
        throw new Error(data?.detail || "Prediction failed.");
      }

      console.log("Prediction response:", data);

      setResult(data);
    } catch (err) {
      console.error("Prediction error:", err);

      setError(
        err.message ||
          "Could not connect to the backend. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };

  // ============================================================
  // EXPLORE BREEDS
  // ============================================================

  const handleExploreBreeds = async () => {
    setBreedsLoading(true);
    setError("");
    setSelectedBreed(null);

    try {
      const response = await fetch(`${API_URL}/breeds`);

      let data;

      try {
        data = await response.json();
      } catch {
        throw new Error("Backend returned an invalid response.");
      }

      if (!response.ok) {
        throw new Error(
          data?.detail || "Failed to load breeds."
        );
      }

      if (!Array.isArray(data?.breeds)) {
        throw new Error(
          "Invalid breed data received from backend."
        );
      }

      setBreeds(data.breeds);
      setShowBreeds(true);
      setBreedSearch("");
    } catch (err) {
      console.error("Breed explorer error:", err);

      setError(
        err.message ||
          "Could not load breeds. Make sure FastAPI is running."
      );
    } finally {
      setBreedsLoading(false);
    }
  };

  // ============================================================
  // STEP 3 - BREED DETAILS
  // ============================================================

  const handleBreedClick = async (breedName) => {
    setBreedDetailsLoading(true);
    setError("");
    setSelectedBreed(null);

    try {
      const response = await fetch(
        `${API_URL}/breeds/${encodeURIComponent(breedName)}`
      );

      let data;

      try {
        data = await response.json();
      } catch {
        throw new Error(
          "Backend returned an invalid response."
        );
      }

      if (!response.ok) {
        throw new Error(
          data?.detail ||
            "Failed to load breed information."
        );
      }

      console.log("Selected breed:", data);

      setSelectedBreed(data);
    } catch (err) {
      console.error("Breed details error:", err);

      setError(
        err.message ||
          "Could not load breed information."
      );
    } finally {
      setBreedDetailsLoading(false);
    }
  };

  // ============================================================
  // SAFE INFORMATION
  // ============================================================

  const predictionInfo = result?.breed_info || {};

  const selectedInfo =
    selectedBreed?.information || {};

  // ============================================================
  // STEP 2 - FILTER BREEDS
  // ============================================================

  const searchText = breedSearch.trim().toLowerCase();

  const filteredBreeds = breeds.filter((breed) =>
    String(breed)
      .toLowerCase()
      .includes(searchText)
  );

  // ============================================================
  // UI
  // ============================================================

  return (
    <div className="app">

      {/* ======================================================
          HEADER
      ====================================================== */}

      <header className="header">
        <h1>🐄 Indian Cattle Breed AI</h1>

        <p>
          AI-powered Indian cattle and buffalo breed
          identification
        </p>
      </header>


      <main className="container">

        {/* ====================================================
            UPLOAD CARD
        ==================================================== */}

        <section className="upload-card">

          <h2>Identify a Cattle Breed</h2>

          <p className="description">
            Upload an image of an Indian cattle or buffalo breed.
          </p>


          {/* IMAGE UPLOAD */}

          <label className="upload-area">

            <input
              type="file"
              accept="image/*"
              onChange={handleFileChange}
            />

            {preview ? (
              <img
                src={preview}
                alt="Cattle preview"
                className="preview-image"
              />
            ) : (
              <div className="upload-placeholder">

                <div className="upload-icon">
                  📷
                </div>

                <h3>
                  Upload Cattle Image
                </h3>

                <p>
                  Click here to choose an image
                </p>

              </div>
            )}

          </label>


          {/* FILE NAME */}

          {selectedFile && (
            <p className="filename">
              Selected: {selectedFile.name}
            </p>
          )}


          {/* PREDICT BUTTON */}

          <button
            className="predict-button"
            onClick={handlePredict}
            disabled={!selectedFile || loading}
          >
            {loading
              ? "🔄 Predicting..."
              : "🔍 Predict Breed"}
          </button>


          {/* ERROR */}

          {error && (
            <div className="error">
              {error}
            </div>
          )}

        </section>


        {/* ====================================================
            PREDICTION RESULT
        ==================================================== */}

        {result && (
          <section className="result-card">

            <h2>
              Prediction Result
            </h2>


            {/* MAIN RESULT */}

            <div className="main-result">

              <div className="result-label">
                Predicted Breed
              </div>

              <h3>
                🐄 {result.breed || "Unknown Breed"}
              </h3>


              {/* CONFIDENCE */}

              <div className="confidence-section">

                <div className="confidence">

                  Confidence:{" "}

                  <strong>
                    {result.confidence ?? 0}%
                  </strong>

                </div>


                <div className="confidence-bar">

                  <div
                    className="confidence-fill"
                    style={{
                      width: `${Math.min(
                        Math.max(
                          Number(result.confidence) || 0,
                          0
                        ),
                        100
                      )}%`,
                    }}
                  />

                </div>


                <div className="confidence-level">

                  {Number(result.confidence) >= 75
                    ? "🟢 High Confidence"
                    : Number(result.confidence) >= 50
                    ? "🟡 Medium Confidence"
                    : "🔴 Low Confidence"}

                </div>


                <div className="confidence-explanation">

                  {Number(result.confidence) >= 75
                    ? "The AI is highly confident that this image matches the predicted breed."
                    : Number(result.confidence) >= 50
                    ? "The AI has moderate confidence. Check the Top Predictions before confirming the breed."
                    : "The AI has low confidence. Try uploading a clearer image showing the cattle's full body and distinctive features."}

                </div>

              </div>

            </div>


            {/* TOP 3 PREDICTIONS */}

            <div className="top-predictions">

              <h3>
                Top Predictions
              </h3>

              {Array.isArray(result.top_3) &&
              result.top_3.length > 0 ? (

                result.top_3.map(
                  (prediction, index) => (
                    <div
                      className="prediction-row"
                      key={`${prediction.breed}-${index}`}
                    >

                      <span>
                        {index + 1}.{" "}
                        {prediction.breed}
                      </span>

                      <strong>
                        {prediction.confidence}%
                      </strong>

                    </div>
                  )
                )

              ) : (
                <p>
                  Top predictions are not available.
                </p>
              )}

            </div>


            {/* TOP CHARACTERISTICS */}

            {result.breed_info && (

              <div className="top-characteristics">

                <h3>
                  ⭐ Top Characteristics
                </h3>

                <div className="characteristic-list">

                  <div className="characteristic-item">

                    <span>🥛</span>

                    <div>

                      <strong>
                        Purpose
                      </strong>

                      <p>
                        {predictionInfo.purpose ||
                          "Information not available"}
                      </p>

                    </div>

                  </div>


                  <div className="characteristic-item">

                    <span>🐄</span>

                    <div>

                      <strong>
                        Appearance
                      </strong>

                      <p>
                        {predictionInfo.appearance ||
                          "Information not available"}
                      </p>

                    </div>

                  </div>


                  <div className="characteristic-item">

                    <span>☀️</span>

                    <div>

                      <strong>
                        Climate
                      </strong>

                      <p>
                        {predictionInfo.climate ||
                          "Information not available"}
                      </p>

                    </div>

                  </div>


                  <div className="characteristic-item">

                    <span>✨</span>

                    <div>

                      <strong>
                        Special Feature
                      </strong>

                      <p>
                        {predictionInfo.special_features ||
                          "Information not available"}
                      </p>

                    </div>

                  </div>

                </div>

              </div>

            )}


            {/* COMPLETE BREED INFORMATION */}

            {result.breed_info && (

              <div className="breed-info">

                <h3>
                  Breed Characteristics
                </h3>

                <div className="info-grid">

                  <div>
                    <strong>
                      Origin
                    </strong>

                    <p>
                      {predictionInfo.origin ||
                        "Information not available"}
                    </p>
                  </div>


                  <div>
                    <strong>
                      Type
                    </strong>

                    <p>
                      {predictionInfo.type ||
                        "Information not available"}
                    </p>
                  </div>


                  <div>
                    <strong>
                      Purpose
                    </strong>

                    <p>
                      {predictionInfo.purpose ||
                        "Information not available"}
                    </p>
                  </div>


                  <div>
                    <strong>
                      Appearance
                    </strong>

                    <p>
                      {predictionInfo.appearance ||
                        "Information not available"}
                    </p>
                  </div>


                  <div>
                    <strong>
                      Climate
                    </strong>

                    <p>
                      {predictionInfo.climate ||
                        "Information not available"}
                    </p>
                  </div>


                  <div>
                    <strong>
                      Special Features
                    </strong>

                    <p>
                      {predictionInfo.special_features ||
                        "Information not available"}
                    </p>
                  </div>

                </div>

              </div>

            )}

          </section>
        )}


        {/* ====================================================
            BREED EXPLORER
        ==================================================== */}

        <section className="breed-explorer">

          <h2>
            🐄 Breed Explorer
          </h2>

          <p>
            Explore Indian cattle and buffalo breeds and
            learn about their characteristics.
          </p>


          {/* EXPLORE BUTTON */}

          <button
            className="explorer-button"
            onClick={handleExploreBreeds}
            disabled={breedsLoading}
          >

            {breedsLoading
              ? "🔄 Loading Breeds..."
              : "🔎 Explore Breeds"}

          </button>


          {/* ==================================================
              STEP 2 - SEARCH
          ================================================== */}

          {showBreeds && (

            <div className="breed-controls">

              <input
                type="text"
                className="breed-search"
                placeholder="🔍 Search breed..."
                value={breedSearch}
                onChange={(event) =>
                  setBreedSearch(event.target.value)
                }
              />

            </div>

          )}


          {/* ==================================================
              BREED LIST
          ================================================== */}

          {showBreeds && (

            <div className="breed-list">

              <h3>
                Indian Cattle & Buffalo Breeds (
                {filteredBreeds.length}
                )
              </h3>


              {filteredBreeds.length === 0 ? (

                <div className="no-breeds">
                  🔍 No breed found.
                </div>

              ) : (

                <div className="breed-grid">

                  {filteredBreeds.map(
                    (breed, index) => (

                      <button
                        key={`${breed}-${index}`}
                        className="breed-item"
                        onClick={() =>
                          handleBreedClick(breed)
                        }
                      >

                        🐄 {breed}

                      </button>

                    )
                  )}

                </div>

              )}

            </div>

          )}


          {/* ==================================================
              STEP 3 - BREED DETAILS LOADING
          ================================================== */}

          {breedDetailsLoading && (

            <div className="breed-loading">

              🔄 Loading breed information...

            </div>

          )}


          {/* ==================================================
              STEP 3 - SELECTED BREED DETAILS
          ================================================== */}

          {selectedBreed && (

            <div className="selected-breed-card">

              <h3>
                🐄 {selectedBreed.breed || "Breed Details"}
              </h3>


              <div className="breed-details-grid">

                {/* ORIGIN */}

                <div className="breed-detail-item">

                  <strong>
                    📍 Origin
                  </strong>

                  <p>
                    {selectedInfo.origin ||
                      "Information not available"}
                  </p>

                </div>


                {/* TYPE */}

                <div className="breed-detail-item">

                  <strong>
                    🐄 Type
                  </strong>

                  <p>
                    {selectedInfo.type ||
                      "Information not available"}
                  </p>

                </div>


                {/* PURPOSE */}

                <div className="breed-detail-item">

                  <strong>
                    🥛 Purpose
                  </strong>

                  <p>
                    {selectedInfo.purpose ||
                      "Information not available"}
                  </p>

                </div>


                {/* APPEARANCE */}

                <div className="breed-detail-item">

                  <strong>
                    👀 Appearance
                  </strong>

                  <p>
                    {selectedInfo.appearance ||
                      "Information not available"}
                  </p>

                </div>


                {/* CLIMATE */}

                <div className="breed-detail-item">

                  <strong>
                    ☀️ Climate
                  </strong>

                  <p>
                    {selectedInfo.climate ||
                      "Information not available"}
                  </p>

                </div>


                {/* SPECIAL FEATURES */}

                <div className="breed-detail-item">

                  <strong>
                    ⭐ Special Features
                  </strong>

                  <p>
                    {selectedInfo.special_features ||
                      "Information not available"}
                  </p>

                </div>

              </div>

            </div>

          )}

        </section>

      </main>

    </div>
  );
}

export default App;