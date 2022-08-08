import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { loadHomeNews } from '../../store/news'
import { addNewList, loadAllLists, deleteList } from '../../store/list';
import LineChart from '../../components/Linechart-Component/Linechart';
import EditListModal from '../EditListModal';
import EditList from '../EditListModal/EditListForm';
import { loadCurrentPortfolio, loadPortfolio } from '../../store/portfolio';
import { NavLink, useHistory } from 'react-router-dom';
import { loadStockList } from '../../store/liststock';
import UserNavBar from '../UserNavBar';
import alphahoodblack from '../../images/alphahoodblack.png'
import './dashboard.css';
import { authenticate } from '../../store/session';
import { listenerCount } from 'pg/lib/query';



function Dashboard() {
    const dispatch = useDispatch()
    const history = useHistory()
    const newsArticles = useSelector(state => state.newsReducer.news);
    const userlog = useSelector(state => state.session.user)
    //news not needed
    //const newsArticles = useSelector(state => state.newsReducer.news);
    const userId = useSelector(state => state.session.user.id)
    const [watchlistName, setWatchlistName] = useState(false)
    const [newListName, setNewListName] = useState("")
    const [displayPort, setDisplayPort] = useState(0)
    const [portfolioHistory, setPortfolioHistory] = useState({
        "2022-07-01 09:30:00-04:00": 0,
        "2022-07-01 09:35:00-04:00": 0,
        "2022-07-01 09:40:00-04:00": 0,
        "2022-07-01 09:45:00-04:00": 0,
        "2022-07-01 09:50:00-04:00": 0
    })
    const [portfolioGraph, setPortfolioGraph] = useState(false)
    const [updated, setUpdate] = useState(false)
    const [updateLog, setUpdateLog] = useState("Updating, One Sec!")
    const [enteredWatch, setEnteredWatch] = useState(false)


    const watchlists = useSelector(state => state.lists)
    const portfoliolist = watchlists.filter(watchlist => watchlist.name == "Portfolio")


    if (!userlog) {
        history.push('/')
    }




    const user = useSelector(state => state.session.user);
    const portfolio = useSelector(state => state.portfolio.portfolio);
    const currentPortfolio = useSelector(state => state.portfolio.CurrentPortfolio)
    const liststocks = useSelector(state => state.listStockReducer.listStock)

    useEffect(() => {
        dispatch(loadAllLists(userId))
        dispatch(authenticate())
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

        e.preventDefault()
    }
    const createlist = async (e) => {
        e.preventDefault()
        const newlist = {
            name: newListName,
            userId: userId
        }
        await dispatch(addNewList(newlist))
        setNewListName("")
    }

    const hidelist = (id)=>{
        let list = document.querySelectorAll(`#watchlist-${id}`)
        let arrow = document.getElementById(`hidestocklist${id}`).children[0]
        if (arrow.className==="fa-solid fa-angle-down"){
            arrow.className="fa-solid fa-angle-up"
        }
        else{
            arrow.className="fa-solid fa-angle-down"

        }

        for (let i = 0;i<list.length;i++){
            if (list[i].style.display !== "none") list[i].style.display = "none"
            else if (list[i].style.display === "none") {
                if (list[i].className="stock-list-link-container")list[i].style.display = "block"
                if (i === list.length-1){
                    list[i].className="watchlist-buttons-container-list"
                    list[i].style.display="flex"

                }

            }

        }
    }


    if (portfolio === undefined) {
        return (
            <div className='loading-dash-container'>
                <div className='loading-dash-image'>
                    <div className='loading-dash-text-container'>
                        <img src={alphahoodblack} className="home-logo-alpha-loading"></img>
                        <p className='loading-dash-text'>Loading all this Greatness </p>
                        <p className='loading-dash-text'>Please Wait...</p>
                        <div className='loading-dash-message-container'>
                            <p className='loading-dash-message'>If it takes longer than 30 seconds please refresh</p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    // if(newsArticles === undefined){
    //     dispatch(loadHomeNews())
    //     return <h2>Loading News Articles</h2>
    // }
    if (currentPortfolio !== undefined && !updated) {
        let price = currentPortfolio.value
        price = price.toFixed(2)
        setDisplayPort(price)
        setUpdate(true)
        if (currentPortfolio.errors.length > 0)
            setUpdateLog("Errors in the API, Amount may be incorrect, please refresh to retry")
        else
            setUpdateLog("")
    }

    if (portfolio !== undefined && !portfolioGraph) {
        let portfolioHist = portfolio
        setPortfolioHistory({ ...portfolioHist })
        setPortfolioGraph(true)
    }
    if (!watchlists) return <h2>loading</h2>
    return (
        <>
            <UserNavBar />
            <div className='main-container-dash'>
                <div className='outer-left-container'>
                    <div className='portfolio-container'>
                        <div>{updateLog.length > 0 &&
                            <p id='dashboard-port-update-text'>{updateLog}</p>
                        }
                            <p id='portfolio-value-cont'>${displayPort}</p>
                        </div>
                        <div id='chart-container-main'>
                            <LineChart portfolio={portfolioHistory} />
                        </div>
                        <p id='period-dash-graph'>24h</p>
                        <hr className='line-break-dashboard'></hr>
                    </div>
                    <div className='portfolio-buying-container'>
                        <p id='buying-power-header'>Buying Power</p>
                        <p id='buying-power-header'>${user.balance.toFixed(2)}</p>
                    </div>
                    <hr className='line-break-dashboard'></hr>
                    {<div className='trending-list-main-container'>
                        <p id='trending-list-header'>Trending Lists</p>
                        <hr className='line-break-dashboard'></hr>
                        <div className='trending-list-button-container'>
                            <NavLink to='/trendinglists/top-hot-10' style={{ textDecoration: 'none' }}>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/100_most_popular/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Top Hot 10</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/creators-choice' style={{ textDecoration: 'none' }}>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/20_most_popular_etfs/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Creators Choice</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/25-most-popular' style={{ textDecoration: 'none' }}>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/software/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>25 Most Popular</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/technology' style={{ textDecoration: 'none' }}>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/technology/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Technology</p>
                                </div>
                            </NavLink>
                            <NavLink to='/trendinglists/automotive' style={{ textDecoration: 'none' }}>
                                <div className='trending-list-button'>
                                    <img className='trending-list-image-btn' src='https://cdn.robinhood.com/app_assets/list_illustrations/automotive/circle_28/1x.png' />
                                    <p className='trending-list-text-btn'>Automotive</p>
                                </div>
                            </NavLink>
                        </div>
                    </div>}
                    {/* <h2>News</h2> */}
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
                    <div>
                        <div id='create-list-content'>
                            <p id='create-list-header-text'>Lists</p>
                        </div>
                        <ul className='list-stocks-content'>
                            <div className='watchlist-headers-container'>
                                <li className='watchlist-dash-port-name'>{!!watchlists.length && !!portfoliolist && portfoliolist[0].name}</li>
                            </div>
                            {!!watchlists.length && !!liststocks && liststocks[portfoliolist[0].id].map(stock => (
                                <div className='stock-list-link-container-portfolio' key={stock.currentPrice}>
                                    <a style={{ textDecoration: 'none' }} href={`/stocks/${stock.ticker.toUpperCase()}`}>
                                        <div className='stock-inside-content' key={stock.ticker}>
                                            <p className='stock-title-header'>{stock.ticker}</p>
                                            <p className='stock-title-price-cont'>${stock.currentPrice}</p>
                                        </div>
                                    </a>
                                </div>
                            ))}
                            {!!watchlists.length &&
                                watchlists.map((watchlist, idx) => {
                                    if (watchlist.name !== "Portfolio") {
                                        return (
                                            <li key={idx}>
                                                <div className='watchlist-headers-container-extra'>
                                                    <div><p className='watchlist-dash-title'>{watchlist.name}</p></div>
                                                    <div id={`hidestocklist${watchlist.id}`}className="hidestocklist" onClick={()=>hidelist(watchlist.id)}><i className="fa-solid fa-angle-down"></i></div>
                                                </div>
                                                {!!liststocks && liststocks[watchlist.id] !== undefined && liststocks[watchlist.id]?.map((stock) => {
                                                    return (
                                                        <div id={`watchlist-${watchlist.id}`} className='stock-list-link-container' key={stock.ticker}>
                                                            <a style={{ textDecoration: 'none' }} href={`/stocks/${stock.ticker.toUpperCase()}`}>
                                                                <div className='stock-inside-content' key={stock.ticker}>
                                                                    <p className='stock-title-header'>{stock.ticker}</p>
                                                                    <p className='stock-title-price-cont'>${stock.currentPrice}</p>
                                                                </div>
                                                            </a>
                                                        </div>
                                                    )
                                                })}
                                                <div id={`watchlist-${watchlist.id}`} className='watchlist-buttons-container-list'>
                                                    <EditListModal id={watchlist.id} />
                                                    <button className='watchlist-buttons-indivial-btn delete-btn-list' id={watchlist.id} onClick={deleteAList}>Delete List</button>
                                                </div>
                                            </li>
                                        )
                                    }
                                })}
                        </ul>
                    </div>
                    <div>
                        <div id='create-list-content'>
                            <p id='create-list-header-text'>Create a List</p>
                            <button id='create-list-add-btn' onClick={() => setWatchlistName(true)}>+</button>
                        </div>
                        {watchlistName &&
                            <div>
                                <form className='watchlist-form-container'
                                    onSubmit={createlist}>
                                    <input
                                        id='watchlist-input-form'
                                        name="listName"
                                        type="text"
                                        placeholder='List Name'
                                        value={newListName}
                                        onChange={(e) => setNewListName(e.target.value)}></input>
                                    <div className='watchlist-button-container'>
                                        <button className='watchlist-button-form cancel-buttn' onClick={() => setWatchlistName(false)}>Cancel</button>
                                        <button className='watchlist-button-form create-buttn' type="submit">Create List</button>
                                    </div>
                                </form>
                            </div>
                        }
                    </div>
                </div>


            </div >

        </>
    )
}




export default Dashboard
