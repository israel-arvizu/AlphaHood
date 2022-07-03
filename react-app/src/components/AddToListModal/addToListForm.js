import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addNewList } from "../../store/list"
import { loadStockList } from "../../store/liststock";
import './addtolist.css'


const AddToList = ({ stock, closeModal }) => {
  const dispatch = useDispatch()

  const [errorMessages, setErrorMessages] = useState([])
  const listarray = new Set()
  let [sendArray, setSendArray] = useState([])
  const [enteredWatch, setEnteredWatch] = useState(false)
  const watchlists = useSelector(state => state.lists)
  const liststocks = useSelector(state => state.listStockReducer.listStock)


  console.log(liststocks)
  console.log(stock.ticker)



  const handleSubmit = async (e) => {
    e.preventDefault();

    closeModal()
  };

  if (watchlists && watchlists.length > 0 && !enteredWatch) {
    let watchListIds = []
    watchlists.map((list) => {
      watchListIds.push(list.id)
    })
    dispatch(loadStockList(watchListIds))
    setEnteredWatch(true)
  }

  const checkLists = (id) => {
    let checked = document.getElementById(`check-${id}`)

    if (checked.checked && !listarray.has(id)) {
      console.log(listarray)

      sendArray.push(id)
      console.log(sendArray)
    }
    else if (!checked.checked) {
      sendArray = sendArray.filter(item => { return item != id })
      console.log(sendArray)

    }


  }

  const watchlistsubmit = async (e) => {
    e.preventDefault()
    const payload = {
      "arrays": sendArray,
      "stockId": stock.id

    }
    const response = await fetch('/api/lists/addstock',
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    })
    const data = await response.json()

  }

  return (
    <div>
      <div className="watchlistform">
        <form
          onSubmit={watchlistsubmit}>

          {watchlists.map(watchlist => (

            <div>


              <label>{watchlist.name}</label>
              <input type="checkbox" id={`check-${watchlist.id}`} onClick={() => checkLists(watchlist.id)} />
              {!!liststocks && document.getElementById(`check-${watchlist.id}`) && liststocks[watchlist.id].forEach(list => {

                if (list.ticker === stock.ticker) {
                  listarray.add(watchlist.id)

                  document.getElementById(`check-${watchlist.id}`).checked = true
                }
              })}



              <button onClick>Add to this list</button>
            </div>




          ))}
          <button type="submit">Update lists</button>
        </form>



      </div>
    </div>

  );

};

export default AddToList
