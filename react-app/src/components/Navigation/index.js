
import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import "./nav.css"
// import { useSelector } from 'react-redux';
import SearchResults from '../SearchResults';
import { useSelector } from 'react-redux';

const Navigation = () => {

  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector(state => state.session.user);
  const session = useSelector(state => state.session);

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  console.log(user)

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu)
  }, [showMenu]);

  return (
    <div className='navbar'>
      <nav>
        <ul>
          <div className='nav-container'>
            <div className='category-links'>
              <NavLink to='/' exact={true} id="home-icon" activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                🏠
              </NavLink>
              <li>
                <NavLink to='/projects/1' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Circuits
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/2' exact={true} activeClassName='something' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Workshop
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/3' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Craft
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/4' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Cooking
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/5' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Living
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/6' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Outside
                </NavLink>
              </li>
              <li>
                <NavLink to='/projects/7' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Teachers
                </NavLink>
              </li>
            </div>
            <div className='profile-following-div'>
                {user && (
                  <button id='greeting' onClick={openMenu}> Hello {user.username}!</button>
                )}
              <button id='profile-quickmenu' onClick={openMenu}>
                {user && (
                  <img src={`data:image/jpeg;base64,${user.userPhoto}`} alt=''></img>
                )}
              </button>
              {!user && (
                <button id='greeting' onClick={openMenu} style={{marginRight : "130px"}}> Login</button>
              )}
            </div>
          </div>
          <div className="lower-nav">
            <div className='left-lower'>
              <div className='step-by-step-logo'>
                <NavLink to='/'>
                  <img src="https://www.instructables.com/assets/img/instructables-logo-v2.png" alt='' />
                  <p>step by step</p>
                </NavLink>
              </div>
              <div>
                {/* <button>Projects</button>
                <button>Contests</button> */}
              </div>
            </div>
            <div className='right-lower'>
              {session.user && (
                <div>
                  <NavLink className="lower-nav-sign-up" to="/create">PUBLISH</NavLink>
                </div>
              )}
              {!session.user && (
                <>
                  <NavLink className='lower-nav-login' to="/login">LOGIN</NavLink>
                  <NavLink className="lower-nav-sign-up" to="/sign-up">SIGN-UP</NavLink>
                </>
              )}
              <div className='search-input'>
                <SearchResults />
              </div>
            </div>
          </div>
        </ul>
      </nav>
      {showMenu && (
        <ul className='profile-options'>
          <div className='dropdown-div'>
            <NavLink to='/login' exact={true} id="something" activeClassName='another' style={{ textDecoration: 'none', color: "black" }}>
              <div className='dropdown-btns'>
                <li>
                  Login
                </li>
              </div>
            </NavLink>
            <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
              <div className='dropdown-btns'>
                <li>
                  Sign Up
                </li>
              </div>
            </NavLink>
            {/* <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
              <div className='dropdown-btns'>
                <li>
                  Users
                </li>
              </div>
            </NavLink> */}
            {user && (
              <div className='dropdown-btns'>
                <li>
                  <LogoutButton />
                </li>
              </div>
            )}
          </div>
        </ul>
      )}
    </div>
  );
};

export default Navigation;
