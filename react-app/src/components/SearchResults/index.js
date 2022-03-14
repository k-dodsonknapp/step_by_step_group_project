// import React from "react";
import "./SearchResults.css";
import React, { useState, useEffect, useLayoutEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink, useHistory, Redirect } from "react-router-dom";
import { search } from "../../store/project";
import { useDispatch } from "react-redux";

const SearchResults = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchKeyWord, setSearchKeyWord] = useState("");
  const [projects, setProjects] = useState();
  const [errors, setErrors] = useState([]);

  const errSearch = () => {
    const searchErrors = [];

    if (searchKeyWord < 3) {
      searchErrors.push("Please enter a search")
    }
    setErrors(searchErrors);
    return searchErrors;
  }

  const clickToSearch = (e) => {
    e.preventDefault();
    const searchErr = errSearch();
    if (searchErr.length > 0) return;
    dispatch(search(searchKeyWord));
    setSearchKeyWord('')
    history.push(`/howto/${searchKeyWord}`);
    // return <Redirect to={`/howto/${searchKeyWord}`} />;
  };



  // click on cancel search button to clear search results

  // let searchBlock;

  // if (projects) {
  //   //console.log(projects)
  //   searchBlock = projects.map((project, i) => {
  //     return (
  //       <a key={`link${i}`} href={`/projects/${project.id}`}>
  //         <div key={`liked'_${project.id}`}></div>
  //       </a>
  //     );
  //   });
  // }

  return (
    <div>
      <form title="Search Form" onSubmit={clickToSearch}>
        {errors && errors.map(err => (
          <p key={err}>{err}</p>
        ))}
        <input
          className="search-field"
          type="text"
          placeholder="Let's Make..."
          value={searchKeyWord}
          onChange={(e) => {
            setSearchKeyWord(e.target.value);
          }}
        />
        <button className='search-btn'type="submit">Search Button</button>
      </form>
    </div>
  );
};

export default SearchResults;
