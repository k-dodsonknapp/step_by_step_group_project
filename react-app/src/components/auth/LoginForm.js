import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
import DemoButton from './DemoUser';
import './auth.css'
const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    };
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  };

  return (
    <div className="loginPage">
      <div className="loginformContainer">
        <form onSubmit={onLogin}>
          <div>
            {errors.map((error, ind) => (
              <div key={ind}>{error}</div>
            ))}
          </div>
          <div>
            <label htmlFor='email'>Email</label>
            <input
              name='email'
              type='text'
              className="loginInput"
              placeholder='Email'
              value={email}
              onChange={updateEmail}
            />
          </div>
          <div>
            <label htmlFor='password'>Password</label>
            <input
              name='password'
              type='password'
              className="loginInput"
              placeholder='Password'
              value={password}
              onChange={updatePassword}
            />
            <div className='signupBtns'>
              <button className="loginButton" type='submit'>Login</button>
              <DemoButton />
            </div>
          </div>
        </form>
      </div>
    </div>

  );
};

export default LoginForm;
