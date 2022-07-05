import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import AddToList from './addToListForm'
import './addButton.css'

function AddToListModal({ stock }) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className='add-to-list' onClick={() => setShowModal(true)} id="editbuttonlist">Add to List</button>

      {showModal &&
        (<Modal onClose={() => setShowModal(false)}>
          <AddToList stock={stock} closeModal={() => setShowModal(false)} />
        </Modal>
        )}
    </>
  );
}

export default AddToListModal;
