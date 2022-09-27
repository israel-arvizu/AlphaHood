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
        <div className="splash-container">
          <header className="splash-header">
            <div className="splash-nav-bar-container">
              <img id="splashLogo" src={logo} alt='Alpha Hood Logo' />
              <nav className="splash-header-container">
                <div className="splash-nav-buttons">
                    <a href='/about' className='about-us'>
                      About Us
                    </a>
                  {!user &&
                    <button className="demo-btn" onClick={getdemo}>
                      Demo
                    </button>
                  }
                  {!user &&
                    <a href='/login' className='login'>
                      Log in
                    </a>
                  }
                  {!user &&
                    <a href='/sign-up' className='sign-up'>
                      Sign up
                    </a>
                  }
                  {user &&
                    <a href='/dashboard' className='home-button-splash'>
                      Home
                    </a>
                  }
                </div>
              </nav>
            </div>
            </header>
            <div className="firstsection">
              <div className="div-section-first">
                <img className="phones-image-splash" src={robinhood}></img>
              </div>
              <div className="div-section-first right">
                  <div className="div-section-first-inner">Investing is simple here</div>
                  <a href="/sign-up" className="splash-button main-one-content"> Get Started </a>
              </div>
            </div>
        </div>
    </>
  )



}


export default SplashPage
