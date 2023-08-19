import "./App.css";
import FileDisplay from "./components/FileDisplay";
import FileForm from "./components/FileForm";

function App() {
  return (
    <>
      <div className="container-md">
        <FileForm></FileForm>
        <FileDisplay></FileDisplay>
      </div>
    </>
  );
}

export default App;
