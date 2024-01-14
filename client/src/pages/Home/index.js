// Landing page
import styled from 'styled-components';
import axios from 'axios';
import Nav from '../../components/Navbar.js'
import { useState } from 'react';
import { FONT_SIZE } from '../../constants';
import landing from '../../landing.png';
import rick from '../../RickAstley.jpg';

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
`;

const Container = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  height: 100%;
  width: 1100px;
`;

const Title = styled.div`
  font-weight: 500;
  font-size: 32pt;
  color: black;
  text-shadow: 1px 1px 4px black;
  font-family: 'Inria Sans', sans-serif;
  margin-bottom: 20px;
  padding: 20px 0px;
`;

const WelcomeContent = styled.div`
  color: #5879D1;
  font-family: 'Inria Sans', sans-serif;
  border-top: 2px solid #5879D1;
  background-color: rgba(230,230,230,0.9);
  border-radius: 0px 0px 10px 10px;
  transform: translateX(-20px);
  padding: 10px 20px;
  font-size: ${FONT_SIZE.lg};
`;

const SubContainer = styled.div`
  display: flex;
  padding: 40px;
  width: 50%;
  height: calc(100% - 160px);
  border-radius: 10px;
  flex-direction: column;
  font-size: 14pt;
  font-family: 'Inria Sans', sans-serif;
`;

const InputField = styled.input`
  all: unset;
  margin-bottom: 20px;
  background-color: white;
  height: min-height;
  border-radius: 5px;
  padding: 10px;
  width: calc(100% - 20px);
`;

const FileUpload = styled.label`
  padding: 10px;
  border-radius: 10px;
  background-color: lightgreen;
  font-family: 'Inria Sans', sans-serif;
  cursor: pointer;
`;

const LabelPad = styled.div`
  height: 10px;
  width: 10px;
`;

const CustomInput = styled.input`
  display: none;
`;

const RegistrationText = styled.div`
  color: darkgray;
  width: min-content;
`;

const QR = styled.img`
  height: 170px;
  width: 170px;
`;

const ButtonContainer = styled.div`
  display: flex;
  justify-content: flex-end;
  width: 100%;
`;

const CreateAccount = styled.button`
  all: unset;
  background-color: #F67171;
  padding: 10px;
  border-radius: 10px;
  cursor: pointer;
`

// Sends input fields:
// - "name"
// - "major"
// - "email"

function Home() {
  const [file, setFile] = useState()
  const [submissionStatus, setStatus] = useState('');

  function handleChange(event) {
    setFile(event.target.files[0]);
    setStatus(' ✔️');
  }
  
  function handleSubmit(event) {
    event.preventDefault()
    const url = 'http://localhost:5000/uploadFile';
    const formData = new FormData();
    formData.append('file', file);
    formData.append('fileName', file.name);
    const config = {
      headers: {
        'content-type': 'multipart/form-data',
      },
    };
    axios.post(url, formData, config)
  }

  return (<div>
      <Nav></Nav>
      <form onSubmit={handleSubmit}>
      <Welcome>
        <Container>
          
          <SubContainer>
            <Title>Looking for research in academia?</Title>
            <WelcomeContent>Join our community of only 4 people nationwide</WelcomeContent>
          </SubContainer>
          
          <SubContainer style={{backgroundColor: 'rgba(230,230,230,0.9)'}}>
            <div style={{display: 'flex', height: '60%', width: '100%'}}>
              <div style={{width: '50%', height: '100%', marginRight: '40px'}}>
                  <InputField placeholder="First/Last Name" name="name" id="name" required/>
                  <InputField placeholder="Email" name="email" id="email" required/>
                  <InputField placeholder="Field of Study" name="major" id="major" required/>

                  <LabelPad />
                  <FileUpload for="resume-upload" type="file" onChange={handleChange}>
                    Upload a resume
                    {submissionStatus}
                  </FileUpload>
                  <LabelPad />
                  <CustomInput id="resume-upload" type="file" onChange={handleChange} required/>
              </div>
              <div style={{height: '87%', display: 'flex', flexDirection: 'column', alignItems: 'center', backgroundColor: 'white', flex: '1'}}>
                <QR src={rick}></QR>
                <RegistrationText>
                  Already&nbsp;<nobr/>Registered?
                  Download the App
                </RegistrationText>
              </div>
            </div>
            <div style={{color: 'rgba(0,0,0,0.7)',height: '40%', width: '100%'}}>
              <div>By submitting my number, I agree to a policy that I don't necessarily agree to.</div>
              <br/>
              <input type="checkbox"/><nobr/>I agree to get special offers about me being stupid
              <br/>
              <div style={{marginTop: '10px'}}>
                <input type="checkbox"/><nobr/>I agree to live awesomely to the best of my ability
              </div>
              <br/>
              <ButtonContainer>
                <CreateAccount type="submit">Create Account</CreateAccount>
              </ButtonContainer>
            </div>
          </SubContainer>
        </Container>
      </Welcome>
      </form>
    </div>)
}

export default Home;