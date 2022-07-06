import { useState, useEffect, } from "react"
import { useSelector, useDispatch } from 'react-redux'
import { loadAllLists } from "../../store/list"
import { loadPortfolio } from "../../store/stocks"
import NavBar from "../NavBar"
import { Redirect, useHistory } from "react-router-dom"
import { demo_user_login } from "../../store/session.js"
import logo from './logo.png'
import './splashpage.css'
import robinhood from './robinhood.png'


function SplashPage() {
  const history = useHistory()
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)

  useEffect(() => {
    if (user) {
      dispatch(loadAllLists(user.id))
    }
  }, [])


  const getdemo = () => {
    dispatch(demo_user_login())
    history.push('/dashboard')
  }




  return (
    <>
      <header className="splash-header">
        <div className="splash-container">
          <div className="splash-nav-bar-container">
            <div className="logo">
              <img id="splashLogo" src={logo} alt='a' />
            </div>
            <nav className="splashbuttons">
              <div className="splash-nav-buttons">
                <div>
                  <a href='/about' className='about-us'>
                    About Us
                  </a>
                </div>
                <button className="demo-btn" onClick={getdemo}>
                  Demo
                </button>
                {!user &&
                  <div>
                    <a href='/login' className='login'>
                      Login
                    </a>
                  </div>
                }
                {!user &&
                  <div>
                    <a href='/sign-up' className='sign-up'>
                      Sign Up
                    </a>
                  </div>
                }
                {user &&
                  <div>
                    <a href='/dashboard' className='home-button-splash'>
                      Home
                    </a>
                  </div>
                }
              </div>
            </nav>
            </div>
          <div className="firstsection">
            <div className="divhalf">
              <img className="phones" src={robinhood}></img>

            </div>
            <div className="divhalf2">
              <div className="innerhalf">Investing is simple here</div>

            </div>
          </div>
        </div>
      </header>
    </>
  )



}


export default SplashPage
