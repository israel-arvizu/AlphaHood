const SEARCH_STOCKS = 'search/SEARCH_STOCKS'

export const getSearchedStocks = (stocks) => {
    return {
        type: SEARCH_STOCKS,
        payload: stocks
    }
}

export const searchStocks = () => async (dispatch) => {
    const response = await fetch('/api/search/')

    if (response.ok) {
        const data = await response.json()

        dispatch(getSearchedStocks(data))
    }
}

let initialState = { entries: {}, isLoading: true }

export default function searchReducer(state = initialState, action) {
    switch (action.type) {
        case SEARCH_STOCKS:
            return {
                entries: action.payload
            }
        default:
            return state;
    }
}
