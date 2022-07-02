import React, {useState} from 'react';
import UserNavBar from '.';

const Wallet = ({setShowModal, onClose}) => {
    const [amount, setAmount] = useState(0);

    function purchaseAmount() {
        return null;
    }

    return (
        <>
        <UserNavBar />
            <div>
                <div>
                    <h2>Add Money to Your Wallet!</h2>
                    <div>
                        <p>Please Select Amount from Below</p>
                    </div>
                    <div>
                        <form onSubmit={purchaseAmount}>
                            <div>
                                <label htmlFor='amount'>Amount</label>
                                <select
                                name='amount'
                                value={amount}
                                onChange={() => {setAmount()}}
                                >
                                    <option value={25}>$25</option>
                                    <option value={50}>$50</option>
                                    <option value={100}>$100</option>
                                    <option value={500}>$500</option>
                                </select>
                                <button type='submit'>Purchase</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Wallet
