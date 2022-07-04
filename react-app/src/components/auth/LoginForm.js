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
    return <div><Loading /></div>
    history.push('/dashboard');
  }

  return (
    <div className = 'login-page'>
     <div className = 'login-img'>
       <img src="https://cdn.robinhood.com/assets/generated_assets/webapp/632fcb3e7ed928b2a960f3e003d10b44.jpg"  alt="login-img"/>
     </div>

     <div className = 'form-component'>
       <form onSubmit={onLogin}>
         <div>
           <header className="">
             <div className="topleft">
               <div className="leftlogo">

               </div>
             <div className="middleleft">
               <div>
                 <h2 className="logintitle">Log in to Alphahood</h2>
               </div>
               <div>
                 <span className="loginparagraph">We'll need your name, email address, and a unique password. You'll use this login to access Alphahood next time.</span>
               </div>
               <div>

               </div>
               <div></div>
             </div>


             </div>
           </header>
           <div>
             {errors.map((error, ind) => (
               <div key={ind}>{error}</div>
             ))}
           </div>
           <div>
             <label htmlFor='email' className='email-label'>Email</label>
             <input
               className='email-input'
               name='email'
               type='text'
               // placeholder='Email'
               value={email}
               onChange={updateEmail}
             />
           </div>
           <div>
             <label htmlFor='password'className='password-label'>Password</label>
             <input
               className='password-input'
               name='password'
               type='password'
               // placeholder='Password'
               value={password}
               onChange={updatePassword}
             />
             <button type='submit' className='submit-button' >Login</button>
           </div>
         </div>
       </form>
     </div>
   </div>
   );
 };

 export default LoginForm;
