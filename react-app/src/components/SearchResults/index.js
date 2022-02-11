// import React from "react";
import "./SearchResults.css";
import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
// import { NavLink } from "react-router-dom";
import searchResults from "../../store/project";
import { useDispatch } from "react-redux";

const SearchResults = () => {
  const [searchKeyWord, setSearchKeyWord] = useState("");
  const [projects, setProjects] = useState();
  const dispatch = useDispatch();

  useEffect(() => {
    if (searchKeyWord) {
      async function fetchData() {
        const response = await fetch(`/api/search/${searchKeyWord}`);
        const responseData = await response.json();
        setProjects(responseData.projects);
      }
      fetchData();
    }
  }, [searchKeyWord]);

  const clickToSearch = (e) => {
    e.preventDefault();
    console.log("inside click to search");
    dispatch(searchResults(searchKeyWord));
  };

  // click on cancel search button to clear search results

  let searchBlock;

  if (projects) {
    //console.log(projects)
    searchBlock = projects.map((project, i) => {
      return (
        <a key={`link${i}`} href={`/projects/${project.id}`}>
          <div key={`liked'_${project.id}`}></div>
        </a>
      );
    });
  }

  return (
    <nav>
      <div>
        <form title="Search Form" onSubmit={clickToSearch}>
          <input
            type="text"
            placeholder="Let's Make..."
            onChange={(e) => {
              setSearchKeyWord(e.target.value);
            }}
          />
          <button type="submit">Search Button</button>
        </form>
      </div>
      {searchKeyWord ? (
        <div>
          <h1> Search results for: </h1>
          <h2>{searchKeyWord}</h2>
          <ul>{searchBlock}</ul>
        </div>
      ) : null}
      <h1>Hello from Search Results page</h1>
    </nav>
    // <div className="searchbar">
    //   <div className="search">
    //     <input
    //       placeholder={`Let's Make...`}
    //       type="text"
    //       style={{
    //         width: "80px",
    //         height: "16px",
    //         padding: "6px 10px",
    //         borderRight: "transparent",
    //       }}
    //     ></input>
    //     {/* <img
    //       class="search-icon"
    //       style={{
    //         height: "20px",
    //         border: "2px solid black",
    //         borderLeft: "transparent",
    //       }}
    //       src="data:image/svg+xml;utf8;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pgo8IS0tIEdlbmVyYXRvcjogQWRvYmUgSWxsdXN0cmF0b3IgMTkuMC4wLCBTVkcgRXhwb3J0IFBsdWctSW4gLiBTVkcgVmVyc2lvbjogNi4wMCBCdWlsZCAwKSAgLS0+CjxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgdmVyc2lvbj0iMS4xIiBpZD0iQ2FwYV8xIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDU2Ljk2NiA1Ni45NjYiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDU2Ljk2NiA1Ni45NjY7IiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iMTZweCIgaGVpZ2h0PSIxNnB4Ij4KPHBhdGggZD0iTTU1LjE0Niw1MS44ODdMNDEuNTg4LDM3Ljc4NmMzLjQ4Ni00LjE0NCw1LjM5Ni05LjM1OCw1LjM5Ni0xNC43ODZjMC0xMi42ODItMTAuMzE4LTIzLTIzLTIzcy0yMywxMC4zMTgtMjMsMjMgIHMxMC4zMTgsMjMsMjMsMjNjNC43NjEsMCw5LjI5OC0xLjQzNiwxMy4xNzctNC4xNjJsMTMuNjYxLDE0LjIwOGMwLjU3MSwwLjU5MywxLjMzOSwwLjkyLDIuMTYyLDAuOTIgIGMwLjc3OSwwLDEuNTE4LTAuMjk3LDIuMDc5LTAuODM3QzU2LjI1NSw1NC45ODIsNTYuMjkzLDUzLjA4LDU1LjE0Niw1MS44ODd6IE0yMy45ODQsNmM5LjM3NCwwLDE3LDcuNjI2LDE3LDE3cy03LjYyNiwxNy0xNywxNyAgcy0xNy03LjYyNi0xNy0xN1MxNC42MSw2LDIzLjk4NCw2eiIgZmlsbD0iIzAwMDAwMCIvPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8Zz4KPC9nPgo8L3N2Zz4K"
    //     /> */}
    //   </div>
    // </div>
  );
};

export default SearchResults;
