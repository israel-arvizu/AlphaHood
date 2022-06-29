import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { getOneStock, getStocks } from '../../store/stocks'

function StockDetail() {
    const dispatch = useDispatch()
    const ticker = useParams().ticker //could change ticker in obj
    const tickerUpper = ticker.toUpperCase()
    const stocks = useSelector(state => state.stocks)
    const selectedStock = stocks[tickerUpper]

    // const stock = useSelector(state => state.stocksReducer.stock) //?
    useEffect(() => {
        dispatch(getOneStock(tickerUpper))
    }, [dispatch])

    // if (stock === undefined) return <h2>Loading</h2>


    if (selectedStock == undefined) return <h2>Loading...</h2>


    return (
        <>
            <div className='top-details'>
                <h2>{selectedStock.name}</h2>
                <p>{selectedStock.currentPrice}</p>
                <p>Change Today</p>
            </div>
            <div className='graph-container'>
                {/* GRAPH GOES HERE */}
            </div>
            <div className='about-container'>
                <h2>About</h2>
                <p>{selectedStock.longBusinessSummary}</p>
                <div className='employees-container'>
                    <p>Employees</p>
                    <p>{selectedStock.fullTimeEmployees}</p>
                </div>
                <div className='headquarters-container'>
                    <p>Headquarters</p>
                    <p>{selectedStock.city}, {selectedStock.state}</p>
                </div>
            </div>
            <div className='key-statistics'>
                <h2>Key Statistics</h2>
                <div className='marketCap-container'>
                    <p>Market Cap</p>
                    <p>{selectedStock.marketCap}</p>
                </div>
                <div className='trailingPE-container'>
                    <p>Trailing Price-Earnings</p>
                    <p>{selectedStock.trailingPE}</p>
                </div>
                <div className='dividendYield-container'>
                    <p>Dividend Yield</p>
                    <p>{selectedStock.dividendYield}</p>
                </div>
                <div className='averageVolume-container'>
                    <p>Average Volume</p>
                    <p>{selectedStock.averageVolume}</p>
                </div>
                <div className='dayHigh-container'>
                    <p>High Today</p>
                    <p>{selectedStock.dayHigh}</p>
                </div>
                <div className='dayLow-container'>
                    <p>Low Today</p>
                    <p>{selectedStock.dayLow}</p>
                </div>
                <div className='regularMarketOpen-container'>
                    <p>Regular Market Open</p>
                    <p>{selectedStock.regularMarketOpen}</p>
                </div>
                <div className='volume-container'>
                    <p>Volume</p>
                    <p>{selectedStock.volume}</p>
                </div>
                <div className='fiftyTwoWeekHigh-container'>
                    <p>52 Week High</p>
                    <p>{selectedStock.fiftyTwoWeekHigh}</p>
                </div>
                <div className='fiftyTwoWeekLow-container'>
                    <p>52 Week Low</p>
                    <p>{selectedStock.fiftyTwoWeekLow}</p>
                </div>
            </div>
            <div className='related-list-container'>
                <h2>Related Lists</h2>
                <button>{selectedStock.industry}</button>
                <button>{selectedStock.state}</button>
            </div>
            <div className='news-container'>
                <h2>News</h2>
                <p>INSERT NEWS HERE</p>
            </div>
            <div className='analyst-rating-container'>
                <h2>Analyst Ratings</h2>
                <p>{selectedStock.recommendationKey}</p>
            </div>
            <div className='Earnings'>
                <h2>Earnings</h2>
                <p>PUT EARNINGS HERE</p>
            </div>
        </>
    )
}

export default StockDetail
