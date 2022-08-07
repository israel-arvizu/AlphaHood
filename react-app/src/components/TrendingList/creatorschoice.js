import { useEffect } from 'react'
import creatorschoice from './creatorschoice.png'
import { useParams } from 'react-router-dom'
import './trendinglist.css'
const CreatorsChoice= () =>{
    let {list} = useParams()
    let navbarbg = document.getElementsByClassName('usernav-container')
    let outernavbg = document.getElementsByClassName('outer-container')
    console.log(outernavbg)

    useEffect(()=>{

    navbarbg[0].style.backgroundColor="#ffa985"
    outernavbg[0].style.backgroundColor="#ffa985"

    return (()=>{

    })
    }, [list])





    return(
        <div className="creatorschoicediv">
            <img src={creatorschoice}></img>


        </div>


    )
}

export default CreatorsChoice
