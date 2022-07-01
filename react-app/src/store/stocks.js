const LOAD_STOCKS = 'stocks/LOAD_STOCKS'
const GET_STOCK = 'stocks/GET_STOCK'
const LOAD_SEARCH_STOCK = 'stocks/LOAD_SEARCH_STOCK'

const loadstocks = (stocks) => ({
    type: LOAD_STOCKS,
    payload: stocks
})

const getStock = (stock) => ({
    type: GET_STOCK,
    payload: stock
})

const loadSearchStock = (stock) => {
    return {
        type: LOAD_SEARCH_STOCK,
        payload: stock
    }
}

export const getOneSearchStock = (ticker) => async (dispatch) => {
    const res = await fetch(`api/stocks/${ticker}`)

    const stock = await res.json()
    dispatch(loadSearchStock)
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
    const data = await response.json()
    dispatch(getStock(data))
    //check time for market open
    const updateStock = await fetch(`/api/stocks/update/${ticker}`,
        {
            method: "POST"
        })
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
            const allStocks = []
            action.stocks.forEach(stock => {
                allStocks[stock.id] = stock
            })
            return allStocks
        case GET_STOCK:
            newState = {}
            newState[action.payload.ticker] = action.payload
            return newState
        // return { ...state, stock: action.payload }
        default:
            return state;
    }
}
