
import React from "react";
import { useSelector } from "react-redux";
import './SearchResultsPage.css'
import SearchResults from "../SearchResults";

const SearchRes = () => {

  const projects = useSelector((state) => Object.values(state.projects));

  return (
    <div id='search-page'>
      <SearchResults />
      { projects &&
        <ul id='search-results-container'>
          {projects.map(project => (
            <a className='search-link'href={`/projects/${project.id}`}>
              <li key={project.id}className="searh-list-component">
                <img className="search-img" src={`${project.titleImage}`} alt=''></img>
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
