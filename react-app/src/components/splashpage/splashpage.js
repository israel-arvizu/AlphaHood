import {useState, useEffect} from "react"
import NavBar from "../NavBar"
import './splashpage.css'


function SplashPage(){

    return(
        <div>
            <NavBar />
            <div>
                <div>
                    <div className="navbar">
                        <nav>
                            <div>

                            </div>
                            <div>
                                <ul>
                                    <li>
                                        <div>
                                            <a><span>GitHub</span></a>
                                        </div>
                                    </li>


                                </ul>
                            </div>
                            <div>
                            </div>
                        </nav>


                    </div>
                    <div className="firsts">
                        <div className="firsts-leftsidewhole">
                            <div className="leftsideinsidebox">

                            </div>

                        </div>
                        <div className = "firsts-rightsidewhole">
                            <div className="firsts-rightsideinsidebox">
                                <div className = "titlebox">
                                    <div className ="title">Investing is simple here</div>
                                    <div className = "getstartedbuttoncontainer">
                                        <a href="/sign-up" type="anchor" >
                                            <span className="getstartedbutton">
                                                <span className="getstartedtext">Get Started</span>

                                            </span>

                                        </a>


                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>
                    <div>

                    </div>
                    <div>

                    </div>
                    <footer>

                    </footer>
                </div>

            </div>
        </div>
    )



}


export default SplashPage
