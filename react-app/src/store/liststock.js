const LOAD_STOCKS = 'liststock/LOAD_STOCKS'
const STOCK_CHART = 'stocks/STOCK_CHART'


const loadstocks = (list)=>({
    type: LOAD_STOCKS,
    list
})

const loadChart = (data) => ({
    type: STOCK_CHART,
    payload: data
})

export const loadStockList = (watchlistIds) => async(dispatch)=>{
    const response = await fetch(`/api/lists/stocks`,
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(watchlistIds)
    })
    const data = await response.json()
    dispatch(loadstocks(data))
    return response
}

export const stockChartHistory = (ticker) => async (dispatch) => {
    const response = await fetch(`/api/stocks/chart/${ticker}`)

    if (response.ok) {
        const data = await response.json()
        dispatch(loadChart(data))
    }
}

export default function listStockReducer(state = {}, action) {
    let newState;
    switch (action.type) {
        case LOAD_STOCKS:
            newState = {...state, listStock: action.list}
            return newState;
        case STOCK_CHART:
                return {...state, chartHistory: action.payload }
        default:
            return state;
    }
}
