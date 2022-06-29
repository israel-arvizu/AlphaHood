import {useEffect, useState} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import {useParams} from 'react-router-dom'
import { loadstocklist } from '../store/stocks'

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
                                            <td>{stock.marketCap}</td>
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
    )

}

export default TrendingLists
