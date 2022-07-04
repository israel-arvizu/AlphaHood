import {useEffect, useState} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {useParams} from 'react-router-dom'
import { loadstocklist } from '../store/stocks'
import UserNavBar from './UserNavBar'


import { topTen, creator, mostpop, tech, auto, topTenDefault,
    creatorDefault, mostPopDefault, techDefault, autoDefault } from './TrendingList/TrendingListData'



function TrendingLists() {
    const [stockDetails, setStockDetails] = useState([])
    const [updated, setUpdated] = useState(false)
    const [initialRender, setInitialRender] = useState(false)
    let dispatch = useDispatch()
    let topic = []
    let {list} = useParams()
    console.log(tech)

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
                <div>
                    <div>
                        <img></img>
                    </div>
                    <div>
                        <div>
                            <h1>{title}</h1>
                            <p>description</p>
                            <div>
                                <table>
                                    <tr>
                                        <th>Name</th>
                                        <th>Symbol</th>
                                        <th>Price</th>
                                        <th>Today</th>
                                        <th>Market Cap</th>
                                    </tr>
                                        {stockDetails.map(stock=>{
                                            return (
                                                <tr>
                                                    <td>{stock.name}</td>
                                                    <td>{stock.ticker}</td>
                                                    <td>{stock.price}</td>
                                                    <td>{stock.todayPerformance + "%"}</td>
                                                    <td>{numToString(stock.marketCap)}</td>
                                                </tr>
                                            )
                                        })}
                                </table>
                            </div>
                        </div>
                        <div>
                            <h3>WatchList</h3>
                        </div>

                    </div>
                </div>
       </>
    )

}

export default TrendingLists
