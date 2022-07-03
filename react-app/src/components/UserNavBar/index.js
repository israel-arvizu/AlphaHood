import React, { useState } from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import SearchBar from '../searchbar'
import './UserNavBar.css'

const UserNavBar = () => {

  return (
    <nav>
      <div className='usernav-container'>
        <div>
          <NavLink to='/dashboard' exact={true} activeClassName='active'>
            Home
          </NavLink>
        </div>
        <div className='searchbar-container'>
          <SearchBar />
        </div>
        <div>
          <NavLink to='/wallet' exact={true} activeClassName='active'>
            Wallet
          </NavLink>
        </div>
        <div>
          <NavLink to='/dashboard' exact={true} activeClassName='active'>
            Profile
          </NavLink>
        </div>
        <div>
          <LogoutButton />
        </div>
      </div>
    </nav>
  );
}

export default UserNavBar;
