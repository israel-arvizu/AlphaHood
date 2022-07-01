import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { loadHomeNews } from '../../store/news'
import { addNewList, loadAllLists, deleteList } from '../../store/list';
import LineChart from '../../components/Linechart-Component/Linechart';
import EditListModal from '../EditListModal';
import EditList from '../EditListModal/EditListForm';
import { loadPortfolio, loadCurrentPortfolio } from '../../store/stocks';


function Dashboard() {
    const dispatch = useDispatch()
    const newsArticles = useSelector(state => state.newsReducer.news);
    const userId = useSelector(state=> state.session.user.id)
    const [watchlistName, setWatchlistName]=useState(false)
    const [newListName, setNewListName] = useState("")
    const [displayPort, setDisplayPort] = useState(0)
    const [updated, setUpdate] = useState(false)
    const [updateLog, setUpdateLog] = useState("Updating, One Sec!")
    const watchlists = useSelector(state=>state.lists)

    const user = useSelector(state => state.session.user);
    const portfolio = useSelector(state => state.stocks.portfolio);
    const currentPortfolio = useSelector(state => state.stocks.CurrentPortfolio)

    useEffect(() => {
        dispatch(loadAllLists(userId))
        dispatch(loadHomeNews())
        dispatch(loadPortfolio(user.id))
        dispatch(loadCurrentPortfolio(user.id))
    }, [dispatch])

    const deleteAList = async(e)=>{
        dispatch(deleteList(e.target.id))
        console.log(e.target.id)
        e.preventDefault()

    }
    const createlist = async(e)=>{
        e.preventDefault()
        const newlist = {
            name: newListName,
            userId: userId
        }


        const data = await dispatch(addNewList(newlist))
    }


    if (newsArticles === undefined || portfolio === undefined){
        return <h2>Loading</h2>
    }
    if(currentPortfolio !== undefined && !updated){
        let price = currentPortfolio
        setDisplayPort(price)
        setUpdate(true)
        setUpdateLog("")
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
                    <LineChart portfolio={portfolio}/>
                </div>
                <h2>Buying Power</h2>
                <h2>Trending Lists</h2>
                <div>
                    <button><a href='/trendinglists/top-hot-10'>Top Hot 10</a></button>
                    <button><a href='/trendinglists/creators-choice'>Creators Choice</a></button>
                    <button><a href='/trendinglists/25-most-popular'>25 Most Popular</a></button>
                    <button><a href='/trendinglists/technology'>Technology</a></button>
                    <button><a href='/trendinglists/automotive'>Automotive</a></button>

                </div>
                <h2>News</h2>
                {newsArticles.map((article) => {
                    if (article.thumbnail !== undefined)
                        return (
                            <div key={article.title}>
                                <hr></hr>
                                <a href={article.link}>
                                    <img src={article.thumbnail.resolutions[1].url} alt='thumbnail' />
                                    <a>{article.publisher}</a>
                                    <h3>{article.title}</h3>
                                </a>
                                <div>
                                    <p>{article.relatedTickers[0]}</p>
                                    <p>{article.relatedTickers[1]}</p>
                                </div>
                            </div>
                        )
                    return null
                })}
            </div>
            <div>
                WatchList
                <button onClick={()=>setWatchlistName(true)}>+</button>

                {watchlistName &&
                <div>
                    <form
                    onSubmit={createlist}>
                        <input name="listName"
                        type="text"
                        placeholder='Your list name'
                        value={newListName}
                        onChange={(e)=>setNewListName(e.target.value)}></input>
                        <button type="submit">Add List</button>

                    </form>

                </div>

                }

                <div>
                    <ul>
                        {!!watchlists.length &&
                        watchlists.map(watchlist=>(
                            <li>{watchlist.name}
                            <EditList id={watchlist.id} />
                            <button id={watchlist.id} onClick={deleteAList}>Delete</button>
                            </li>




                    ))}
                    </ul>


                </div>

            </div>
        </>
    )
}

export default Dashboard
