import {useEffect, useState} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {useParams} from 'react-router-dom'
import { loadstocklist } from '../store/stocks'
import UserNavBar from './UserNavBar'

const topTen = ["AMZN", "PYPL", "NVDA", "SHOP", "RDFN", "APPL", "ERIC", "PANW", "ROKU", "TSLA"]
const creator = ["GOOGL", "NVDA", "NKE", "MLAI" ]
const mostpop = ["APPL", "MSFT", "AMZN", "TSLA", "GOOGL", "GOOG", "NVDA", "BRK.B",
                "META", "UNH", "JNJ","JPM","V","PG","XOM","HD","CVX","MA","BAC",
                "ABBV","PFE", "AVGO","COST","DIS","KO"]
const tech = ["HPE", "MNDT", "ARW", "HPO","INTC","GDDY","BKI","SNX","ON","NATI","SWCH","AZPN","PANW", "PSTG", "DGI"]
const auto = ["TSLA", "GM","F","TM","KMX","CVNA","RACE","STLA","NIO","HMC"]


function TrendingLists() {
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

    if(!stocks) return <h2>Loading</h2>
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
                                        {stocks.map(stock=>{
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
