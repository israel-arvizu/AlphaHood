const LOAD_STOCKS = 'stocks/LOAD_STOCKS'
const LOAD_PORTFOLIO = 'stocks/LOAD_PORTFOLIO'

const loadstocks = (stocks) => ({
    type: LOAD_STOCKS,
    payload: stocks
})

const loadportfolio = (stocks) => ({
    type: LOAD_PORTFOLIO,
    payload: stocks
})

//LOAD FEATUTURED LIST STOCKS
export const loadstocklist = (list) => async(dispatch)=>{
    const response = await fetch("/api/stock/loadfeaturelists",
        {
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify(list)
        })
    const data = await response.json()
    dispatch(loadstocks(data));
    return response
}

//GETS USERS POTFOLIO STOCKS
export const loadPortfolio = (id) => async(dispatch) =>{
    const response = await fetch(`/api/stock/loadportfolio/${id}`);
    const data = await response.json()
    dispatch(loadportfolio(data));
    return response
}

let initialState = {};
export default function stocksReducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_STOCKS:
            return {...state, stocks : action.payload}
        case LOAD_PORTFOLIO:
            return {...state, portfolio: action.payload}
        default:
            return state;
    }
}
