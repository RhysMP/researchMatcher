import styled from 'styled-components';
import { Link } from 'react-router-dom';
import { FONT_COLOR, FONT_SIZE, COLOR } from '../constants';

const Navbar = styled.nav`
	width: 100%;
	height: 60px;
	display: flex;
	flex-direction: row;
  font-weight: bold;
	background-color: #5879D1;
`;

const LeftContainer = styled.div`
	flex: 30%;
	display: flex;
	align-items: center;
	padding: 10px 50px;
`;

const RightContainer = styled.div`
	flex: 70%;
	display: flex;
	justify-content: flex-end;
	padding-right: 10px;
`;

const JoinButton = styled.button`
	align-self: center;
	all: unset;
	padding: 0px 20px;
	color: black;
	background-color: white;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", Segoe UI Symbol, "Noto Color Emoji" !important;
	height: 35px;
	font-family: 'Lato';
	font-weight: bold;
	margin: 0px 20px;
	border-radius: 10px;
	
	&:hover {
		transform: scale(1.03);
		cursor: pointer;
	}

	&:active {
		box-shadow: none;
		transform: translateY(0);
		cursor: pointer;
	}
`;

const NavbarLink = styled(Link)`
	align-self: center;
	text-decoration: none;
  font-family: 'Inria Sans', sans-serif;
	padding: 0px 24px;
	margin: 0px 3px;
	color: white;
	&:hover {
		padding-top: 2px;
		padding-bottom: 2px;
		border-radius: 0px;
		outline: 1px solid black;
	}

	&:hover {
		transform: scale(1.03);
		cursor: pointer;
	}

	&:active {
		box-shadow: none;
		transform: translateY(0);
		cursor: pointer;
	}
`;

const Logo = styled.div`
	color: black;
	font-size: ${FONT_SIZE.xl};
	align-self: center;
`

const AIContainer = styled.div`
  color: white;
  width: 20px;
  font-size: 16px;
  display: flex;
  align-items: center;
  margin-left: 10px;
`;

const AI = styled.div`
  border-radius: 40px;
  padding: 2px 10px;
  background-color: ${FONT_COLOR.tertiary};
  font-family: Spot Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace;
`;

function Nav() {
	return (
		<Navbar>
			<LeftContainer>
				<button
					style={{ all: 'unset', cursor: 'pointer', display: 'flex'}}
					onClick={() => {
						window.location.href = '/';
					}}
				>
					<Logo style={{alignSelf: 'center'}}>ResearchMatcherer</Logo>
          <AIContainer><AI>AI</AI></AIContainer>
				</button>
			</LeftContainer>
			<RightContainer>
				<NavbarLink
								onClick={() => {
						window.location.href = '/';
					}}>
						Share your research
				</NavbarLink>

				<NavbarLink
					onClick={() => {
						window.location.href = '/';
					}}>
					Contact</NavbarLink>

				<NavbarLink
					onClick={() => {
						window.location.href = '/student';
					}}>
					Sign in
				</NavbarLink>
				<div style={{ height: 'min-content', display: 'flex', alignSelf: 'center'}}>
					<JoinButton
						onClick={() => {
							window.location.href = '/student';
						}}
					>
						Join Us
					</JoinButton>
				</div>
			</RightContainer>
		</Navbar>
	);
}

export default Nav;