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
    axios.get(`https://jsonplaceholder.typicode.com/users`)
    .then(res => {
      const data = res.data;
      setUpload(JSON.stringify(data))
    })
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
