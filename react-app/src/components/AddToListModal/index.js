import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import AddToList from './addToListForm'

function AddToListModal({stock}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true) } id="editbuttonlist">Add to List</button>
      {console.log(showModal)}
      {showModal &&
      (<Modal onClose={() => setShowModal(false)}>
          <AddToList stock={stock} closeModal={() => setShowModal(false)}/>
        </Modal>
      )}
    </>
  );
}

export default AddToListModal;
