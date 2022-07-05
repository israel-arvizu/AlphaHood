import { useEffect, useState } from 'react'
import stockList from './data.json'
import './searchbar.css'
function SearchBar() {
    const [filteredData, setFilteredData] = useState([])
    const [entry, setEntry] = useState('')


    const inputChange = (e) => {
        const input = e.target.value
        setEntry(input)
        const filter = stockList.filter(value => {
            return value.name.toUpperCase().includes(input.toUpperCase()) || value.ticker.includes(input.toUpperCase())
        })

        if (input === "") {
            setFilteredData([])
        } else {
            setFilteredData(filter)
        }
    }


    return (
        <div className='search'>
            <div className='searchInputs'>
                <input
                    type='text'
                    placeholder='Search for stocks...'
                    value={entry}
                    onChange={e => inputChange(e)}
                ></input>
            </div>
            {filteredData.length != 0 && (
                <div className='dataResult'>
                    {filteredData.slice(0, 10).map(value => {
                        return (
                            <a key={value.ticker} className='dataItem' href={`/stocks/${value.ticker}`}>
                                <p>{value.ticker}  {value.name}</p>
                            </a>
                        )
                    })}
                </div>
            )}
        </div>
    )

}
export default SearchBar
