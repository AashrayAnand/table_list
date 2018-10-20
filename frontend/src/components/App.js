import React from "react";
import ReactDOM from "react-dom";
import QueryForm from "./QueryForm";
import DataProvider from "./DataProvider";
import Table from "./Table";
const App = () => (
  <div className="container">
      <h1 className="text-center py-3">LibCal Schedule</h1>
      <div className="row">
        <QueryForm />
        <DataProvider endpoint="api/list/" 
                      render={data => <Table data={data} />} />
      </div>
  </div>
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;