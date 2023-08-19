import React, { useState } from "react";
import FileCard from "./FileCard";
import axios from "axios";

function FileForm() {
  const [selectedFiles, setSelectedFiles] = useState([]);

  const handleFileChange = (event) => {
    const fileList = Array.from(event.target.files);
    setSelectedFiles(fileList);
  };

  const handleUpload = async () => {
    if (selectedFiles.length === 0) {
      alert("Please Select a file");
      return;
    }
    console.log("Uploading Files...");
    const formData = new FormData();
    selectedFiles.forEach((file) => {
      formData.append("files", file);
    });
    try {
      const response = await axios.post(
        "http://localhost:8000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
          withCredentials: true,
        }
      );
    } catch (error) {
      console.error("Upload failed:", error);
      alert("Something went wrong!" + error);
      return;
    }

    setSelectedFiles([]);
    const fieldInput = document.getElementById("inputGroupFile");
    fieldInput.value = "";
    alert("Files Uploaded Successfully !");
  };

  return (
    <div className="mt-5 px-2">
      {/* Input form */}
      <div className="mb-3">
        <h3 className="mb-3">Upload Files</h3>
        <div className="input-group">
          <input
            type="file"
            className="form-control"
            id="inputGroupFile"
            aria-describedby="inputGroupFile"
            aria-label="Upload"
            multiple={true}
            onChange={handleFileChange}
          />
          <button
            className="btn btn-outline-secondary"
            type="button"
            id="inputGroupFileAdd"
            onClick={handleUpload}
          >
            Upload
          </button>
        </div>
      </div>

      {/* List files */}
      <div
        style={{
          border: "2px dashed #cbd5e0",
          height: "30vh",
          overflow: "auto",
          borderRadius: "10px",
        }}
        className="p-2"
      >
        {selectedFiles.length !== 0 ? (
          selectedFiles.map((file, index) => (
            <FileCard key={index} name={file.name}></FileCard>
          ))
        ) : (
          <div className="d-flex flex-column justify-content-center align-items-center w-100 h-100">
            <h5 className="align-self-center">No Files Selected</h5>
          </div>
        )}
      </div>
    </div>
  );
}

export default FileForm;
