const LOAD_STOCKS = 'stocks/LOAD_STOCKS'
<<<<<<< HEAD
const GET_STOCK = 'stocks/GET_STOCK'
=======
const LOAD_PORTFOLIO = 'stocks/LOAD_PORTFOLIO'
>>>>>>> origin/portfolioUpdates

const loadstocks = (stocks) => ({
    type: LOAD_STOCKS,
    payload: stocks
})

<<<<<<< HEAD
const getStock = (stock) => ({
    type: GET_STOCK,
    payload: stock
})


export const loadstocklist = (list) => async (dispatch) => {
    const response = await fetch("/api/stocks/loadfeaturelists",
=======
const loadportfolio = (stocks) => ({
    type: LOAD_PORTFOLIO,
    payload: stocks
})

//LOAD FEATUTURED LIST STOCKS
export const loadstocklist = (list) => async(dispatch)=>{
    const response = await fetch("/api/stock/loadfeaturelists",
>>>>>>> origin/portfolioUpdates
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(list)
        })
    const data = await response.json()
    dispatch(loadstocks(data));
    return response
}

<<<<<<< HEAD
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

=======
//GETS USERS POTFOLIO STOCKS
export const loadPortfolio = (id) => async(dispatch) =>{
    const response = await fetch(`/api/stock/loadportfolio/${id}`);
    const data = await response.json()
    dispatch(loadportfolio(data));
    return response
}
>>>>>>> origin/portfolioUpdates

let initialState = {};
export default function stocksReducer(state = initialState, action) {
    let newState;
    switch (action.type) {
        case LOAD_STOCKS:
<<<<<<< HEAD
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
=======
            return {...state, stocks : action.payload}
        case LOAD_PORTFOLIO:
            return {...state, portfolio: action.payload}
>>>>>>> origin/portfolioUpdates
        default:
            return state;
    }
}
