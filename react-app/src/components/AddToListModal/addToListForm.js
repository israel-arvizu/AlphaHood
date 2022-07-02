import { useEffect, useState} from "react";
import { useDispatch, useSelector } from "react-redux";
import { addNewList} from "../../store/list"


const AddToList = ({closeModal}) => {
  const dispatch = useDispatch()

  const [errorMessages, setErrorMessages] = useState([])
  const lists = useSelector(state=>state.lists)

  console.log(lists)


  const handleSubmit = async (e) => {
    e.preventDefault();

    closeModal()
  };



  return (
  <div>
    <div className="edit-list-form">
      <ul>
      {lists.map(list=>(
        <li>{list.name}
        <button onClick>Add to this list</button>
        </li>


      ))}
      </ul>


      </div>
    </div>

  );

};

export default AddToList
