import React, { useEffect, useState } from "react";
import TableFile from "./TableFile";

function FileDisplay({ tableData }) {
  return (
    <div className="mt-5 px-2">
      <div className="mb-3">
        <h3 className="mb-3">S3 Bucket Files</h3>
      </div>

      <div
        style={{
          border: "2px dashed #cbd5e0",
          height: "30vh",
          overflow: "auto",
          borderRadius: "10px",
        }}
        className="p-2"
      >
        {tableData.length !== 0 ? (
          <TableFile tableData={tableData}></TableFile>
        ) : (
          <div className="d-flex flex-column justify-content-center align-items-center w-100 h-100">
            <h5 className="align-self-center">No Files Uploaded</h5>
          </div>
        )}
      </div>
    </div>
  );
}

export default FileDisplay;
