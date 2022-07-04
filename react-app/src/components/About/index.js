import { useState } from "react";
import { useSelector } from "react-redux";
import { NavLink } from "react-router-dom";
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
        setBio("Software Engineering Student at App Academy");
        setFaveStock("Nike Inc: NKE");
        setLinkedIn("https://www.linkedin.com/in/augustino-elisaia-7307a822b/");
        setGitHub("https://github.com/elisaia55")
    }

    const dylan = () => {
        setPerson("Dylan Peate");
        setBio("Software Engineering Student at App Academy");
        setFaveStock("Nike Inc: NKE");
        setLinkedIn("https://www.linkedin.com/in/augustino-elisaia-7307a822b/");
        setGitHub("https://github.com/elisaia55")
    }


    const izzy = () => {
        setPerson("Israel Arvizu");
        setBio("Software Engineering Student at App Academy");
        setFaveStock("Nike Inc: NKE");
        setLinkedIn("https://www.linkedin.com/in/augustino-elisaia-7307a822b/");
        setGitHub("https://github.com/elisaia55")
    }

    const brian = () => {
        setPerson("Brian Kim");
        setBio("Software Engineering Student at App Academy");
        setFaveStock("Nike Inc: NKE");
        setLinkedIn("https://www.linkedin.com/in/augustino-elisaia-7307a822b/");
        setGitHub("https://github.com/elisaia55")
    }
};
