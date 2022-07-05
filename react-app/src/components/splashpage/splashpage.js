import { useState, useEffect, } from "react"
import { useSelector, useDispatch } from 'react-redux'
import { loadAllLists } from "../../store/list"
import { loadPortfolio } from "../../store/stocks"
import NavBar from "../NavBar"
import logo from './logo.png'
import './splashpage.css'
import robinhood from './robinhood.png'


function SplashPage() {
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)

  useEffect(()=>{
    if(user){
    dispatch(loadAllLists(user.id))
    }
  }, [])





  return (
    <>
      <header className="splash-header">
        <div className="splash-container">
          <div className="logo">
            <img id="splashLogo" src={logo} alt='a' />
          </div>
          <nav className="splashbuttons">
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
                {!user && <a href='/sign-up' exact={true} className='sign-up'>
                  Sign Up
                </a>
                }
                {user && <a href='/dashboard' exact={true} className='sign-up'>
                  Home
                </a>}
              </li>
            </ul>
          </nav>
          <div className="firstsection">
            <div className="divhalf">
              <img src={robinhood}></img>

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
