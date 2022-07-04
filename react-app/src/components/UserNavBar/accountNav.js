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

    const [amount, setAmount] = useState(0);

    const dispatch = useDispatch();
    const history = useHistory();



    return (
        <>
            <div className="acc-username">{ user?.username }</div>
            <div className="acc-balance">{ user?.balance }</div>
            <div className="acc-logout"><LogoutButton /></div>
            <div className="acc-links" onClick={ () => {
                document.querySelector(".account-dropdown").classList.add("hidden");
                setBool(true)
            } }>

            </div>
        </>




    )


}
export default UserAccountNav;
