import React, {useState} from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import UserNavBar from '../UserNavBar';
import { add_to_balance } from '../../store/session';
import './wallet.css'

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
        <div className='bottom-body-container'>
            <div className='money-wallet-container'>
                <div id='money-wallet-header'>
                    <p className='money-wallet-text'>Add Money to Your Wallet!</p>
                </div>
                <div className='money-wallet-bottom-container'>
                    <p className='money-wallet-bottom-text'>Please Select Amount from Below</p>
                </div>
                <div>
                    <form onSubmit={purchaseAmount}>
                        <div id='wallet-form-container'>
                            <div id='wallet-form-input-container'>
                                <label htmlFor='amount' id='money-amount-label'>Amount</label>
                                <select  id='money-amount-select-table' value={amount} onChange={setValue}>
                                    <option value={25}>$25</option>
                                    <option value={50}>$50</option>
                                    <option value={100}>$100</option>
                                    <option value={500}>$500</option>
                                    <option value={1000}>$1000</option>
                                    <option value={2500}>$2500</option>
                                </select>
                            </div>
                            <button id='wallet-submit-button' type='submit'>Purchase</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        </>
    )
}

export default Wallet
