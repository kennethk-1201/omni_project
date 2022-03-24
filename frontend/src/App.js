import { useState } from "react";

import Axios from "axios";
import axios from "axios";

function App() {

  const [shortUrl, setShortUrl] = useState("");
  const [longUrl, setLongUrl] = useState("");

  const handleChange = e => {
    setLongUrl(e.target.value)
  }

  const sendRequest = async e => {
    e.preventDefault();
    
    try {
      const response = await Axios.post(`${process.env.REACT_APP_BACKEND}/urlshortener/add/`, longUrl);
      setShortUrl(response.data.short_url);

    } catch (e) {
      console.log(e.message);
    }
  }

  return (
    <div className="container">
      <h1>Enter URL:</h1>
      <form className="input-form" onSubmit={sendRequest}>
        <input type="text" className="url-input" value={longUrl} onChange={handleChange}/>
        <button type="submit">Submit</button>
      </form>
      <h1>{shortUrl}</h1>
    </div>
  );
}

export default App;
