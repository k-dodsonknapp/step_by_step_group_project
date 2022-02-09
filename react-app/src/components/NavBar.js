import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import LogoutButton from "./auth/LogoutButton";
import { searchResults } from "../store/project";
import { useDispatch } from "react-redux";

const NavBar = ({ loaded }) => {
  // const sessionUser = useSelector((state) => state.session?.user);

  const [searchKeyWord, setSearchKeyWord] = useState("");
  const [projects, setProjects] = useState();
  const dispatch = useDispatch();

  // useEffect(() => {
  //   if (searchKeyWord) {
  //     async function fetchData() {
  //       const response = await fetch(`/api/search/${searchKeyWord}`);
  //       const responseData = await response.json();
  //       setProjects(responseData.projects);
  //     }
  //     fetchData();
  //   }
  // }, [searchKeyWord]);

  const clickToSearch = (e) => {
    e.preventdefault();
    // console.log('e.target.value', e.target.value)
    // const response = await fetch(`/api/search/${searchKeyWord}`);
    // const responseData = await response.json();
    // setProjects(responseData.projects);
    console.log("inside click to search");
    dispatch(searchResults(searchKeyWord));
  };
  // click on cancel search button to clear search results
  // const clearClickToSearch = async (e) => {
  //   setSearchKeyWord("");
  // };
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
      {/* {searchKeyWord ? (
        <div>
          <h1> Search results for: </h1>
          <h2>{searchKeyWord}</h2> */}
      {/* <button onClick={clearClickToSearch}>Clear results</button>
          <ul>{searchBlock}</ul> */}
      {/* </div>
      ) : null} */}
      {/* <ul>
        <li>
          <NavLink to="/" exact={true} activeClassName="active">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/login" exact={true} activeClassName="active">
            Login
          </NavLink>
        </li>
        <li>
          <NavLink to="/sign-up" exact={true} activeClassName="active">
            Sign Up
          </NavLink>
        </li>
        <li>
          <NavLink to="/users" exact={true} activeClassName="active">
            Users
          </NavLink>
        </li>
        <li>
          <LogoutButton />
        </li>
      </ul> */}
    </nav>
  );
};

export default NavBar;
