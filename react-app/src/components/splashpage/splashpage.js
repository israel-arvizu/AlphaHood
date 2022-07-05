import { useState, useEffect, } from "react"
import { useSelector, useDispatch } from 'react-redux'
import { loadAllLists } from "../../store/list"
import { loadPortfolio } from "../../store/stocks"
import NavBar from "../NavBar"
import {useHistory} from "react-router-dom"
import {demo_user_login} from "../../store/session.js"
import logo from './logo.png'
import './splashpage.css'
import robinhood from './robinhood.png'


function SplashPage() {
  const history = useHistory()
  const dispatch = useDispatch()
  const user = useSelector(state => state.session.user)

  useEffect(()=>{
    if(user){
    dispatch(loadAllLists(user.id))
    }
  }, [])


  const getdemo = () =>{
    dispatch(demo_user_login())
    history.push('/')
  }




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
              <button className="demo" onClick={getdemo}>
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
