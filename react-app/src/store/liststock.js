const LOAD_STOCKS = '/liststock/LOAD_STOCKS'


const loadstocks = (list)=>({
    type: LOAD_STOCKS,
    list
})


export const loadStocksforList = (userId) => async(dispatch)=>{
    const response = await fetch(`api/lists/stocks`,
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userId)
    })
    const data = await response.json()
    dispatch(loadstocks(data))
    return response
}

export default function listStockReducer(state = [], action) {
    let newState;
    switch (action.type) {
        case LOAD_STOCKS:
            return [...state, ...action.list.lists]

        default:
            return state;
    }
}
