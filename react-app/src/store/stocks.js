const LOAD_STOCKS = 'stocks/LOAD_STOCKS'


const loadstocks = (stocks) => ({
    type: LOAD_STOCKS,
    payload: stocks
})


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


let initialState = {};
export default function stocksReducer(state = initialState, action) {
    switch (action.type) {
        case LOAD_STOCKS:
            return {...state, stocks : action.payload}
        default:
            return state;
    }
}
