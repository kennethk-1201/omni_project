import { useEffect } from "react";

import {
    useParams,
} from "react-router-dom";

import Axios from "axios";

const RedirectComponent = props => {
    let { slug } = useParams();


    useEffect(() => {
        const getUrl = async () => {
            try {
                const response = await Axios.get(`${process.env.REACT_APP_BACKEND}/urlshortener/get/${slug}`);
                if (response.data) {
                    window.location.assign(response.data);
                } else {
                    window.location.assign(process.env.REACT_APP_HOST);
                }
            } catch (e) {
                window.location.assign(process.env.REACT_APP_HOST);
            }
            
        }
        getUrl();
        // eslint-disable-next-line
    }, [])

    return (
        <div className="redirect-container">
            <div class="lds-ellipsis"><div></div><div></div><div></div><div></div></div>
        </div>
    )
}

export default RedirectComponent