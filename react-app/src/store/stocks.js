const LOAD_STOCKS = 'stocks/LOAD_STOCKS'
const LOAD_PORTFOLIO = 'stocks/LOAD_PORTFOLIO'
const LOAD_CURR_PORTFOLIO = 'stocks/LOAD_CURR_PORTFOLIO'
const GET_STOCK = 'stocks/GET_STOCK'

const loadstocks = (stocks) => ({
    type: LOAD_STOCKS,
    payload: stocks
})

const loadcurrportfolio = (stocks) => ({
    type: LOAD_CURR_PORTFOLIO,
    payload: stocks
})

const loadportfolio = (stocks) => ({
    type: LOAD_PORTFOLIO,
    payload: stocks
})

const getStock = (stock) => ({
    type: GET_STOCK,
    payload: stock
})


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

export const loadCurrentPortfolio = (id) => async(dispatch) =>{
    const response = await fetch(`/api/stocks/getportfolio/${id}`);
    const data = await response.json()
    dispatch(loadcurrportfolio(data));
    return response
}

//GETS USERS POTFOLIO STOCKS
export const loadPortfolio = (id) => async(dispatch) =>{
    const response = await fetch(`/api/stocks/loadportfolio/${id}`);
    const data = await response.json()
    dispatch(loadportfolio(data));
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
            return {...state, stocks : action.payload}
        case LOAD_PORTFOLIO:
            return {...state, portfolio: action.payload}
        case LOAD_CURR_PORTFOLIO:
            newState = {...state}
            newState["CurrentPortfolio"] = action.payload
            return newState
        case GET_STOCK:
            newState = {}
            newState[action.payload.ticker] = action.payload
            return newState
        // return { ...state, stock: action.payload }
        default:
            return state;
    }
}
