import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
import UploadPicture from '../UploadPicture';
import './auth.css'
import DemoButton from './DemoUser';
const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const [userPhoto, setUserPhoto] = useState('')
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(
        signUp(
          username,
          email,
          password,
          userPhoto,
        ));
      if (data) {
        setErrors(data)
      }
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }


  /**
   * 
  display: flex;
  height: 68vh;
  background-color: rgba(15, 15, 15, 0.199);
  backdrop-filter: blur(5px);
  width: 501px;
  justify-content: center;



margin-top: 89px;

   */

  return (
    <div className="loginPage">
      <div className="loginformContainer" style={{ paddingTop: '5%' }}>
        <form onSubmit={onSignUp}>
          <div>
            {errors.map((error, ind) => (
              <div key={ind}>{error}</div>
            ))}
          </div>
          <div className='newUser-input'>
            <label>Username</label>
            <input
              placeholder='What do we call you?'
              type='text'
              name='username'
              className="signupInput"
              onChange={updateUsername}
              value={username}
            ></input>
          </div>
          <div className='newUser-input'>
            <label>Email</label>
            <input
              placeholder='Where can we reach you?'
              type='text'
              name='email'
              className="signupInput"
              onChange={updateEmail}
              value={email}
            ></input>
          </div>
          <div className='newUser-input'>
            <label>Password</label>
            <input
            placeholder='How will we know it is you?'
              type='password'
              name='password'
              className="signupInput"
              onChange={updatePassword}
              value={password}
            ></input>
          </div>
          <div className='newUser-input'>
            <label>Repeat Password</label>
            <input
            placeholder='Again, how will we know it is you?'
            type='password'
              name='repeat_password'
              className="signupInput"
              onChange={updateRepeatPassword}
              value={repeatPassword}
              required={true}
            ></input>
          </div>
          <div className='newUser-input'>
            <label>User Photo</label>
            <UploadPicture className={"addPhoto"} setTitleImagee={setUserPhoto} />
          </div>
          <div className='signupBtns'>
            <button className='loginButton' type='submit'>Sign Up</button>
            <DemoButton className={"new-user-demo"} />
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignUpForm;
