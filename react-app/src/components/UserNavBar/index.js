import React, {useState} from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';

const UserNavBar = () => {

  return (
    <nav>
      <div>
        <div>
          <NavLink to='/dashboard' exact={true} activeClassName='active'>
            Home
          </NavLink>
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
