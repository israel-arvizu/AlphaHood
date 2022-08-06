import { useEffect } from 'react'
import automotive from './automotive.png'
import './trendinglist.css'
const Automotive = () =>{
    let navbarbg = document.getElementsByClassName('usernav-container')
    let outernavbg = document.getElementsByClassName('outer-container')
    console.log(outernavbg)

    useEffect(()=>{

    navbarbg[0].style.backgroundColor="#c9e7ec"
    outernavbg[0].style.backgroundColor="#c9e7ec"
    }, [navbarbg.length, outernavbg])





    return(
        <div className="automotivediv">
            <img src={automotive}></img>


        </div>


    )
}

export default Automotive
