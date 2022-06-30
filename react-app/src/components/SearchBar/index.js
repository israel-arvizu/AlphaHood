import React, { useEffect, useState } from 'react'
import { useSelector, useDispatch } from "react-redux"
import { useHistory } from 'react-router-dom'
import { searchStocks } from '../../store/searchbar'
import { getOneStock, getStocks } from '../../store/stocks'
import './SearchBar.css'

function SearchBar() {
    const dispatch = useDispatch()
    const history = useHistory();
    const stocks = useSelector(state => state?.search?.entries);

    const searchTickers = stocks.searched_stocks?.map(stock => stock['ticker'])
    const searchNames = stocks.searched_stocks?.map(stock => stock['name'])

    const stockResults = searchTickers?.map((ticker, name) => {
        return `${ticker}: ${searchNames[name]}`
    })

    const [searchStock, setSearchStock] = useState('');
    const [searchResults, setSearchResults] = useState([])

    useEffect((() => {

        const searchBarResults = stockResults?.filter(name => name.toUpperCase().includes(searchStock.toUpperCase()));
        setSearchResults(searchBarResults)




        return (
            <input
                type='text'
                name='search-bar-nav'
                placeholder='Search Stocks Here...'
                onChange={ (e) => }
            ></input>
        )



    }
