// import React from "react";
import "./SearchResults.css";
import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink, useHistory, Redirect } from "react-router-dom";
import { search } from "../../store/project";
import { useDispatch } from "react-redux";

const SearchResults = () => {
  const [searchKeyWord, setSearchKeyWord] = useState("");
  const [projects, setProjects] = useState();
  const dispatch = useDispatch();
  const history = useHistory();

  const clickToSearch = (e) => {
    e.preventDefault();
    console.log("inside click to search");
    dispatch(search(searchKeyWord));
    history.push(`/howto/${searchKeyWord}`);
    // return <Redirect to={`/howto/${searchKeyWord}`} />;
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
    <div>
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
            {/* <h1> Search results for: </h1> */}
            {/* <h2>{searchKeyWord}</h2> */}
            <ul>{searchBlock}</ul>
          </div>
        ) : null}
        {/* <h1>Hello from Search Results page</h1> */}
      </nav>

      <ul>{searchBlock}</ul>
    </div>
  );
};

export default SearchResults;
