import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { Redirect } from 'react-router-dom';
import { loadHomeNews } from '../store/news';
import LineChart from './Linechart-Component/Linechart';


function Dashboard() {
    const dispatch = useDispatch()
    const newsArticles = useSelector(state => state.newsReducer.news);


    useEffect(() => {
        dispatch(loadHomeNews())
    }, [dispatch])

    if (newsArticles === undefined) return <h2>Loading</h2>
    // console.log(newsArticles[0].thumbnail.resolutions[2].url);
    return (
        <>
            <div>
                LeftSection
                <div>
                    <LineChart />
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
            </div>
        </>
    )
}

export default Dashboard
