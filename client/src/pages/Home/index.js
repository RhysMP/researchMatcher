// Landing page
import styled from 'styled-components';
import Nav from '../../components/Navbar.js'
import landing from '../../landing.png';
import { useState } from 'react';
import axios from 'axios';
import { FONT_SIZE } from '../../constants';

const Welcome = styled.div`
  display: flex;
  background-image: url(${landing});
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  width: 100%;
  height: 600px;
  margin-top: 10px;
  align-items: center;
  justify-content: center;
`

const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 100%;
  width: 1100px;
`

const Title = styled.div`
  font-weight: 500;
  font-size: 32pt;
  color: black;
  text-shadow: 1px 1px 4px black;
  font-family: 'Inria Sans', sans-serif;
  margin-bottom: 40px;
  padding: 20px 0px;
`

const WelcomeContent = styled.div`
  color: #5879D1;
  font-family: 'Inria Sans', sans-serif;
  border-top: 2px solid #5879D1;
  background-color: rgba(220,220,220,0.9);
  border-radius: 0px 0px 10px 10px;
`

const SubContainer = styled.div`
  display: flex;
  padding: 40px;
  width: 50%;
  height: calc(100% - 160px);
  border-radius: 10px;
`

function Home() {
  const [file, setFile] = useState()

  function handleChange(event) {
    setFile(event.target.files[0])
  }
  
  function handleSubmit(event) {
    event.preventDefault()
    const url = 'http://localhost:3000/uploadFile';
    const formData = new FormData();
    formData.append('file', file);
    formData.append('fileName', file.name);
    const config = {
      headers: {
        'content-type': 'multipart/form-data',
      },
    };
    axios.post(url, formData, config).then((response) => {
      console.log(response.data);
    });

  }

  return (<div>
      <Nav></Nav>
      <Welcome>
        <Container>
          <SubContainer style={{flexDirection: 'column', padding: '20px 40px'}}>
            <Title>Looking for research in academia?</Title>
            <WelcomeContent>Join our community of only 4 people nationwide</WelcomeContent>
          </SubContainer>
          <SubContainer style={{backgroundColor: 'rgba(220,220,220,0.9)'}}>
            <form onSubmit={handleSubmit}>
              <h1>React File Upload</h1>
              <input type="file" onChange={handleChange}/>
              <button type="submit">Upload</button>
            </form>
          </SubContainer>
        </Container>
      </Welcome>
    </div>)
}

export default Home;