import { useEffect } from 'react'
import top25 from './top25.png'
import './trendinglist.css'
const Top25 = () =>{
    let navbarbg = document.getElementsByClassName('usernav-container')
    let outernavbg = document.getElementsByClassName('outer-container')
    console.log(outernavbg)

    useEffect(()=>{

    navbarbg[0].style.backgroundColor="#ffed89"
    outernavbg[0].style.backgroundColor="#ffed89"
    }, [navbarbg.length, outernavbg])





    return(
        <div className="top25mostpopulardiv">
            <img src={top25}></img>


        </div>


    )
}

export default Top25
