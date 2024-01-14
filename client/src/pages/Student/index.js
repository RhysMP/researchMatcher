import styled from 'styled-components';
import Nav from '../../components/Navbar.js';
import { FONT_SIZE } from '../../constants';
import whiteabstract from '../../whitewaves.jpg';
import back from '../../back.png';
import { useState } from 'react';
import { useLocation } from 'react-router-dom';
import oldman from './oldman.jpg';

const Container = styled.div`
  display: flex;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-image: url(${whiteabstract});
  width: 100%;
  height: calc(100vh - 60px);
  overflow: hidden;
`;

const LeftPanel = styled.div`
  background-color: #8FA8E9;
  width: 300px;
  border-radius: 20px;
`;

const LeftPanelCover = styled.div`
  display: flex;
  flex-direction: column;
  background-color: #EBF0FB;
  height: calc(100% - 40px);
  width: calc(100% - 60px);
  padding: 20px;
  overflow-y: auto;
  scrollbar-width: none;
  font-family: 'Inria Sans', sans-serif;
`;

const MatchContainer = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-family: 'Inria Sans', sans-serif;
  flex: 1;
`;

const ProfessorContainer = styled.div`
  background-color: #C8E4FF;
  width: 450px;
  height: 500px;
  padding: 40px;
  border-radius: 10px;
`;

const Name = styled.div`
  color: black;
  font-size: ${FONT_SIZE.xl};
  margin-bottom: 10px;
`;

const Image = styled.div`
  width: 250px;
  height: 250px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-image: url(${oldman});
`;

const Subtitle = styled.div`
  font-size: ${FONT_SIZE.lg};
`;

const Description = styled.div`
  font-size: ${FONT_SIZE.sm};
`;

const MatchScore = styled.div`
  font-size: ${FONT_SIZE.xl};
`;

const Person = styled.div`
  display: flex;
  flex-direction: row;
  align-items: center;
  width: 100%;
  height: 60px;
  padding: 5px 0px;
  background-color: rgba(255,255,255,0.9);
  border-radius: 5px;
  margin-bottom: 10px;
  cursor: pointer;
  &:hover {
    background-color: rgba(255,255,255,0.5);
  }
`;

const ProfilePic = styled.div`
  margin: 0px 15px;
  border-radius: 100px;
  width: 50px;
  height: 50px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-image: url(${oldman});
`;

const ProfileName = styled.div`
  font-weight: bolder;
  font-family: 'Inria Sans', sans-serif;
`;

const RedDot = styled.div`
  height: 10px;
  width: 10px;
  background-color: red;
  border-radius: 100px;
  float: right;
  transform: translateX(-200%);
`

const Connect = styled.div`
  font-weight: bolder;
  font-family: 'Inria Sans', sans-serif;
  border-radius: 10px;
  background-color: lightgreen;
  width: min-content;
  padding: 10px 20px;
  transform: translateY(calc(-100% - 20px));
  cursor: pointer;

  &:hover {
    transform: scale(1.03, 1.03) translateY(calc(-100% - 18px));
  }
`;

const Swipe = styled.div`
  background-color: #F67171;
  border: solid 5px #F67171;
  width: 25px;
  height: 25px;
  margin-left: auto;
  border-radius: 5px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-image: url(${back});
  cursor: pointer;

  &:hover {
    background-color: #F6717166;
    border: solid 5px #F6717166;
  }
`;

function limitCharacters(str, limit) {
  if (typeof str !== 'string' || typeof limit !== 'number') {
    console.error('Invalid input. Please provide a valid string and a numeric limit.');
    return str;
  }

  if (str.length <= limit) {
    return str;
  } else {
    return str.slice(0, limit) + '...';
  }
}

function loadKeywords(arr) {
  let keys = [];
  for (let i = 0; i < arr.length; i++) {
    if (i >= 4) {
      break;
    }

    keys.push(<div>
      • {arr[i]}
    </div>);
  }
  return keys;
}

// The Student Dashboard
function Student() {
  const [professors, setProfessors] = useState([{"name": "Jimmy O' Yang"}, {"name": "Sigma the Ligma"}, {"name": "Johnson Stockton"}, {"name": "Rhys Panopio"}, {"name": "Kaan Koc"}, {"name": "Mario Tapia"}, {"name": "Yasir White"}, {"name": "Jimmy O' Yang"}, {"name": "Sigma the Ligma"}, {"name": "Johnson Stockton"}, {"name": "Rhys Panopio"}, {"name": "Kaan Koc"}, {"name": "Mario Tapia"}, {"name": "Yasir White"}, {"name": "Jimmy O' Yang"}, {"name": "Sigma the Ligma"}, {"name": "Johnson Stockton"}, {"name": "Rhys Panopio"}, {"name": "Kaan Koc"}, {"name": "Mario Tapia"}, {"name": "Yasir White"}]);
  const [percent, setPercent] = useState(79);
  const [abstract, setAbstract] = useState("This paper shows how Long Short-term Memory recurrent neural networks can be used to generate complex sequences with long-range structure, simply by predicting one data point at a time. The approach is demonstrated for text (where the data are discrete) and online handwriting (where the data are real-valued). It is then extended to handwriting synthesis by allowing the network...");
  const [profName, setProfName] = useState("Jimmy O' Yang");
  const location = useLocation();
  const { data } = location.state || {};
  const [loaded, setLoaded] = useState(false)
 
  if (!loaded) {
    setProfessors(data["professors"]);
    setLoaded(true);
    let best = getBestMatch(data["professors"]);
    console.log(JSON.stringify(best))
    setPercent(best.similarity_score);
    setAbstract(best.abstract);
    setProfName(best.fname + " " + best.lname);
  }

  function getBestMatch(profs) {
    let best = {"similarity_score": 0};
    for (let i = 0; i < profs.length; i++) {
      if (profs[i] == undefined) {
        continue;
      }
      if (profs[i].similarity_score > best.similarity_score) {
        best = profs[i];
      }
    }
    return best;
  }

  function swipe(name) {
    for (let i = 0; i < professors.length; i++) {
      if (professors[i].fname + " " + professors[i].lname == name) {
        // Delete from the DOM
        let proflist = document.getElementById("ProfList");
        for (const child of proflist.children) {
          if (child.getAttribute('key') == name) {
            child.remove();
          }
        }
        // Delete from the table
        delete professors[i];
        break;
      }
    }

    // Find the next best professor, load their data.
    let best = getBestMatch(professors);
    setPercent(best.similarityscore);
    setAbstract(best.abstract);
    setProfName(best.name);
  }

  function clickMessage(target, prof) {
    setProfName(prof.fname + " " + prof.lname);
    setAbstract(prof.abstract);
    setPercent((prof.similarity_score * 100))

    for (const child of target.children) {
      if (child.getAttribute('value') === "reddot") {
        child.style="display: none;"
      }
    }
  }

  function ListProfessors(arr) {
    let Professors = [];
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] == undefined) {
        continue;
      }
      let name = arr[i].fname + " " + arr[i].lname;
      let prof = (<Person key={name} onClick={(e)=>{clickMessage(e.target, arr[i])}}>
        <ProfilePic onClick={(e)=>{clickMessage(e.target.parentElement, arr[i])}}/>
        <RedDot value="reddot"/>
        <ProfileName onClick={(e)=>{clickMessage(e.target.parentElement, arr[i])}}>{name}</ProfileName>
      </Person>)
      Professors.push(prof);
    }
    return Professors;
  }

  return (
    <div>
      <Nav/>
      <Container>
        <LeftPanel>
          <LeftPanelCover id="ProfList">
            <div style={{fontWeight: 'bolder', fontSize: FONT_SIZE.base, marginBottom: '10px'}}>Matches</div>
            {ListProfessors(professors)}
          </LeftPanelCover>
        </LeftPanel>
        <MatchContainer>
          <ProfessorContainer>
            <div style={{display: 'flex', flexDirection: 'row', width: '100%'}}>
              <Name>{profName}</Name>
              <Swipe onClick={(e)=>{swipe(profName)}}></Swipe>
            </div>
            <div style={{display: 'flex', flexDirection: 'row'}}>
              <Image/>
              <Description style={{marginLeft: '20px', flex: 1}}>
                <MatchScore>
                  {Math.round(percent*1.25)}%
                  <br/>
                  Match
                </MatchScore>
                <div style={{marginTop: '40px'}}>
                  Keywords:
                  <br></br>
                  {loadKeywords(["Quantum Computing", "Deep Learning", "Machine Learning", "Neural Netorks"])}
                </div>
              </Description>
            </div>
            
            <Description>
              <Subtitle style={{marginTop: '20px'}}>
                Research Preview:
              </Subtitle>
              {limitCharacters(abstract, 370)}
            </Description>
          </ProfessorContainer>
          <ProfessorContainer style={{display: 'flex', justifyContent: 'flex-end', height: 'min-content', padding: '0px', backgroundColor: 'rgba(0,0,0,0)'}}>
            <Connect>
              Connect
            </Connect>
          </ProfessorContainer>
        </MatchContainer>
      </Container>
    </div>
  )
}

export default Student;