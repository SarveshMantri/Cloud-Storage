import React from "react";

function FileCard({ name }) {
  return (
    <div className="card mx-2 mb-1">
      <div className="card-body">{name}</div>
    </div>
  );
}

export default FileCard;
