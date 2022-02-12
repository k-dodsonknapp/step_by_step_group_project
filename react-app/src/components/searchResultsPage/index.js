// import "./SearchResults.css";
import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { search } from "../../store/project";
import { useDispatch } from "react-redux";
import './SearchResultsPage.css'
import SearchResults from "../SearchResults";

const SearchRes = () => {
  const [searchKeyWord, setSearchKeyWord] = useState("");
  const dispatch = useDispatch();
  const history = useHistory();
  const projects = useSelector((state) => Object.values(state.projects));

  console.log(projects);

  return (
    <div id='search-page'>
      <SearchResults />
      { projects &&
        <ul id='search-results-container'>
          {projects.map(project => (
            <a className='search-link'href={`/projects/${project.id}`}>
              <li key={project.id}className="searh-list-component">
                <img className="search-img" src={`${project.titleImage}`}></img>
                <div className="search-text">
                  <div className="search-title">{project.title}</div>
                  <p className="search-overview">{project.overview}</p>
                </div>
              </li>
            </a>
          ))}
        </ul>
      }
    </div>
  );
};

export default SearchRes;
