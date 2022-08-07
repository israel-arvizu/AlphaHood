import { useEffect } from 'react'
import automotive from './automotive.png'
import { useParams } from 'react-router-dom'
import './trendinglist.css'
const Automotive = () =>{
    let {list} = useParams()
    let navbarbg = document.getElementsByClassName('usernav-container')
    let outernavbg = document.getElementsByClassName('outer-container')


    useEffect(()=>{

    navbarbg[0].style.backgroundColor="#c9e7ec"
    outernavbg[0].style.backgroundColor="#c9e7ec"
    }, [list])





    return(
        <div className="automotivediv">
            <img src={automotive}></img>


        </div>


    )
}

export default Automotive
