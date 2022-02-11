// import "./SearchResults.css";
import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink, useHistory } from "react-router-dom";
import { search } from "../../store/project";
import { useDispatch } from "react-redux";
// import SearchResults from "./searchResults/index.js";

const SearchRes = () => {
  const [searchKeyWord, setSearchKeyWord] = useState("");
  const dispatch = useDispatch();
  const history = useHistory();
  const projects = useSelector((state) => Object.values(state.projects));

  console.log(projects);

  //   const clickToSearch = (e) => {
  //     e.preventDefault();
  //     console.log("inside click to search");
  //     dispatch(search(searchKeyWord));
  //     history.push(`/howto/${searchKeyWord}`);
  //   };

  //   let searchBlock;

  //   if (projects) {
  //     //console.log(projects)
  //     searchBlock = projects.map((project, i) => {
  //       return (
  //         <a key={`link${i}`} href={`/projects/${project.id}`}>
  //           <div key={`liked'_${project.id}`}></div>
  //         </a>
  //       );
  //     });
  //   }

  return (
    //   <div>
    //     <form title="Search Form" onSubmit={clickToSearch}>
    //       <input
    //         type="text"
    //         placeholder="Let's Make..."
    //         onChange={(e) => {
    //           setSearchKeyWord(e.target.value);
    //         }}
    //       />
    //       <button type="submit">Search Button</button>
    //     </form>
    //   </div>
    //   {searchKeyWord ? (
    //     <div>
    //        {/* <h1> Search results for: </h1>  */}
    //        {/* <h2>{searchKeyWord}</h2>  */}
    //       <ul>{searchBlock}</ul>
    //     </div>
    //   ) : null}
    <>
      <h1>Hello from Search Results page</h1>
      {projects && 
      <> 
      {projects.map(project => (
          <div>{project.title}</div>
      ))}
      </>}
    </>
  );
};

export default SearchRes;
