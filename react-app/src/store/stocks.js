const LOAD_STOCKS = 'stocks/LOAD_STOCKS'
const GET_STOCK = 'stocks/GET_STOCK'
const BUY_STOCK = 'stocks/BUY_STOCK'
const LOAD_OWNED = 'stocks/LOAD_OWNED'

const loadstocks = (stocks) => ({
    type: LOAD_STOCKS,
    payload: stocks
})

const getStock = (stock) => ({
    type: GET_STOCK,
    payload: stock
})

const buyStock = (transaction) => ({
    type: BUY_STOCK,
    payload: transaction
})

const loadOwned = (stocks) => ({
    type: LOAD_OWNED,
    payload: stocks
})

// export const loadOwnedStocks = (id) => async (dispatch) => {
//     const response = await fetch(`/api/stocks/loadOwnedStocks/${id}`)
//     const data = await response.json()
//     dispatch(loadOwned(data))
//     return response
// }


export const purchaseStock = (ticker, transaction, type) => async (dispatch) => {
    const response = await fetch(`/api/stocks/${ticker}/${type}`,
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(transaction)
        })
    const data = await response.json()
    dispatch(buyStock(data))
}

export const loadstocklist = (list) => async (dispatch) => {
    const response = await fetch("/api/stocks/loadfeaturelists",
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(list)
        })
    const data = await response.json()
    dispatch(loadstocks(data));
    return response
}


export const getOneStock = (ticker) => async (dispatch) => {
    const response = await fetch(`/api/stocks/${ticker}`) //GRAB STOCK FROM DB

    if (response.ok) {
        const data = await response.json()
        dispatch(getStock(data))
    }
}


export const updateStock = (ticker) => async dispatch => {
    const response = await fetch(`/api/stocks/update/${ticker}`,
        {
            method: "POST"
        })
    if (response.ok) {
        const data = await response.json()
        dispatch(getStock(data))
    }
}

export const getStocks = () => async dispatch => {
    const response = await fetch(`/api/stocks/`)
    if (response.ok) {
        const stocks = await response.json()
        dispatch(loadstocks(stocks))
        return stocks
    }
}



let initialState = {};
export default function stocksReducer(state = initialState, action) {
    let newState;
    switch (action.type) {
        case LOAD_STOCKS:
            return { ...state, stocks: action.payload }
        case LOAD_OWNED:
            return { ...state, myPortfolio: action.payload }
        case GET_STOCK:
            newState = {...state}
            newState[action.payload.ticker] = action.payload
            return newState
        case BUY_STOCK:
            return { ...state }
        default:
            return state;
    }
}
