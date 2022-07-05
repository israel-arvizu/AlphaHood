const LOAD_NEWS = 'news/LOAD_NEWS';

//ACTIONS
const loadNews = (news) => ({
    type: LOAD_NEWS,
    payload: news
})

//THUNKERS
export const loadHomeNews = () => async (dispatch) => {
    const response = await fetch('/api/news/load')
    const data = await response.json();
    dispatch(loadNews(data));
    return response;
}

export const getNews = ticker => async (dispatch) => {
    const response = await fetch(`/api/news/${ticker}`)
    const data = await response.json();

    dispatch(loadNews(data));
    return response;


    // if (response.ok) {
    //     const data = await response.json()
    //     dispatch(loadNews(data))
    //     return response
    // }
}


//REDUCER
let initialState = {};
export default function newsReducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_NEWS:
            return { ...state, news: action.payload }
        default:
            return state;
    }
}
