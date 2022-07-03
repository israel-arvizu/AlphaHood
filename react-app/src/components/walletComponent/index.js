import React, {useState} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import UserNavBar from '../UserNavBar';
import { add_to_balance } from '../../store/session';

function Wallet(){
    const dispatch = useDispatch()
    const history = useHistory()
    const [amount, setAmount] = useState(25);
    const userId = useSelector(state => state.session.user.id)

    function purchaseAmount(e) {
        e.preventDefault()
        dispatch(add_to_balance(userId, amount))
        history.push('/dashboard')
    }

    function setValue(e){
        setAmount(e.target.value)
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
                                <select value={amount} onChange={setValue}>
                                    <option value={25}>$25</option>
                                    <option value={50}>$50</option>
                                    <option value={100}>$100</option>
                                    <option value={500}>$500</option>
                                    <option value={1000}>$1000</option>
                                    <option value={2500}>$2500</option>
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
