const LOAD_STOCKS = 'liststock/LOAD_STOCKS'


const loadstocks = (list)=>({
    type: LOAD_STOCKS,
    list
})


export const loadStockList = (watchlistIds) => async(dispatch)=>{
    const response = await fetch(`/api/lists/stocks`,
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(watchlistIds)
    })
    const data = await response.json()
    console.log(data)
    dispatch(loadstocks(data))
    return response
}

export default function listStockReducer(state = {}, action) {
    let newState;
    switch (action.type) {
        case LOAD_STOCKS:
            newState = {...state, listStock: action.list}
            return newState;
        default:
            return state;
    }
}
