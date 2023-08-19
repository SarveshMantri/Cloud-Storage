import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";
import FileDisplay from "./components/FileDisplay";
import FileForm from "./components/FileForm";

function App() {
  const [tableData, setTableData] = useState([]);

  const fetchApiData = async () => {
    try {
      const response = await axios.get(
        "http://localhost:8000/all-file-attributes"
      );
      setTableData(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchApiData();
  }, []);
  return (
    <>
      <div className="container-md">
        <FileForm fetchApiData={fetchApiData}></FileForm>
        <FileDisplay tableData={tableData}></FileDisplay>
      </div>
    </>
  );
}

export default App;
