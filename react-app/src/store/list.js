const LOAD_LISTS = 'list/LOAD_LISTS'
const ADD_LIST = 'list/ADD_LIST'
const ADD_STOCK_TO_LIST = 'list/ADD_STOCK_TO_LIST'


const loadlists = (lists)=>({
    type: LOAD_LISTS,
    payload: lists
})

const addlist=(list)=>({
    type: ADD_LIST,
    payload: list
})

const addstocktolist=(stock)=>({
    type:ADD_STOCK_TO_LIST,
    payload: stock
})


export const addNewList = (list) => async(dispatch)=>{
    const response=await fetch('/api/lists/new',
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(list)
    })

    const data = await response.json()
    dispatch(addlist(data));
    return response

}

export const addstock = (stock) => async(dispatch)=>{
    const response = await fetch('api/lists/addstock',
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(stock)
    })
    const data = await response.json()
    dispatch(addstocktolist(data));
    return response

}


export default function listsReducer(state = {}, action) {
    let newState;
    switch (action.type) {
        case LOAD_LISTS:
            return {...state, lists : action.payload}
        case ADD_LIST:
            return {...state, lists: action.payload}
        case ADD_STOCK_TO_LIST:
            return {...state, lists: action.payload}
        default:
            return state;
    }
}
