import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import AddToList from './addToListForm'

function AddToListModal() {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true) } id="editbuttonlist">Add to List</button>
      {console.log(showModal)}
      {showModal &&
      (<Modal onClose={() => setShowModal(false)}>
          <AddToList closeModal={() => setShowModal(false)}/>
        </Modal>
      )}
    </>
  );
}

export default AddToListModal;
