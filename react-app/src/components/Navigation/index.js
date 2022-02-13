
import React, { useEffect, useState } from 'react';
import { NavLink, useParams } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import "./nav.css"
import { useSelector } from 'react-redux';
import SearchResults from '../SearchResults';
import ProfileButton from './ProfileButton';
const Navigation = ({loaded}) => {

  const [showMenu, setShowMenu] = useState(false)
  const sessionUser = useSelector(state => state.session.user);

  let sessionLinks;
  if (sessionUser) {
    sessionLinks = (
    <>
      <div className='navbar'>
      <nav>
        <ul>
          <div className='nav-container'>
            <div className='category-links'> 
              <NavLink to='/' exact={true} id="home-icon" activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                🏠
              </NavLink>
              <li>
                <NavLink to='/Circuits' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Circuits
                </NavLink>
              </li>
              <li>
                <NavLink to='/Workshop' exact={true} activeClassName='something' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Workshop
                </NavLink>
              </li>
              <li>
                <NavLink to='/Craft' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Craft
                </NavLink>
              </li>
              <li>
                <NavLink to='/Cooking' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Cooking
                </NavLink>
              </li>
              <li>
                <NavLink to='/Living' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Living
                </NavLink>
              </li>
              <li>
                <NavLink to='/Outside' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Outside
                </NavLink>
              </li>
              <li>
                <NavLink to='/Teachers' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Teachers
                </NavLink>
              </li>
              <ProfileButton user={sessionUser} />
            </div>
          </div>
          </ul>
          </nav>
          </div>
          <nav>
          <div className="lower-nav">
            <div className='left-lower'>
              <div className='step-by-step-logo'>
                <NavLink to='/'>
                  <img src="https:www.instructables.com/assets/img/instructables-logo-v2.png" />
                  <p>step by step</p>
                </NavLink>
              </div>
              <div>
                <button>Projects</button>
                <button>Contests</button>
              </div>
            </div>
            <div className='right-lower'>
              <div>
                <NavLink to="/create">PUBLISH</NavLink>
              </div>
              <div>
                <SearchResults />
              </div>
            </div>
          </div>


       </nav>
      </>
    );
  } else {
    sessionLinks = (
    <>
      <div className='navbar'>
      <nav>
        <ul>
          <div className='nav-container'>
            <div className='category-links'> 
              <NavLink to='/' exact={true} id="home-icon" activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                🏠
              </NavLink>
              <li>
                <NavLink to='/login' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Login
                </NavLink>
              </li>
              <li>
                <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
                  Sign Up
                </NavLink>
              </li>
              </div>
          </div>
          </ul>
          </nav>
          </div>
          <nav>
          <div className="lower-nav">
            <div className='left-lower'>
              <div className='step-by-step-logo'>
                <NavLink to='/'>
                  <img src="https:www.instructables.com/assets/img/instructables-logo-v2.png" />
                  <p>step by step</p>
                </NavLink>
              </div>
            </div>
            <div className='right-lower'>
            </div>
          </div>


       </nav>
      </>
    );
  }
 
  

  return (
    <>
      {loaded && sessionLinks}
        {/* <nav>
           <div className="lower-nav">
             <div className='left-lower'>
               <div className='step-by-step-logo'>
                 <NavLink to='/'>
                   <img src="https:www.instructables.com/assets/img/instructables-logo-v2.png" />
                   <p>step by step</p>
                 </NavLink>
               </div>
               <div>
                 <button>Projects</button>
                 <button>Contests</button>
               </div>
             </div>
             <div className='right-lower'>
               <div>
                 <NavLink to="/create">PUBLISH</NavLink>
               </div>
               <div>
                 <SearchResults />
               </div>
             </div>
           </div>
 

        </nav> */}
    </>
    // <div className='navbar'>
    //   <nav>
    //     <ul>
    //       <div className='nav-container'>
    //         <div className='category-links'>
    //           {loaded && sessionLinks}
              
    //           <NavLink to='/' exact={true} id="home-icon" activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //     
    //           </NavLink>
    //           <li>
    //             <NavLink to='/Circuits' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //               Circuits
    //             </NavLink>
    //           </li>
    //           <li>
    //             <NavLink to='/Workshop' exact={true} activeClassName='something' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //               Workshop
    //             </NavLink>
    //           </li>
    //           <li>
    //             <NavLink to='/Craft' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //               Craft
    //             </NavLink>
    //           </li>
    //           <li>
    //             <NavLink to='/Cooking' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //               Cooking
    //             </NavLink>
    //           </li>
    //           <li>
    //             <NavLink to='/Living' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //               Living
    //             </NavLink>
    //           </li>
    //           <li>
    //             <NavLink to='/Outside' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //               Outside
    //             </NavLink>
    //           </li>
    //           <li>
    //             <NavLink to='/Teachers' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "#CCCCCC" }}>
    //               Teachers
    //             </NavLink>
    //           </li>
    //         </div>
    //       </div>
          
//           <nav>
//           <div className="lower-nav">
//             <div className='left-lower'>
//               <div className='step-by-step-logo'>
//                 <NavLink to='/'>
//                   <img src="https://www.instructables.com/assets/img/instructables-logo-v2.png" />
//                   <p>step by step</p>
//                 </NavLink>
//               </div>
//               <div>
//                 <button>Projects</button>
//                 <button>Contests</button>
//               </div>
//             </div>
//             <div className='right-lower'>
//               <div>
//                 <NavLink to="/create">PUBLISH</NavLink>
//               </div>
//               <div>
//                 <SearchResults />
//               </div>
//             </div>
//           </div>
//         </ul>
//       </nav>
//         <ul className='profile-options'>
//           <div className='dropdown-div'>
//             <li>
//               <NavLink to='/login' exact={true} id="something" activeClassName='another' style={{ textDecoration: 'none', color: "black" }}>
//                 Login
//               </NavLink>
//             </li>
//             <li>
//               <NavLink to='/sign-up' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
//                 Sign Up
//               </NavLink>
//             </li>
//             <li>
//               <NavLink to='/users' exact={true} activeClassName='active' style={{ textDecoration: 'none', color: "black" }}>
//                 Users
//               </NavLink>
//             </li>
//             <div className='nav-links'>
//               <li>
//                 <LogoutButton />
//               </li>
//             </div>
//           </div>
//         </ul>
//     </div>
  );
}

export default Navigation;
