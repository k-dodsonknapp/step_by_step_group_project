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

  console.log(document.cookie);

  const onSignUp = async (e) => {
    e.preventDefault();
    console.log(userPhoto, 'something')
    const formData = new FormData();
    console.log(formData, 'thiiiiss')
    console.log(username, email, password, userPhoto)
    formData.append('username', username);
    formData.append('email', email);
    formData.append('password', password)
    formData.append('userPhoto', userPhoto)
    for (let [key, value] of formData.entries()) {
      console.log(`${key}:`, value); // This should log all key-value pairs, including the file
    }
    console.log(formData)
    if (password === repeatPassword) {
      const data = await dispatch(
        signUp(formData)
      )
      if (data) {
        setErrors(data)
      }
    }
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
      <div className="loginformContainer">
        <form onSubmit={onSignUp}>
          <div className='newUser-input'>
            <label>User Photo</label>
            <UploadPicture uploadType={"addProfilePhoto"} setPhoto={setUserPhoto} />
          </div>
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
              onChange={(e) => setUsername(e.target.value)}
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
              onChange={(e) => setEmail(e.target.value)}
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
              onChange={(e) => setPassword(e.target.value)}
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
              onChange={(e) => setRepeatPassword(e.target.value)}
              value={repeatPassword}
              required={true}
            ></input>
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
