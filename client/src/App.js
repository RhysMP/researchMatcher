import logo from './logo.svg';
import './App.css';
import styled from 'styled-components';
import axios from 'axios';
import { useState } from 'react';

const Button = styled.button`
  display: flex;
  color: black;
  justify-content: center;
  align-items: center;
  all: unset;
  height: 200px;
  width: 200px;
  background-color: lightblue;
  cursor: pointer;
  border-radius: 20px;
`

function App() {
  const [uploaded, setUpload] = useState('Pending...')

  function buttonClick() {
    axios.get(`http://127.0.0.1:5000/students`, {
      headers: {
        'Content-Type': 'application/json',
        // Add any other required headers here
      }
    })
    .then(res => {
      const data = res.data;
      setUpload(JSON.stringify(data));
    })
    .catch(error => {
      console.error("Error fetching data:", error);
    });
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Click the button below to check!
        </p>
        <Button onClick={() => {buttonClick()}}>Click Me!</Button>
        <p>Data: {uploaded}</p>
      </header>
    </div>
  );
}

export default App;
