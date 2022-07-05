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
    const myPortfolio = useSelector((state) => state.portfolio.CurrentPortfolio)
    const stocks = useSelector((state) => state.stocks)

    const [amount, setAmount] = useState(0);

    const dispatch = useDispatch();
    const history = useHistory();


    if (myPortfolio === undefined) {
        return <h2>Loading Balance and Investments</h2>
    }


    return (
        <>
            <div className="account-name"><div id="account-user-name"></div>{ user?.username }</div>
            <div className="portfolio-details">
                <div className="portfolio-info">
                    <h3 className="account-value"><span className="investments-name">Total Investments:</span> ${ myPortfolio.value.toLocaleString("en-US") }</h3>
                    <div className="portfolio-value"></div>
                </div>
                <div className="avail-cash">
                    <h3 className="account-value"><span className="investments-name2"> Available Balance: </span> <span className="test-test"> ${ user?.balance.toLocaleString("en-US") }</span></h3>
                    <div className="portfolio-value"></div>
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
