import { useState } from "react";

import Axios from "axios";

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
      <form className="input-form" onSubmit={sendRequest}>
        <h1 className="app-title">Shorten a URL</h1>
        <input type="text" className="url-input" value={longUrl} onChange={handleChange}/>
        <button type="submit" className="submit-url">Submit</button>
        {shortUrl && (
          <>
            <p className="new-link-title">Your new URL:</p>
            <a className="new-link" href={`${process.env.REACT_APP_HOST}/${shortUrl}`}>{`${process.env.REACT_APP_HOST}/${shortUrl}`}</a>
          </>
        )}
      </form>
    </div>
  );
}

export default App;
