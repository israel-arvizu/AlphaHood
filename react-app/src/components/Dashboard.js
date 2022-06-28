import {useEffect} from 'react'
import {useDispatch, useSelector} from 'react-redux'
import { loadHomeNews } from '../store/news';


function Dashboard() {
    const dispatch = useDispatch()
    const newsArticles = useSelector(state => state.newsReducer.news);
    useEffect(() => {
        dispatch(loadHomeNews())
    }, [dispatch])

    if(newsArticles === undefined) return <h2>Loading</h2>
    // console.log(newsArticles[0].thumbnail.resolutions[2].url);
    return(
        <>
            <div>
                LeftSection
                <h2>Portfolion Graph</h2>
                <h2>Buying Power</h2>
                <h2>Trending Lists</h2>
                    <div>

                    </div>
                <h2>News</h2>
                {newsArticles.map((article) => {
                    if(article.thumbnail !== undefined)
                        return (
                            <div>
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
