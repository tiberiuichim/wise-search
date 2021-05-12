// import "./polyfills";
import React from "react";
import ReactDOM from "react-dom";
import { SearchApp } from "@eeacms/search";

const isIE = false || !!document.documentMode;

var mountNode = document.getElementById("search-app");
ReactDOM.render(
  <React.Fragment>
    {isIE && (
      <p className="ie-warning">
        IMPORTANT: This website is not optimised for Internet Explorer. For the
        best experience, please use another browser.
      </p>
    )}
    <SearchApp />
  </React.Fragment>,
  mountNode
);
