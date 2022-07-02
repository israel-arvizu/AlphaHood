const LOAD_LISTS = 'list/LOAD_LISTS'
const ADD_LIST = 'list/ADD_LIST'
const EDIT_LIST = 'list/EDIT_LIST'
const DELETE_LIST = 'list/DELETE_LIST'
const ADD_STOCK_TO_LIST = 'list/ADD_STOCK_TO_LIST'
const LOAD_STOCKS = '/list/LOAD_STOCKS'


const loadlists = (lists) => ({
    type: LOAD_LISTS,
    lists
})

const addlist = (list) => ({
    type: ADD_LIST,
    list
})


const addstocktolist = (stock) => ({
    type: ADD_STOCK_TO_LIST,
    payload: stock
})

const editlist = (list) => ({
    type: EDIT_LIST,
    list
})

const deletelist = (id) => ({
    type: DELETE_LIST,
    id
})



export const loadAllLists = (userId) => async (dispatch) => {
    const response = await fetch(`api/lists/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userId)
    })
    const data = await response.json()

    dispatch(loadlists(data))
    return response
}

export const addNewList = (list) => async (dispatch) => {
    const response = await fetch('/api/lists/new',
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(list)
        })

    const data = await response.json()
    dispatch(addlist(data));
    return response


}

export const deleteList = (id) => async (dispatch) => {
    const response = await fetch(`/api/lists/${id}/`,
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify("hello")

        })

    dispatch(deletelist(id))



}


export const editNewList = (id, name) => async (dispatch) => {
    const response = await fetch(`/api/lists/${id}/edit`,
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(name)
        })

    const data = await response.json()
    console.log("!@#!#", data)
    dispatch(editlist(data));
    return response

}

export const addstock = (stock) => async (dispatch) => {
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


export default function listsReducer(state = [], action) {
    let newState;
    switch (action.type) {
        case LOAD_LISTS:
            console.log(state)
            console.log(state.length)
            console.log(action.lists.watchlists)
            let newState = []
            if (state.length > 0) {
                console.log(state)
                state.forEach(list => {
                    console.log(list.id)
                    if (action.lists.watchlists) {
                        action.lists.watchlists.forEach(watchlist => {


                            if (list.id === watchlist.id) {
                               newState.push(watchlist)
                               console.log(newState)

                            }
                        })
                    }
                })
            }
            else if (state.length===0){
                return [...state, ...action.lists.watchlists]
            }

            return newState

        case ADD_LIST:
            return [...state, action.list]
        case ADD_STOCK_TO_LIST:
            return { ...state, lists: action.payload }
        case EDIT_LIST:
            state.map((list) => (
                list.id === action.list.id ? list.name = action.list.name : list.name
            ))
            return [...state]

        case DELETE_LIST:
            console.log(typeof (state[0].id))
            return state.filter(({ id }) => id !== Number(action.id))

        default:
            return state;
    }
}
