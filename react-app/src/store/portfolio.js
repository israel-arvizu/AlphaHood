const LOAD_CURR_PORTFOLIO = 'stocks/LOAD_CURR_PORTFOLIO'
const LOAD_PORTFOLIO = 'stocks/LOAD_PORTFOLIO'

//ACTIONS
const loadcurrportfolio = (stocks) => ({
    type: LOAD_CURR_PORTFOLIO,
    payload: stocks
})

const loadportfolio = (stocks) => ({
    type: LOAD_PORTFOLIO,
    payload: stocks
})

export const loadCurrentPortfolio = (id) => async (dispatch) => {
    const response = await fetch(`/api/stocks/getportfolio/${id}`);
    const data = await response.json()
    dispatch(loadcurrportfolio(data));
    return response
}

export const loadPortfolio = (id) => async (dispatch) => {
    const response = await fetch(`/api/stocks/loadportfolio/${id}`);
    const data = await response.json()
    dispatch(loadportfolio(data));
    return response
}

let initialState = {};
export default function portfolioReducer(state = initialState, action) {
    let newState;
    switch (action.type) {
        case LOAD_PORTFOLIO:
            return { ...state, portfolio: action.payload }
        case LOAD_CURR_PORTFOLIO:
            newState = { ...state }
            newState["CurrentPortfolio"] = action.payload
            return newState
        default:
            return state;
    }
}
