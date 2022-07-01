import React, { useState } from 'react';
import { Modal } from '../../context/Modal';
import EditList from './EditListForm'

function EditListModal({id}) {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true) } id="editbuttonlist">Edit</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditList id={id} closeModal={() => setShowModal(false)}/>
        </Modal>
      )}
    </>
  );
}

export default EditListModal;
