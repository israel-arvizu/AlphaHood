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
  let [deleteArray,setDeleteArray] = useState([])
  let [disableArray, setdisableArray] = useState([])
  let [disableArraylength, setDisableArraylength]=useState(disableArray.length)
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

  useEffect(()=>{
    console.log(disableArray.length)
    setDisableArraylength(disableArray.length)
    console.log(disableArray.length)
  }, [disableArray])

  const checkLists = async (e, id) => {

    let checked = document.getElementById(`check-${id}`)
    let submit = document.getElementById(`submitadd`)
    if(checked.checked && listarray.has(id)){


      deleteArray = deleteArray.filter(item=>{return item!= id})
    }
    if (!checked.checked && listarray.has(id)){
      console.log(e.target.checked)

     let newarr = disableArray.filter(item=>{return item!= id})




      deleteArray.push(id)

    }

    if (checked.checked && !listarray.has(id)) {
      console.log(listarray)

      sendArray.push(id)
      console.log(sendArray)
    }
    else if (!checked.checked) {
      sendArray = sendArray.filter(item => { return item != id })
      console.log(sendArray)

    }
    else if (listarray.has(id) && !checked.checked){
      deleteArray.push(id)
    }

    console.log(deleteArray)
    console.log(sendArray)



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
    }).then(data=>console.log(data)).then(()=>fetch('/api/lists/deletestock',
    {
      method:"POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload2)
    }
    ))
    const data = await response.json()


    const deleteresponse = await fetch('/api/lists/deletestock',
    {
      method:"POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload2)
    }
    )
    const data2=await deleteresponse.json()

  }

  return (
    <div>
      <div className="watchlistform">
        <form
          onSubmit={watchlistsubmit}>

          {watchlists.map(watchlist => (

            <div>


              <label>{watchlist.name}</label>
              <input type="checkbox" id={`check-${watchlist.id}`} onChange={(e) => checkLists(e, watchlist.id)} />
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
