// import React from "react";
import "./SearchResults.css";
import React, { useState } from "react";
// import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { search } from "../../store/project";
import { useDispatch } from "react-redux";

const SearchResults = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchKeyWord, setSearchKeyWord] = useState("");
  // const [projects, setProjects] = useState();
  let [errors, setErrors] = useState("Let's make...");

  const errSearch = () => {
    let searchErrors = '';

    if (searchKeyWord < 3) {
      searchErrors = "Please enter a search"
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
  };

  return (
    <>
      <div>
        <form title="Search Form" onSubmit={clickToSearch}>
          <input
            className="search-field"
            type="text"
            placeholder={errors}
            value={searchKeyWord}
            onChange={(e) => {
              setSearchKeyWord(e.target.value);
            }}
          />
          <button className='search-btn' type="submit">Search Button</button>
        </form>
      </div>
    </>
  );
};

export default SearchResults;
