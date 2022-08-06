import {useEffect, useState} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {useParams} from 'react-router-dom'
import { loadstocklist } from '../store/stocks'
import UserNavBar from './UserNavBar'
import TopHotTen from './TrendingList/tophot10'
import CreatorsChoice from './TrendingList/creatorschoice'
import Top25 from './TrendingList/25mostpopular'
import Technology from './TrendingList/Technology'
import Automotive from './TrendingList/automotive'
import './TrendingList/trendinglist.css'




import { topTen, creator, mostpop, tech, auto, topTenDefault,
    creatorDefault, mostPopDefault, techDefault, autoDefault } from './TrendingList/TrendingListData'



function TrendingLists() {
    const [stockDetails, setStockDetails] = useState([])
    const [updated, setUpdated] = useState(false)
    const [initialRender, setInitialRender] = useState(false)
    let dispatch = useDispatch()
    let topic = []
    let {list} = useParams()


    function numToString(num) {
        var newValue = num;
        if (num >= 1000) {
            var suffixes = ["", "k", "m", "b","t"];
            var suffixNum = Math.floor( (""+num).length/3 );
            var shortValue = '';
            for (var precision = 4; precision >= 1; precision--) {
                shortValue = parseFloat( (suffixNum !== 0 ? (num / Math.pow(1000,suffixNum) ) : num).toPrecision(precision));
                var dotLessShortValue = (shortValue + '').replace(/[^a-zA-Z 0-9]+/g,'');
                if (dotLessShortValue.length <= 2) { break; }
        }
        if (shortValue % 1 !== 0)  shortValue = shortValue.toFixed(1);
        newValue = shortValue+suffixes[suffixNum];
        }
        return newValue;
    }

    const stocks = useSelector(state => state.stocks.stocks)
    const liststocks =useSelector(state=> state.listReducer)

    switch (list){
        case "top-hot-10":
            topic = topTen
            break
        case "creators-choice":
            topic = creator
            break
        case "25-most-popular":
            topic = mostpop
            break
        case "technology":
            topic = tech
            break
        case "automotive":
            topic = auto
            break
        default:
            topic = []
    }

    let listarray = list.split("-")
    let titlearray = listarray.map(word=>{
        return word[0].toUpperCase() + word.slice(1, word.length)
    })
    let title = titlearray.join(" ")

    useEffect(()=>{
        dispatch(loadstocklist(topic))
    }, [dispatch])

    if(!stocks && !initialRender) {
        switch (list){
            case "top-hot-10":
                topic = topTenDefault
                break
            case "creators-choice":
                topic = creatorDefault
                break
            case "25-most-popular":
                topic = mostPopDefault
                break
            case "technology":
                topic = techDefault
                break
            case "automotive":
                topic = autoDefault
                break
            default:
                topic = []
        }

        setStockDetails(topic)
        setInitialRender(true)
    }

    if(stocks !== undefined && !updated){
        setStockDetails(stocks)
        setUpdated(true)
    }
    return(
        <>
            <UserNavBar />
                <div className="trendinglistcontainer">
                    {list==="top-hot-10" && <TopHotTen/>}
                    {list==="creators-choice" && <CreatorsChoice />}
                    {list==="25-most-popular" && <Top25/>}
                    {list==="technology" && <Technology/>}
                    {list==="automotive" && <Automotive/>}

                    <div>
                        <div className="tablecontainer">
                            <div className="trendinglisttitle">{title}
                            {list === "top-hot-10" &&
                             <span className="trendinglisttitlelogo">  <i class="fa-solid fa-fire-flame-curved"></i></span>}
                             </div>

                            <div>
                                <table className = "trendingtable">
                                    <tr>
                                        <th className="tlist">Name</th>
                                        <th className="tlist">Symbol</th>
                                        <th className="tlist">Price</th>
                                        <th className="tlist">Today</th>
                                        <th className="tlist">Market Cap</th>
                                    </tr>
                                        {stockDetails.map(stock=>{
                                            return (
                                                <tr className="tlistdatacontainer">
                                                    <td className="tlistdata">{stock.name}</td>
                                                    <td className="tlistdata">{stock.ticker}</td>
                                                    <td className="tlistdata">{stock.price}</td>
                                                    <td className="tlistdata">{stock.todayPerformance + "%"}</td>
                                                    <td className="tlistdata">{numToString(stock.marketCap)}</td>
                                                </tr>
                                            )
                                        })}
                                </table>
                            </div>
                        </div>


                    </div>
                </div>
       </>
    )

}

export default TrendingLists
