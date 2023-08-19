import React from "react";
import moment from "moment";

function TableFile({ tableData }) {
  return (
    <table className="table table-hover">
      <thead>
        <tr>
          <th>NO</th>
          <th>File Name</th>
          <th>AWS Name</th>
          <th>File Type</th>
          <th>Size</th>
          <th>Upload Date</th>
        </tr>
      </thead>
      <tbody>
        {tableData.map((item, i) => (
          <tr key={i + 1}>
            <td>{i + 1}</td>
            <td>{item.name}</td>
            <td>{item.awsName}</td>
            <td>{item.type}</td>
            <td>{item.size.toFixed(2)} KB</td>
            <td>{moment(item.date).format("DD-MM-YYYY HH:mm:ss")}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default TableFile;
