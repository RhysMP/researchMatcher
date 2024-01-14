import styled from 'styled-components';
import Nav from '../../components/Navbar.js';
import { FONT_SIZE } from '../../constants';
import whiteabstract from '../../whitewaves.jpg';

const Container = styled.div`
  display: flex;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-image: url(${whiteabstract});
  width: 100%;
  height: calc(100vh - 60px);
`;

const LeftPanel = styled.div`
  background-color: #8FA8E9;
  width: 250px;
  border-radius: 20px;
`;

const LeftPanelCover = styled.div`
  background-color: #EBF0FB;
  height: calc(100% - 40px);
  width: calc(100% - 60px);
  padding: 20px;
`;

const MatchContainer = styled.div`
  display: flex;
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
`;

const Image = styled.div`
  width: 250px;
  height: 250px;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  background-image: url("https://lastfm.freetls.fastly.net/i/u/770x0/94cbc3fbf0529f53cfec3a31b1c33e31.jpg#94cbc3fbf0529f53cfec3a31b1c33e31");
`;

const Subtitle = styled.div`
  font-size: ${FONT_SIZE.lg};
`;

const Description = styled.div`
  font-size: ${FONT_SIZE.sm};
`;

const MatchScore = styled.div`
  font-size: ${FONT_SIZE.xl};
`

// The Student Dashboard

function Student() {
  return (
    <div>
      <Nav/>
      <Container>
        <LeftPanel><LeftPanelCover/></LeftPanel>
        <MatchContainer>
          <ProfessorContainer>
            <Name>Jimmy O' Yang</Name>
            <div style={{display: 'flex', flexDirection: 'row'}}>
              <Image/>
              <Description style={{marginLeft: '20px', flex: 1}}>
                <MatchScore>
                  79%
                  <br/>
                  Match
                </MatchScore>
                <div style={{marginTop: '40px'}}>
                  Expertise in:
                  <br></br>
                  * [Looping through professor keywords option]
                </div>
              </Description>
            </div>
            
            <Description>
              <Subtitle>
                Research Snippet:
              </Subtitle>
              This paper shows how Long Short-term Memory recurrent neural networks can be used to generate complex sequences with long-range structure, simply by predicting one data point at a time. The approach is demonstrated for text (where the data are discrete) and online handwriting (where the data are real-valued). It is then extended to handwriting synthesis by allowing the network...
            </Description>
          </ProfessorContainer>
        </MatchContainer>
      </Container>
    </div>
  )
}

export default Student;