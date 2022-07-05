import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, useHistory } from 'react-router-dom';
import { login } from '../store/session';
import { loadAllLists } from '../store/list';
import { loadStockList } from '../store/liststock';
import { loadCurrentPortfolio, loadPortfolio } from '../store/portfolio';



export default function Loading () {
    const dispatch = useDispatch()
    const history = useHistory()
    const user = useSelector(state => state.session.user);
    const watchlists = useSelector(state=>state.lists)
    const [enteredWatch, setEnteredWatch] = useState(false)
    useEffect(() => {
        dispatch(loadAllLists(user.id))
        dispatch(loadPortfolio(user.id))
        dispatch(loadCurrentPortfolio(user.id))
    }, [dispatch])

    if(watchlists && watchlists.length > 0 && !enteredWatch){
        let watchListIds = []
        watchlists.map((list) => {
            watchListIds.push(list.id)
        })
        dispatch(loadStockList(watchListIds))



        setEnteredWatch(true)
    }
    const liststocks = useSelector(state=>state.listStockReducer.listStock)
    window.location.reload()

    if (liststocks)(


        history.push('/dashboard')

    )


    return (
        <div><img src="https://c.tenor.com/FBeNVFjn-EkAAAAC/ben-redblock-loading.gif" height="200" width="200"></img></div>
    )


}
