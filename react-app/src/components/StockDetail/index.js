import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Redirect, useHistory, useParams } from 'react-router-dom'
import { getOneStock, getStocks, updateStock, purchaseStock } from '../../store/stocks'
import { loadOwnedStocks } from '../../store/ownedStocks'
// import { getNews } from '../../store/news'
import UserNavBar from '../UserNavBar'

import AddToListModal from '../AddToListModal'
import { loadAllLists } from '../../store/list'

import StockLineChart from '../Linechart-Component/StocksLineChart'
import { stockChartHistory } from '../../store/liststock';
import './StockDetail.css'


function StockDetail() {
    const history = useHistory()
    const dispatch = useDispatch()
    const ticker = useParams().ticker //could change ticker in obj
    const tickerUpper = ticker.toUpperCase()
    const stocks = useSelector(state => state.stocks)
    const selectedStock = stocks[tickerUpper]
    const [marketState, setMarketState] = useState(false)
    const formatter = new Intl.NumberFormat('en')
    const letterFormatter = new Intl.NumberFormat('en-US', {
        notation: "compact",
        maximumFractionDigits: 1
    })

    const newsArticles = useSelector(state => state.newsReducer.news);
    const sessionUser = useSelector(state => state.session.user)
    const myPortfolio = useSelector(state => state.ownedStocks.myPortfolio)
    const chartData = useSelector(state => state.listStockReducer.chartHistory)

    const [buyStock, setBuyStock] = useState('Buy')
    const [balance, setBalance] = useState(sessionUser.balance)
    const [shares, setShares] = useState(0)
    // let marketOpen = false
    // let currentDate = new Date('June 30, 2022 13:20:00')



    useEffect(() => {
        dispatch(getOneStock(tickerUpper))
        dispatch(loadOwnedStocks(sessionUser.id))
        dispatch(stockChartHistory(tickerUpper))
        dispatch(loadAllLists(sessionUser.id))
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
            dispatch(loadOwnedStocks(sessionUser.id))
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

    // if (selectedStock === undefined) {
    //     history.push('/')
    // }

    if (chartData === undefined) {
        return <h2>Loading Graph...</h2>
    }

    const handleSubmit = async (e) => {
        e.preventDefault();

        const transaction = {
            userId: sessionUser.id,
            userBalance: sessionUser.balance,
            shareCount: Math.abs(shares),
            stockPrice: selectedStock.currentPrice,
            stockId: selectedStock.id
        }
        await dispatch(purchaseStock(tickerUpper, transaction, 'buy'))
        history.push('/dashboard')
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
        history.push('/dashboard')
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



    const changeToday = () => {
        let change = (((selectedStock.currentPrice - selectedStock.regularMarketOpen) / selectedStock.regularMarketOpen) * 100).toFixed(2)
        let changeNum = selectedStock.currentPrice - selectedStock.regularMarketOpen
        return [change, changeNum]
    }
    let number = changeToday()[0]
    let priceDif = changeToday()[1]




    return (
        <>
            <UserNavBar />
            <div className='parent-container'>
                <div className='left-container'>
                    <div className='top-details'>
                        <h2>{selectedStock.name}</h2>
                        <p className='price-container'>${selectedStock.currentPrice}{marketState ? '' : <p className='after-hours'>After hours</p>}</p>
                        <p className={number > 0 ? 'positiveNum' : 'negativeNum'}>{
                            number > 0 ? <p>+${priceDif.toFixed(2)} (+{number}%)</p> : <p>${priceDif.toFixed(2)} ({number}%)</p>
                        }</p>
                    </div>
                    <div className='graph-container'>
                        <StockLineChart stockHistory={chartData} />
                    </div>
                    <h2>About</h2>
                    <hr></hr>
                    <div className='about-container'>
                        <p id='long-summary'>{selectedStock.longBusinessSummary}</p>
                        <div className='about-inner'>
                            <div className='employees-container'>
                                <p className='item-title'>Employees</p>
                                <p className='item-info'>{formatter.format(selectedStock.fullTimeEmployees)}</p>
                            </div>
                            <div className='headquarters-container'>
                                <p className='item-title'>Headquarters</p>
                                <p className='item-info'>{selectedStock.city}, {selectedStock.state}</p>
                            </div>
                        </div>
                    </div>
                    <h2 id='key-banner'>Key Statistics</h2>
                    <hr></hr>
                    <div className='key-statistics'>
                        <div className='marketCap-container key-container'>
                            <p className='item-title'>Market Cap</p>
                            <p className='item-info'>{
                                letterFormatter.format(selectedStock.marketCap)}</p>
                            {/* selectedStock.marketCap */}
                        </div>
                        <div className='trailingPE-container key-container'>
                            <p className='item-title'>Trailing P/E</p>
                            <p className='item-info'>{selectedStock.trailingPE.toFixed(2)}</p>
                        </div>
                        <div className='dividendYield-container key-container'>
                            <p className='item-title'>Dividend Yield</p>
                            <p className='item-info'>{selectedStock.dividendYield || '—'}</p>
                        </div>
                        <div className='averageVolume-container key-container'>
                            <p className='item-title'>Average Volume</p>
                            <p className='item-info'>{letterFormatter.format(selectedStock.averageVolume)}</p>
                        </div>
                        <div className='dayHigh-container key-container'>
                            <p className='item-title'>High Today</p>
                            <p className='item-info'>${selectedStock.dayHigh}</p>
                        </div>
                        <div className='dayLow-container key-container'>
                            <p className='item-title'>Low Today</p>
                            <p className='item-info'>${selectedStock.dayLow}</p>
                        </div>
                        <div className='regularMarketOpen-container key-container'>
                            <p className='item-title'>Open Price</p>
                            <p className='item-info'>${selectedStock.regularMarketOpen}</p>
                        </div>
                        <div className='volume-container key-container'>
                            <p className='item-title'>Volume</p>
                            <p className='item-info'>{letterFormatter.format(selectedStock.volume)}</p>
                        </div>
                        <div className='fiftyTwoWeekHigh-container key-container'>
                            <p className='item-title'>52 Week High</p>
                            <p className='item-info'>${selectedStock.fiftyTwoWeekHigh}</p>
                        </div>
                        <div className='fiftyTwoWeekLow-container key-container'>
                            <p className='item-title'>52 Week Low</p>
                            <p className='item-info'>${selectedStock.fiftyTwoWeekLow}</p>
                        </div>
                    </div>
                    {/* <div className='related-list-container'>
                        <h2>Related Lists</h2>
                        <button>{selectedStock.industry}</button>
                        <button>{selectedStock.state}</button>
                    </div> */}
                    {/* <div className='news-container'>
                <h2>News</h2>
                {
                    newsArticles ?
                        <p>{
                            newsArticles.title
                        }</p> :
                        <p> Sorry Couldn't Load News...</p>
                }
            </div> */}
                    <h2>Analyst Ratings</h2>
                    <hr></hr>
                    <div className='analyst-rating-container'>
                        <p>{selectedStock.recommendationKey}</p>
                    </div>
                    {/* <div className='Earnings'>
                <h2>Earnings</h2>
                <p>PUT EARNINGS HERE</p>
            </div> */}
                </div>
                <div className='right-container'>
                    <div className='right-inner-container'>
                        <div className='buy-sell-container'>
                            <h2 id='trade-tag'>Trade {selectedStock.ticker}</h2>
                            <hr></hr>
                            <form onSubmit={e => handleSubmit(e)}>
                                <input
                                    name='shares'
                                    type='number'
                                    // value={shares}
                                    onKeyDown={(e) => {
                                        if (e.target.value < 0) { e.target.value = e.target.value * -1 }
                                    }}
                                    onChange={e => setShares(e.target.value)}
                                ></input>
                                <div className='buy-sell-btns'>
                                    <button id='buy-btn' type="submit" disabled={
                                        sessionUser.balance <= selectedStock.currentPrice * shares
                                    }>Buy</button>
                                    <button id='sell-btn' onClick={e => sellShares(e)} disabled={
                                        owned()
                                    }>Sell</button>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div className='testBtn'>
                        <AddToListModal stock={selectedStock} />

                    </div>
                </div>
            </div>
        </>
    )
}



export default StockDetail
