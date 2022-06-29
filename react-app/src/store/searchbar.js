const GET_SEARCH_STOCKS = 'search/GET_SEARCH_STOCKS'

export const loadSearchStocks = (stocks) => {
    return {
        type: GET_SEARCH_STOCKS,
        payload: stocks
    }
}

export const searchStocks = () => async (dispatch) => {
    const res = await fetch('/api/search/')

    if (res.ok) {
        const data = await res.json()
        dispatch(loadSearchStocks(data))
    }
}


let initialState = { entries: {}, isLoading: true }

export default function searchReducer(state = initialState, action) {
    switch (action.type) {
        case GET_SEARCH_STOCKS:
            return { entries: action.stocks }
        default:
            return state;
    }
}
