import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { signUp } from '../../store/session';
import "./signup.css"

const SignUpForm = () => {
  let history = useHistory()
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');


  const [repeatPassword, setRepeatPassword] = useState('');
  const [birthday, setBirthday] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    let newErrors = []
    if (username === "") {
      newErrors.push('Name cant be blank!')
    }
    if (username.length < 3){
      newErrors.push("Username must be at least 3 characters")
    }

    if (!email.includes("@")){
      newErrors.push('Enter a valid email')
    }

    if(email === "") {
      newErrors.push('Email is a mandatory Field')
    }

    if (password.length < 5){
      newErrors.push("Password must be greater than 5 characters")
    }
    if (password !== repeatPassword) {
      newErrors.push("Password should match")
    }

    if (!birthday){
      newErrors.push("Enter Birthday")
    }

    setErrors(newErrors)
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, birthday, password));
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

  const updateBirthday = (e) => {
    setBirthday(e.target.value)
  }

  if (user) {
    history.push('/dashboard');
  }
  return (
    <div className='signup-page-main-outline'>
      <div className='right-section-signup'>
        <div className='signup-header-container'>
          <h1 className='signup-header'>
            Create your Login
          </h1>
          <p>
            To access AlphaHood and all its features you'll need to make an account.
          </p>
          <p>You'll use this login to access AlphaHood next time.</p>
          <p id='sign-up-warning-msg'>Please note this is a not a real trading website!</p>
        </div>
        <img src="https://cdn.robinhood.com/app_assets/odyssey/rockets.png" id="signup-rocket" alt="rockets"/>
      </div>
      <div className='left-section-signup'>
        <form className='signup-form' onSubmit={onSignUp}>
          <p className='signup-instructions'>
            Welcome! Please fill out your information below,
          </p>
          <div className='inputs-container'>
            <div className='errors-content-container'>
              {errors.map((error, ind) => (
                <p key={ind}>{error}</p>
              ))}
            </div>
              <input
                type='text'
                className='username'
                onChange={updateUsername}
                value={username}
                placeholder="User Name"
              ></input>
              <input
                type='text'
                className='email'
                onChange={updateEmail}
                value={email}
                placeholder="Email"
              ></input>
              <div>
                <label className='birthday-label'>Birthday</label>
              </div>
              <input
              type='date'
              className='birthday'
              onChange={updateBirthday}
              value={birthday}
              ></input>
              <input
                type='password'
                className='password'
                onChange={updatePassword}
                value={password}
                placeholder="Password"
              ></input>
              <input
                type='password'
                className='repeat_password'
                onChange={updateRepeatPassword}
                value={repeatPassword}
                required={true}
                placeholder="Repeat Password"
              ></input>
            <button className='signupsubmit-button' type='submit' disabled={!!errors.length}>Sign Up</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default SignUpForm;
