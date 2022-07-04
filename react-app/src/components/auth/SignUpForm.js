import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, useHistory } from 'react-router-dom';
import { signUp } from '../../store/session';

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
    <div className='signup-page'>
        <div className="leftimagediv">
                    <img class="leftimage" src="https://cdn.robinhood.com/app_assets/odyssey/rockets.png" height="420"></img>
        <div>



        <div className="form-component-signup"></div>
            <div className="leftSideForm">

              <div className="topleft">
                <div className="leftlogo">

                </div>
                <div className="middleleft">
                  <div>
                    <h2 className="logintitle">Create your login</h2>
                  </div>
                  <div>
                    <span className="loginparagraph">We'll need your name, email address, and a unique password. You'll use this login to access Alphahood next time.</span>
                  </div>
                  <div className="leftimagediv">
                    <img class="leftimage" src="https://cdn.robinhood.com/app_assets/odyssey/rockets.png" height="420">

                    </img>
                  </div>
                  <div></div>
                </div>
              </div>
            </div>
            <div className="rightsideForm">
              {errors.map((error, ind) => (
                <div key={ind}>{error}</div>
              ))}

            <form onSubmit={onSignUp}>
            <div>

              <label>User Name</label>
              <input
                type='text'
                name='username'
                onChange={updateUsername}
                value={username}
              ></input>
            </div>
            <div>
              <label>Email</label>
              <input
                type='text'
                name='email'
                onChange={updateEmail}
                value={email}
              ></input>
            </div>
            <div>
              <label>Birthday</label>
              <input
                type='date'
                name='birthday'
                onChange={updateBirthday}
                value={birthday}
              ></input>
            </div>
            <div>
              <label>Password</label>
              <input
                type='password'
                name='password'
                onChange={updatePassword}
                value={password}
              ></input>
            </div>
            <div>
              <label>Repeat Password</label>
              <input
                type='password'
                name='repeat_password'
                onChange={updateRepeatPassword}
                value={repeatPassword}
                required={true}
              ></input>
            </div>
            <button type='submit'>Sign Up</button>
            </form>
            </div>
            </div>
    </div >
  </div >
  );

};

export default SignUpForm;
