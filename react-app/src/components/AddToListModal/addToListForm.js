import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addNewList } from "../../store/list"
import { loadStockList } from "../../store/liststock";
import './addButton.css'


const AddToList = ({ stock, closeModal }) => {
  const dispatch = useDispatch()

  const [errorMessages, setErrorMessages] = useState([])
  const listarray = new Set()
  let [sendArray, setSendArray] = useState([])
  let [deleteArray,setDeleteArray] = useState([])
  let [disableArray, setdisableArray] = useState([])
  let [disableArraylength, setDisableArraylength]=useState(disableArray.length)
  const [enteredWatch, setEnteredWatch] = useState(false)
  const watchlists = useSelector(state => state.lists).filter(watchlist=>watchlist.name!=="Portfolio")
  const liststocks = useSelector(state => state.listStockReducer.listStock)






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

  useEffect(()=>{

    setDisableArraylength(disableArray.length)

  }, [disableArray])

  const checkLists = async (e, id) => {

    let checked = document.getElementById(`check-${id}`)
    let submit = document.getElementById(`submitadd`)
    if(checked.checked && listarray.has(id)){


      deleteArray = deleteArray.filter(item=>{return item!= id})
    }
    if (!checked.checked && listarray.has(id)){
     let newarr = disableArray.filter(item=>{return item!= id})

      deleteArray.push(id)

    }

    if (checked.checked && !listarray.has(id)) {

      sendArray.push(id)

    }
    else if (!checked.checked) {
      sendArray = sendArray.filter(item => { return item != id })


    }
    else if (listarray.has(id) && !checked.checked){
      deleteArray.push(id)
    }


  }

  const watchlistsubmit = async (e) => {
    e.preventDefault()
    const payload = {
      "arrays": sendArray,
      "stockId": stock.id

    }
    const payload2={
      'arrays': deleteArray,
      "stockId":stock.id


    }
    const response = await fetch('/api/lists/addstock',
    {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    }).then().then(()=>fetch('/api/lists/deletestock',
    {
      method:"POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload2)
    }
    ))
    const data = await response.json()

    closeModal()


  }

  return (
    <div>
      <div className="addtolisttitle">Add to Your List</div>
      <div className="addtowatchlist">
        <form className="updatelists"
          onSubmit={watchlistsubmit}>

          {watchlists.map(watchlist => (



            <div className="listofwatchlists" key={watchlist.name}>


              <label className="watchlistnames">{watchlist.name}</label>
              <input type="checkbox" id={`check-${watchlist.id}`} className="checkboxwatch" onChange={(e) => checkLists(e, watchlist.id)} />
              <hr></hr>
              <br></br>
              {!!liststocks && document.getElementById(`check-${watchlist.id}`) && liststocks[watchlist.id].forEach(list => {

                if (list.ticker === stock.ticker) {
                  listarray.add(watchlist.id)
                  document.getElementById(`check-${watchlist.id}`).checked=true

                }
              })}
            </div>
            ))}
          <button id="submitadd" type="submit" >Update lists</button>
        </form>

      </div>
    </div>

  );

};

export default AddToList
