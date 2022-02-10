import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { authenticate } from './store/session';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import Navigation from './components/Navigation';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';
import ProjectExplore from './components/ProjectExplore';
import ProjectDetails from './components/ProjectDetails'
import CreateProject from './components/CreateProject'
import SearchResults from './components/SearchResults';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Navigation />
      <Switch>
        <Route path='/login' exact={true}>
          <LoginForm />
        </Route>
         <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>

        <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>

        <ProtectedRoute path='/' exact={true} >
          <ProjectExplore/>
        </ProtectedRoute>

        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>

        <Route path='/projects/:projectId' exact={true} >
          <ProjectDetails/>
        </Route>

        <ProtectedRoute path='/howto/:searchkeyword' exact={true} >
          <SearchResults/>
        </ProtectedRoute>

        <ProtectedRoute path='/create' exact={true} >
          <CreateProject/>
        </ProtectedRoute>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
