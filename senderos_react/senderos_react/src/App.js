import logo from './logo.png';
import React from 'react';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';


class App extends React.Component{
  state = {
    excursiones : []
  }

  componentDidMount(){
    fetch('http://localhost:8000/api/excursiones')
    .then(res=>res.json())
    .then(datos=>{
      console.log(datos)
    })
  }

  render(){
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
}

export default App;
