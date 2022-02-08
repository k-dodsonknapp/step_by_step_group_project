import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';

const DemoButton = () => {
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch()
  const handleDemo = async (e) => {
    e.preventDefault();
    const email = 'demo@aa.io'
    const password = 'password'
    await dispatch(login(email, password));

  };

  if (user) {
    return <Redirect to='/' />;
  }

  return <button onClick={handleDemo}>Demo User</button>;
}


export default DemoButton;