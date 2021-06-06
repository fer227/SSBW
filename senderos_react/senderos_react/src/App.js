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
      this.setState({excursiones: datos})
    })
  }

  render(){
    return (
      <div>
        <Container fluid> 
          <Navbar bg="light">
            <Navbar.Brand href="#home">
              <img alt="" src={logo} width="50" height="30" className="d-inline-block align-top"/>
              <span style={{marginLeft:'2vw'}}>Senderos Granada- React</span>
            </Navbar.Brand>
          </Navbar>
        </Container>
        <div className="container" style={{marginTop: '15px'}}>
          <h1>Bienvenido a Senderos</h1>
          <div className="d-flex flex-wrap mt-5 justify-content-around">
            {this.state.excursiones.map((e) => (
              <div className="card me-3 mb-5" style={{width: '18rem'}}>
                <img className="card-img-top" src={"http://localhost:8000/static/images/" + e.file}/>
                <div className="card-body">
                  <h5>{e.nombre}</h5>
                  <p className="card-text">{e.descripcion}</p>
                  <a href="#" className="btn btn-primary">Más información</a>
                </div>
              </div>
            ))}
          </div>  
        </div>      
      </div>     
    );
  }
}

export default App;
