import { useState } from "react";
import { useSelector } from "react-redux";
import { Link, NavLink } from "react-router-dom";

import LinkedInLogo from '../../images/LI-Logo.png'
import GitHubLogo from '../../images/GitHub_Logo_White.png'
import UserNavBar from '../UserNavBar/index'
import "./About.css";


const About = () => {
    const [person, setPerson] = useState();
    const user = useSelector((state) => state.session?.user)


    const [bio, setBio] = useState();
    const [favStock, setFaveStock] = useState();
    const [linkedIn, setLinkedIn] = useState();
    const [gitHub, setGitHub] = useState();


    const fino = () => {
        setPerson("Augustino Elisaia");
        setBio(['Software Engineer', 'Athletics' , 'Food Enthusiast']);
        setFaveStock("Nike Inc, NKE");
        setLinkedIn("https://www.linkedin.com/in/augustino-elisaia-7307a822b/");
        setGitHub("https://github.com/elisaia55")
    }

    const dylan = () => {
        setPerson("Dylan Peate");
        setBio(["Software Engineer", "Photographer", "Money Maker"]);
        setFaveStock("Mclaren, MLAI");
        setLinkedIn("https://www.linkedin.com/in/dylan-peate-839511231/");
        setGitHub("https://github.com/dylanpeate")
    }

    const izzy = () => {
        setPerson("Israel Arvizu");
        setBio(['Computer Enthusiast', 'Technology Lover', 'City Life', 'Friends']);
        setFaveStock("Tesla INC, TSLA");
        setLinkedIn("https://www.linkedin.com/in/israel-arvizu-a11b87218/");
        setGitHub("https://github.com/israel-arvizu")
    }

    const brian = () => {
        setPerson("Brian Kim");
        setBio(['Cybersecurity', 'Software Engineer',  'Video Game Connoisseur']);
        setFaveStock("NVIDIA, NVDA");
        setLinkedIn("https://www.linkedin.com/in/brian-kim-2217ba125/");
        setGitHub("https://github.com/brianshkim")
    }

    return (
        <>
        <div className="about-main">
            <div className="about-title">About alphahood Developers</div>
            <div className="about-lower">
                <div className="about-left">
                    <div className="about-name">
                        { person?.length > 0
                            ? person
                            : "Please select a Full-Stack Developer" }
                    </div>
                    <hr className="line-break-name"></hr>
                    { person?.length > 0 ? (
                        <>
                            <div className="about-left-lower">
                                {/* <div className="about-bio">About Developer:</div> */}
                                {/* <div className="about-dev-bio">{ bio }</div>
                                <span className="about-fav-stock">Favorite Stock:</span>
                                <span>{ favStock }</span>
                                <hr className="line-break-fav-stock"></hr> */}
                                <div id='code-box'>
                                    <div id="code-section">
                                        <div id='code-box-content'>
                                            <span>aboutDeveloper{'{'}</span>
                                            <br/>
                                            {bio && bio.map((activity) => {
                                                return (
                                                <div>
                                                    <div id='fav-activity-term'>=>{activity}</div>
                                                </div>
                                                )
                                            })}
                                            <div>{'}'}</div>
                                            <br/>
                                            <br/>
                                            <div>favoriteStock{'{'}</div>
                                            <div id='fav-activity-term'>=>'stock':  {favStock}</div>
                                            <div>{'}'}</div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="about-me">
                                <a href={ linkedIn } target="_blank" className="linkedin">
                                    <img
                                        className="linkedin-img"
                                        src={ LinkedInLogo }
                                    />

                                </a>
                                <a className="linkedin" href={ gitHub } target="_blank">
                                    <img
                                        className="linkedin-img"
                                        src={ GitHubLogo }
                                    />

                                </a>
                            </div>
                        </>
                    ) : null }
                </div>
                <div className="about-right">
                    <div className="name-links" onClick={ () => fino() }>
                        Augustino Elisaia
                    </div>
                    <div className="name-links" onClick={ () => dylan() }>
                        Dylan Peate
                    </div>
                    <div className="name-links" onClick={ () => izzy() }>
                        Israel Arvizu
                    </div>
                    <div className="name-links" onClick={ () => brian() }>
                        Brian Kim
                    </div>
                    { user?.id ? (
                        <NavLink className="aboutlink" to="/dashboard">
                            Return Home
                        </NavLink>
                    ) : (
                        <NavLink className="aboutlink" to="/dashboard">
                            Return to Dashboard
                        </NavLink>
                    ) }
                </div>
            </div>
        </div>
        </>
    );
};

export default About;
