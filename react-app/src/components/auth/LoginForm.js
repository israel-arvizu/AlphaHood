import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';
import { login } from '../../store/session';
import { loadAllLists } from '../../store/list';
import Loading from '../loading';
import './loginform.css'

const LoginForm = () => {
  let history = useHistory()
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
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    loadAllLists(user.id)
    // return <div><Loading /></div>
    history.push('/dashboard');
  }

  return (
    <div className='login-page'>
      <div className='login-img-cont'>
        <img src="https://cdn.robinhood.com/assets/generated_assets/webapp/632fcb3e7ed928b2a960f3e003d10b44.jpg"  alt="Login Default Image" />
      </div>
      <div className='login-right-outline'>
          <form onSubmit={ onLogin }>
              <h2>Log in to Alphahood</h2>
              <div className={errors.length > 0 ?'login-error-container' : 'login-error-hidden'}>
                {errors.map((error, ind) => (
                  <div key={ind}>{error}</div>
                ))}
              </div>
              <div>
                <label htmlFor='email'>Email</label>
                <input
                  name='email'
                  type='text'
                  value={ email }
                  onChange={ updateEmail }
                />
              </div>
              <div>
                <label htmlFor='password'>Password</label>
                <input
                  name='password'
                  type='password'
                  value={password}
                  onChange={updatePassword}
                />
              </div>
              <button type='submit' className='submit-button'>Log in</button>
              <br></br>
              <div className='right-footer'>
                <p>Not on Alphahood?</p>
                <a href="/sign-up">Create an account</a>
              </div>
          </form>
      </div>
    </div>
  );
};

export default LoginForm;
