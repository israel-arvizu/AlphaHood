import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { getOneStock, getStocks, updateStock, purchaseStock } from '../../store/stocks'
import { loadOwnedStocks } from '../../store/ownedStocks'
// import { getNews } from '../../store/news'
import UserNavBar from '../UserNavBar'

import AddToListModal from '../AddToListModal'
import { loadAllLists } from '../../store/list'

import StockLineChart from '../Linechart-Component/StocksLineChart'
import { stockChartHistory } from '../../store/stocks'


function StockDetail() {
    const dispatch = useDispatch()
    const ticker = useParams().ticker //could change ticker in obj
    const tickerUpper = ticker.toUpperCase()
    const stocks = useSelector(state => state.stocks)
    const selectedStock = stocks[tickerUpper]
    const [marketState, setMarketState] = useState(false)

    const newsArticles = useSelector(state => state.newsReducer.news);
    const sessionUser = useSelector(state => state.session.user)
    const myPortfolio = useSelector(state => state.ownedStocks.myPortfolio)
    const chartData = useSelector(state => state.stocks.chartHistory)

    const [buyStock, setBuyStock] = useState('Buy')
    const [balance, setBalance] = useState(sessionUser.balance)
    const [shares, setShares] = useState(0)
    // let marketOpen = false
    // let currentDate = new Date('June 30, 2022 13:20:00')


    useEffect(()=>{
        dispatch(loadAllLists(sessionUser.id))
    })


    useEffect(() => {
        dispatch(getOneStock(tickerUpper))
        dispatch(loadOwnedStocks(sessionUser.id))
        dispatch(stockChartHistory(tickerUpper))
        // dispatch(getNews(tickerUpper))
        let currentDate = new Date()
        let currentHour = currentDate.getHours()
        let currentDay = currentDate.getDay()
        let currentMinute = currentDate.getMinutes()
        if (currentDay > 0 && currentDay < 6) {
            if (currentHour < 16 && currentHour > 9) {
                setMarketState(true)
            } else if (currentHour === 9 && currentMinute > 29) {
                setMarketState(true)
            }
        } else {
            setMarketState(false)
        }
    }, [dispatch])


    useEffect(() => {
        if (marketState) {
            dispatch(updateStock(tickerUpper))
            // dispatch(loadOwnedStocks(sessionUser.id))
            let currentDate = new Date()
            let currentHour = currentDate.getHours()
            let currentDay = currentDate.getDay()
            let currentMinute = currentDate.getMinutes()
            if (currentDay > 0 && currentDay < 6) {
                if (currentHour < 16 && currentHour > 9) {
                    setMarketState(true)
                } else if (currentHour === 9 && currentMinute > 29) {
                    setMarketState(true)
                }
            } else {
                setMarketState(false)
            }
        }
    })

    // news
    // useEffect(() => {
    //     if (marketState) {

    //         console.log('GotNews')
    //     }
    // }, [dispatch])

    // dispatch(getNews(tickerUpper))




    if (selectedStock === undefined || myPortfolio === undefined) return <h2>Loading...</h2>
    if(chartData === undefined){
        return <h2>Loading Graph...</h2>
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const transaction = {
            userId: sessionUser.id,
            userBalance: sessionUser.balance,
            shareCount: shares,
            stockPrice: selectedStock.currentPrice,
            stockId: selectedStock.id
        }
        await dispatch(purchaseStock(tickerUpper, transaction, 'buy'))
    }

    const sellShares = async (e) => {
        e.preventDefault()

        const transaction = {
            userId: sessionUser.id,
            userBalance: sessionUser.balance,
            shareCount: shares,
            stockPrice: selectedStock.currentPrice,
            stockId: selectedStock.id
        }
        await dispatch(purchaseStock(tickerUpper, transaction, 'sell'))
    }

    const owned = () => {
        for (let i = 0; i < myPortfolio.length; i++) {
            if (myPortfolio[i].stockId === selectedStock.id) {
                if (shares <= myPortfolio[i].shares) {
                    return false
                }
            }
        }
        return true
    }


    return (
        <>
            <UserNavBar />
            <form onSubmit={e => handleSubmit(e)}>
                <input
                    name='shares'
                    type='number'
                    value={shares}
                    onChange={e => setShares(e.target.value)}
                ></input>
                <button type="submit" id='buy-button' disabled={
                    sessionUser.balance <= selectedStock.currentPrice * shares
                }>Buy</button>
                <button onClick={e => sellShares(e)} disabled={
                    owned()
                }>Sell</button>
            </form>
            <AddToListModal stock={selectedStock} />
            <p>Market Open:</p>
            <p>
                {marketState ? 'True' : 'False'}
            </p>
            <div className='top-details'>
                <h2>{selectedStock.name}</h2>
                <p>{selectedStock.currentPrice}</p>
                <p>Change Today</p>
            </div>
            <div className='graph-container'>
                <StockLineChart stockHistory={chartData}/>
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
                {
                    newsArticles ?
                        <p>{
                            newsArticles.title
                        }</p> :
                        <p> Sorry Couldn't Load News...</p>
                }
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
