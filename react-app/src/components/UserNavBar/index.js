import React, { useState, useRef, useEffect } from 'react';
import { NavLink, useHistory } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import SearchBar from '../searchbar'
import UserAccountNav from './accountNav';
import './UserNavBar.css'
import HomeLogo from '../../images/HomeLogo.png'


const UserNavBar = () => {

  const history = useHistory()

  const [num, setNum] = useState(0);
  const dropdown = useRef(null);
  const account = useRef(null)

  const showDropdown = () => {
    if (num === 0) {
      dropdown.current.classList.remove("hidden");
      account.current.style.textDecoration = "underline";
      account.current.style.color = "rgb(255, 80, 0)";
      setNum(1);
    } else {
      setNum(0)
    }
  }

  const RemoveOutside = (ref) => {
    useEffect(() => {
      const handleClick = (e) => {
        if (
          !e?.target?.classList?.contains("account-word") &&
          !e?.target?.nextElementSibling?.classList?.contains("hidden")

        ) {
          setNum(0);
        }
        if (ref.current && !ref.current.contains(e.target)) {
          dropdown.current.classList.add("hidden");
          account.current.style.textDecoration = "none";
          account.current.style.color = "white";
        }
      };
      document.addEventListener("mousedown", handleClick);
      return () => {
        document.removeEventListener("mousedown", handleClick);
      };
    }, [ref])
  }

  RemoveOutside(dropdown);

  return (
    <nav>
      <div className='outer-container'>

        <div className='usernav-container'>
          <div className='left-usernav-container'>
            <div>
              <NavLink to='/dashboard' exact={ true } className="home-logo">
                <img src={ HomeLogo } className="home-logo-alpha"></img>
              </NavLink>
            </div>
            <div className='searchbar-container'>
              <SearchBar />
            </div>
          </div>
          <div className='right-nav-container'>
            <div className='account-link' onClick={ () => history.push("/about") }>
              <p className='user-navbar-text'>About</p>
            </div>
            <NavLink to='/wallet' className="account-word wallet-link">
              <p className='user-navbar-text'>Wallet</p>
            </NavLink>
            <div className='account'>
              <div
                className='account-word'
                onClick={ () => showDropdown() }
                ref={ account }
              >
               <p className='user-navbar-text'> Account</p>
              </div>
              <div className='account-dropdown hidden' ref={ dropdown }>
                <UserAccountNav />

              </div>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default UserNavBar;
