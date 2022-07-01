import { useEffect, useState, useContext } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { editNewList} from "../../store/list"


const EditList = ({ id, closeModal}) => {
  const dispatch = useDispatch()
  const history = useHistory()
  const [errorMessages, setErrorMessages] = useState([])
  console.log(useSelector(state=>state.lists))
  const list = useSelector(state=>state.lists).filter(watchlist=>watchlist.id==id)
  console.log(list[0])
  console.log(id)
  const [name, setName] = useState(list[0].name)



  useEffect(()=>{
    const errors = []
    if (name.length < 1){
      errors.push('Name cannot be empty')}
      setErrorMessages(errors)
    }, [name])

  const updateName = (e) => setName(e.target.value);

  const handleSubmit = async (e) => {
    e.preventDefault();

    console.log(id)



    dispatch(editNewList(id, name))
    //closeModal()
  };



  return (
  <div>
    <div className="edit-list-form">
    <div className="errors">
          <ul>
            {errorMessages.map(error=>(
              <li>{error}</li>
            ))}
          </ul>
        </div>

      <form className="edit-watchlist" onSubmit={handleSubmit}>

        <label>Edit Playlist Name: </label>
        <input
        id = "editinput"
          type="text"
          placeholder="edit title"
          value={name}
          onChange={updateName}
        />

        <br></br>
        <br></br>



        <button type="submit" className="submiteditbutton" disabled={!!errorMessages.length}>Submit Edit</button>

      </form>
    </div>
  </div>
  );

};

export default EditList
