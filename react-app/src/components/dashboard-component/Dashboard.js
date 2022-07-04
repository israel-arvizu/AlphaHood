import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { loadHomeNews } from '../../store/news'
import { addNewList, loadAllLists, deleteList } from '../../store/list';
import LineChart from '../../components/Linechart-Component/Linechart';
import EditListModal from '../EditListModal';
import EditList from '../EditListModal/EditListForm';
import { loadPortfolio, loadCurrentPortfolio } from '../../store/stocks';
import { NavLink, useHistory } from 'react-router-dom';
import { loadStockList } from '../../store/liststock';
import UserNavBar from '../UserNavBar';
import './dashboard.css';



function Dashboard() {
    const dispatch = useDispatch()
    const history = useHistory()
    const newsArticles = useSelector(state => state.newsReducer.news);
    const userId = useSelector(state => state.session.user.id)
    const [watchlistName, setWatchlistName] = useState(false)
    const [newListName, setNewListName] = useState("")
    const [displayPort, setDisplayPort] = useState(0)
    const [portfolioHistory, setPortfolioHistory] = useState({})
    const [portfolioGraph, setPortfolioGraph] = useState(false)
    const [updated, setUpdate] = useState(false)
    const [updateLog, setUpdateLog] = useState("Updating, One Sec!")
    const [enteredWatch, setEnteredWatch] = useState(false)
    const watchlists = useSelector(state => state.lists)



    const user = useSelector(state => state.session.user);
    const portfolio = useSelector(state => state.stocks.portfolio);
    const currentPortfolio = useSelector(state => state.stocks.CurrentPortfolio)
    const liststocks = useSelector(state => state.listStockReducer.listStock)

    useEffect(() => {
        dispatch(loadAllLists(userId))
        dispatch(loadHomeNews())
        dispatch(loadPortfolio(user.id))
        dispatch(loadCurrentPortfolio(user.id))
    }, [dispatch])



    if (watchlists && watchlists.length > 0 && !enteredWatch) {
        let watchListIds = []
        watchlists.map((list) => {
            watchListIds.push(list.id)
        })
        dispatch(loadStockList(watchListIds))
        setEnteredWatch(true)
    }

    const deleteAList = async (e) => {
        dispatch(deleteList(e.target.id))
        console.log(e.target.id)
        e.preventDefault()
    }
    const createlist = async (e) => {
        e.preventDefault()
        const newlist = {
            name: newListName,
            userId: userId
        }
        await dispatch(addNewList(newlist))
    }


    if (portfolio === undefined) {
        return <h2>Loading portfolio</h2>
    }

    // if(newsArticles === undefined){
    //     dispatch(loadHomeNews())
    //     return <h2>Loading News Articles</h2>
    // }
    if (currentPortfolio !== undefined && !updated) {
        let price = currentPortfolio
        price = price.toFixed(2)
        setDisplayPort(price)
        setUpdate(true)
        setUpdateLog("")
    }

    if (portfolio !== undefined && !portfolioGraph) {
        let portfolioHist = portfolio
        setPortfolioHistory(portfolioHist)
        setPortfolioGraph(true)
    }
    if (!watchlists) return <h2>loading</h2>
    return (
        <>
            <UserNavBar />
            <div className='main-container-dash'>
                <div className='outer-left-container'>
                    <div className='portfolio-container'>
                        <div>
                            <p>{ updateLog }</p>
                            <p id='portfolio-value-cont'>${ displayPort }</p>
                        </div>
                        <div id='chart-container-main'>
                            <LineChart portfolio={ portfolioHistory } />
                        </div>
                        <p id='period-dash-graph'>24h</p>
                        <hr className='line-break-dashboard'></hr>
                    </div>
                    <div className='portfolio-buying-container'>
                        <p id='buying-power-header'>Buying Power</p>
                        <p id='buying-power-header'>${ user.balance.toFixed(2) }</p>
                    </div>
                    <hr className='line-break-dashboard'></hr>
                    <div className='trending-list-main-container'>
                        <p id='trending-list-header'>Trending Lists</p>
                        <hr className='line-break-dashboard'></hr>
                        <div className='trending-list-button-container'>
                            <NavLink to='/trendinglists/top-hot-10' style={ { textDecoration: 'none' } }>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/100_most_popular/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Top Hot 10</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/creators-choice' style={ { textDecoration: 'none' } }>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/20_most_popular_etfs/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Creators Choice</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/25-most-popular' style={ { textDecoration: 'none' } }>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/software/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>25 Most Popular</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/technology' style={ { textDecoration: 'none' } }>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/technology/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Technology</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/automotive' style={ { textDecoration: 'none' } }>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/automotive/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Automotive</p>
                                </div>
                            </NavLink>
                        </div>
                    </div>
                    <h2>News</h2>
                    {/* {newsArticles.map((article) => {
                        if (article.thumbnail !== undefined)
                            return (
                                <div key={article.title}>
                                    <hr></hr>
                                    <a href={article.link}>
                                        <img src={article.thumbnail.resolutions[1].url} alt='thumbnail' />
                                        <p>{article.publisher}</p>
                                        <h3>{article.title}</h3>
                                    </a>
                                    <div>
                                        <p>{article.relatedTickers[0]}</p>
                                        <p>{article.relatedTickers[1]}</p>
                                    </div>
                                </div>
                            )
                        return null
                    })} */}
                </div>
                <div className='outer-right-container'>
                    WatchList
                    <button onClick={ () => setWatchlistName(true) }>+</button>

                    { watchlistName &&
                        <div>
                            <form
                                onSubmit={ createlist }>
                                <input name="listName"
                                    type="text"
                                    placeholder='Your list name'
                                    value={ newListName }
                                    onChange={ (e) => setNewListName(e.target.value) }></input>
                                <button type="submit">Add List</button>
                            </form>
                        </div>
                    }
                    <div>
                        <ul>
                            { !!watchlists.length &&
                                watchlists.map(watchlist => {

                                    return (
                                        <li key={ watchlist.id }>{ watchlist.name }

                                            { !!liststocks && liststocks[watchlist.id] !== undefined && liststocks[watchlist.id]?.map((stock) => {
                                                return (
                                                    <div key={ stock.ticker }>
                                                        <span>{ stock.ticker }</span>
                                                        <span>{ stock.currentPrice }</span>
                                                    </div>
                                                )
                                            }) }
                                            <EditListModal id={ watchlist.id } />
                                            <button id={ watchlist.id } onClick={ deleteAList }>Delete</button>
                                        </li>
                                    )
                                }) }
                        </ul>
                    </div>


                }
                </div>
                <div>
                    <ul>
                        { !!watchlists.length &&
                            watchlists.map(watchlist => {


                                return (
                                    <li key={ watchlist.id }>{ watchlist.name }

                                        { !!liststocks && liststocks[watchlist.id] !== undefined && liststocks[watchlist.id]?.map((stock) => {
                                            return (
                                                <div key={ stock.ticker }>
                                                    <span>{ stock.ticker }</span>
                                                    <span>{ stock.currentPrice }</span>
                                                </div>
                                            )
                                        }) }
                                        <EditListModal id={ watchlist.id } />
                                        <button id={ watchlist.id } onClick={ deleteAList }>Delete</button>
                                    </li>
                                )
                            }) }
                    </ul>




                </div>
            </div>
        </>
    )
}




export default Dashboard
