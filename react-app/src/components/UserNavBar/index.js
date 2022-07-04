import React, { useState, useRef, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import SearchBar from '../searchbar'
import UserAccountNav from './accountNav';
import './UserNavBar.css'

const UserNavBar = () => {

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

  RemoveOutside(dropdown)
  return (
    <nav>
      <div className='outer-container'>

        <div className='usernav-container'>
          <div>
            <NavLink to='/dashboard' exact={ true } activeClassName='active'>
              Home
            </NavLink>
          </div>
          <div className='searchbar-container'>
            <SearchBar />
          </div>
          <div className='right-nav-container'>
            <div>
              <NavLink to='/wallet' exact={ true } activeClassName='active'>
                Wallet
              </NavLink>
            </div>
            <div className='account-word' onClick={ () => showDropdown() } ref={ account }>
              Account
            </div>
            <div className='account-dropdown hidden' ref={ dropdown }>
              <UserAccountNav />
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default UserNavBar;
