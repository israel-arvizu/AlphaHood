import {useState, useEffect} from "react"
import NavBar from "../NavBar"
import './splashpage.css'


function SplashPage(){

    return (
        <>
        <header className="splash-header">
          <div class="splash-container">
            <div class="logo">
              <img id="splashLogo" src='./logo.png' alt='a' />
            </div>
            <nav>
              <ul>
                <li>
                  <a href='/about' exact={true} className='about-us'>
                    About Us
                  </a>
                </li>
                  <button className="demo" type="submit">
                    Demo
                  </button>
                <li>
                <a href='/login' exact={true} className='login'>
                    Login
                    </a>
                </li>
                <li>
                <a href='/sign-up' exact={true} className='sign-up'>
                    Sign Up
                  </a>
                </li>
              </ul>
            </nav>
          </div>
        </header>
      </>
      )



}


export default SplashPage
