import React, { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
import LogoutButton from "./auth/LogoutButton";

const NavBar = ({ loaded }) => {
  const sessionUser = useSelector((state) => state.session?.user);

  const [searchBar, setSearchBar] = useState("");
  const [projects, setProjects] = useState();

  useEffect(() => {
    if (searchBar) {
      async function fetchData() {
        const response = await fetch(`/api/search/${searchBar}`);
        const responseData = await response.json();
        setProjects(responseData.projects);
      }
      fetchData();
    }
  }, [searchBar]);

  const clickToSearch = async (e) => {
    // e.preventdefault()
    // console.log('e.target.value', e.target.value)
    setSearchBar(e.target.value);
    const response = await fetch(`/api/search/${e.target.value}`);
    const responseData = await response.json();
    setProjects(responseData.projects);
  };
  // click on cancel search button to clear search results
  const clearClickToSearch = async (e) => {
    setSearchBar("");
  };
  let searchBlock;

  if (projects) {
    //console.log(projects)
    searchBlock = projects.map((project, i) => {
      return (
        <a
          key={`link${i}`}
          href={`/projects/${project.id}`}
        >
          <div key={`liked'_${project.id}`}>
            <img
              alt={project.name}
              src={
                project.medias && project.medias[0]
                  ? project.medias[0]["mediaUrl"]
                  : "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAARMAAAC3CAMAAAAGjUrGAAAAKlBMVEXg4OD////j4+Pd3d36+vri4uLw8PDs7Oz29vb09PTa2tr5+fnm5ubx8fF4aKZkAAABUUlEQVR4nO3Z246CMBRAUWjBgQ78/+8OeMVR4E0TzlovJpUY3DnBglUFAAAAAAAAAAAAAAAAAAAAAAAAAMAh5DZtq/K3T/HTclfv6YNFyf1ukro+ffssPyvX9bg9BtMg/cYalKnJz06TU93EazK/tENa+eJRm+Rxump0K0cEbXI6X0q7t189aJN8/X1p3x4Ru8nwWO7uQxO0Sbk2eax2j51a0CbVcNma3UejW2xfozbJqZley22tW+7pozapcinleUruUcI2Wa4sbgrnKLGbpPPC033yFCV0k2ben/x/dNDnwE1yM2/aXp+mlMBN5iR18/qAKW6T85S8FbfJapKwTdanJHCT9SSaaDLT5NWlSWrXpMh7tpW3g97v9CkN61LqwjUZN64lNzv/AB1O2f+/eCz7H3MspeRtJVwSAAAAAAAAAAAAAAAAAAAAAAAAAICj+gOmbQmv8zyqjAAAAABJRU5ErkJggg=="
              }
            />
            <h4>{project.title.slice(0, 25) + "..."}</h4>
            <p className="authorName">
              by: {project.author.username} in{" "}
              {project.supply ? project.supply[0].name : "All Projects"}
            </p>
          </div>
        </a>
      );
    });
  }

  return (
    <nav>
      <button onClick={clickToSearch}>Search</button>
      <div>
        <form title="Search Form">
          <input
            type="text"
            placeholder="Let's Make..."
            onChange={(e) => setSearchBar(e.target.value)}
          />
        </form>
      </div>
      {searchBar ? (
        <div>
          <h1> Search results for: </h1>
          <h2>{searchBar}</h2>
          <button onClick={clearClickToSearch}>Clear results</button>
          <ul>{searchBlock}</ul>
        </div>
      ) : null}
      <ul>
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
      </ul>
    </nav>
  );
};

export default NavBar;
