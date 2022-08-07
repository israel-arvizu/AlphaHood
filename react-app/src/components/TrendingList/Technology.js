import { useEffect } from 'react'
import { useParams } from 'react-router-dom'

import './trendinglist.css'
import toptech from './toptech.png'
const Technology = () =>{
    let {list} = useParams()
    let navbarbg = document.getElementsByClassName('usernav-container')
    let outernavbg = document.getElementsByClassName('outer-container')
    console.log(outernavbg)

    useEffect(()=>{
        navbarbg[0].style.backgroundColor="#2b94f6 "
        outernavbg[0].style.backgroundColor="#2b94f6 "


    }, [list])


    return(
        <div className="Technologydiv">
            <img src={toptech}></img>


        </div>


    )
}

export default Technology
