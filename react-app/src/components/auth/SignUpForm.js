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


  useEffect(()=>{
      let newErrors = []
      if (username === "") {
        newErrors.push('Name cant be blank!')
      }

      if (username < 3){
        newErrors.push("username must be at least 3 characters")
      }

      if (!email.includes("@")){
        newErrors.push('Enter a valid email')
      }

      if(email === "") {
        newErrors.push('Email is a mandatory Field')
      }

      if (password.length < 5){
        newErrors.push("password must be greater than 5 characters")
      }
      if (password !== repeatPassword) {
        newErrors.push("Password should match")
      }

      if (!birthday){
        newErrors.push("Enter Birthday")
      }

      setErrors(newErrors)


  }, [username,email, password, repeatPassword] )

  const onSignUp = async (e) => {
    e.preventDefault();
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
    history.push('/');
  }
  return (
    <div className = 'signup-page'>
      <div className = 'background-color'/>
        <h1 className= 'signup-header'>
          Create your Login
        </h1>
        <p className= 'signup-desc'>
      We'll need your name, email address, and a unique password. You'll use this login to access Robinhood next time.
      </p>
        <div className = 'signup-img'>
            <img src="https://cdn.robinhood.com/app_assets/odyssey/rockets.png" id="signuprocket" alt="rockets"/>
        </div>
    <form className = 'signup-form'
    onSubmit={onSignUp}>
      <div className = 'signup-instructions'>
        Enter your first and last name as they appear on your government ID.
      </div>
      <div className = 'inputs'>
      <div>
        {errors.map((error, ind) => (
          <div key={ind}>{error}</div>
        ))}
      </div>
      <div>
        <input
          type='text'
          className='username'
          onChange={updateUsername}
          value={username}
          placeholder="User Name"
        ></input>
      </div>
      <div>
        <input
          type='text'
          className='email'
          onChange={updateEmail}
          value={email}
          placeholder="Email"
        ></input>
      </div>
      <div>
        <label className='birthday-label'>Birthday</label>
        <input
        type='date'
        className='birthday'
        onChange={updateBirthday}
        value={birthday}
        ></input>
      </div>
<div>
        <input
          type='password'
          className='password'
          onChange={updatePassword}
          value={password}
          placeholder="Password"
        ></input>
      </div>
      <div>
        <input
          type='password'
          className='repeat_password'
          onChange={updateRepeatPassword}
          value={repeatPassword}
          required={true}
          placeholder="Repeat Password"
        ></input>
      </div>
      <button className= 'signupsubmit-button' type='submit'>Sign Up</button>
      </div>
    </form>
    </div>
  );
};

export default SignUpForm;
