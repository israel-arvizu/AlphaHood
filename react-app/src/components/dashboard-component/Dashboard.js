import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { loadHomeNews } from '../../store/news'
import { addNewList, loadAllLists, deleteList } from '../../store/list';
import LineChart from '../../components/Linechart-Component/Linechart';
import EditListModal from '../EditListModal';
import EditList from '../EditListModal/EditListForm';
import { loadPortfolio, loadCurrentPortfolio } from '../../store/stocks';
import { NavLink } from 'react-router-dom';
import { loadStockList} from '../../store/liststock';




function Dashboard() {
    const dispatch = useDispatch()
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
    const watchlists = useSelector(state=>state.lists)



    const user = useSelector(state => state.session.user);
    const portfolio = useSelector(state => state.stocks.portfolio);
    const currentPortfolio = useSelector(state => state.stocks.CurrentPortfolio)
    const liststocks = useSelector(state=>state.listStockReducer.listStock)

    useEffect(() => {
        dispatch(loadAllLists(userId))
        dispatch(loadHomeNews())
        dispatch(loadPortfolio(user.id))
        dispatch(loadCurrentPortfolio(user.id))
    }, [dispatch])

    if(watchlists && watchlists.length > 0 && !enteredWatch){
        let watchListIds = []
        console.log("entered watchlist")
        console.log(watchlists)
        watchlists.map((list) => {
            console.log(list)
            watchListIds.push(list.id)
        })
        dispatch(loadStockList(watchListIds))
        setEnteredWatch(true)
    }

    const deleteAList = async(e)=>{
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


    if (portfolio === undefined){
        return <h2>Loading portfolio</h2>
    }

    // if(newsArticles === undefined){
    //     dispatch(loadHomeNews())
    //     return <h2>Loading News Articles</h2>
    // }
    if(currentPortfolio !== undefined && !updated){
        let price = currentPortfolio
        price = price.toFixed(2)
        setDisplayPort(price)
        setUpdate(true)
        setUpdateLog("")
    }

    if(portfolio !== undefined && !portfolioGraph){
        let portfolioHist = portfolio
        setPortfolioHistory(portfolioHist)
        setPortfolioGraph(true)
    }

    return (
        <>
            <div>
                LeftSection
                <div>
                    <div>
                        <h3>{updateLog}</h3>
                        <h2>${displayPort}</h2>
                    </div>
                    <LineChart portfolio={portfolioHistory}/>
                </div>
                <h2>Buying Power</h2>
                    <p>{user.balance.toFixed(2)}</p>
                <h2>Trending Lists</h2>
                <div>
                    <NavLink to='/trendinglists/top-hot-10'><button>Top Hot 10</button></NavLink>
                    <NavLink to='/trendinglists/creators-choice'><button>Creators Choice</button></NavLink>
                    <NavLink to='/trendinglists/25-most-popular'><button>25 Most Popular</button></NavLink>
                    <NavLink to='/trendinglists/technology'><button>Technology</button></NavLink>
                    <NavLink to='/trendinglists/automotive'><button>Automotive</button></NavLink>
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
            <div>
                WatchList
                <button onClick={() => setWatchlistName(true)}>+</button>

                {watchlistName &&
                    <div>
                        <form
                            onSubmit={createlist}>
                            <input name="listName"
                                type="text"
                                placeholder='Your list name'
                                value={newListName}
                                onChange={(e) => setNewListName(e.target.value)}></input>
                            <button type="submit">Add List</button>

                        </form>

                    </div>

                }

                <div>
                    <ul>
                        {!!watchlists.length &&
                        watchlists.map(watchlist=>{
                            console.log(watchlist.id)
                            return(
                            <li key={watchlist.id}>{watchlist.name}

                            { !!liststocks && liststocks[watchlist.id]  !==undefined && liststocks[watchlist.id]?.map((stock) => {
                                return (
                                <div key={stock.ticker}>
                                    <span>{stock.ticker}</span>
                                    <span>{stock.currentPrice}</span>
                                </div>
                                )
                            })}

                            <EditList id={watchlist.id} />
                            <button id={watchlist.id} onClick={deleteAList}>Delete</button>
                            </li>
                            )})}
                    </ul>


                </div>

            </div>
        </>
    )
}

export default Dashboard
