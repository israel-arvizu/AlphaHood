import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router";
import LogoutButton from '../auth/LogoutButton';
import { useListModal } from "../../context/ListModal";
import { Modal } from "../../context/Modal"
import { loadOwnedStocks } from "../../store/ownedStocks";


const UserAccountNav = () => {
    const { bool, setBool } = useListModal();
    const user = useSelector((state) => state.session.user)
    const myPortfolio = useSelector((state) => state.stocks.CurrentPortfolio)

    const [amount, setAmount] = useState(0);

    const dispatch = useDispatch();
    const history = useHistory();


    if (myPortfolio === undefined) {
        return <h2>Loading Balance and Investments</h2>
    }


    return (
        <>
            <div className="account-name">{ user?.username }</div>
            <div className="portfolio-details">
                <div className="portfolio-info">
                    <h3 className="account-value">{ myPortfolio.toLocaleString("en-US") }</h3>
                    <div className="portfolio-value">Total Investments</div>
                </div>
                <div className="avail-cash">
                    <h3 className="account-value">{ user?.balance.toLocaleString("en-US") }</h3>
                    <div className="portfolio-value">Available Balance</div>
                </div>
            </div>
            <div className="account-links">
                <div
                    className="account-link"
                    onClick={ () => {
                        document.querySelector(".account-dropdown").classList.add("hidden");
                        setBool(true)
                    } }
                >
                    <div className="acc-logout"><LogoutButton /></div>
                </div>
            </div>
        </>




    )


}
export default UserAccountNav;
