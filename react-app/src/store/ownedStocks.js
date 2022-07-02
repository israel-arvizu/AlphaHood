const LOAD_OWNED = 'stocks/LOAD_OWNED'

const loadOwned = (stocks) => ({
    type: LOAD_OWNED,
    payload: stocks
})

export const loadOwnedStocks = (id) => async (dispatch) => {
    const response = await fetch(`/api/stocks/loadOwnedStocks/${id}`)
    const data = await response.json()
    dispatch(loadOwned(data))
    return response
}



let initialState = {};
export default function owndedStocksReducer(state = initialState, action) {
    let newState;
    switch (action.type) {
        case LOAD_OWNED:
            return { ...state, myPortfolio: action.payload }
        default:
            return state;
    }
}
