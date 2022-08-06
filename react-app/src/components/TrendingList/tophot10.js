import { useEffect } from 'react'
import { useParams } from 'react-router-dom'
import tophot10 from './tophot10.png'
import './trendinglist.css'
const TopHotTen = () =>{
    let {list} = useParams()
    let navbarbg = document.getElementsByClassName('usernav-container')
    let outernavbg = document.getElementsByClassName('outer-container')
    console.log(outernavbg)

    useEffect(()=>{

    navbarbg[0].style.backgroundColor="#ff8b5d"
    outernavbg[0].style.backgroundColor="#ff8b5d"
    }, [list])





    return(
        <div className="top10div">
            <img src={tophot10}></img>


        </div>


    )
}

export default TopHotTen
