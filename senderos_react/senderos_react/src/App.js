import logo from './logo.png';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';


function App() {
  return (
    <Container fluid>
      <Navbar bg="light">
        <Navbar.Brand href="#home">
          <img alt="" src={logo} width="50" height="30" className="d-inline-block align-top"/>
          <span style={{marginLeft:'2vw'}}>Senderos Granada- React</span>
        </Navbar.Brand>
      </Navbar>
    </Container>
  );
}

export default App;
