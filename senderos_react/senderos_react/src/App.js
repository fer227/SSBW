import logo from './logo.png';
import React from 'react';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';


class App extends React.Component{
  state = {
    excursiones : [],
    excursionesFiltradas: [],
    palabra: "",
    detalle: null
  }

  componentDidMount(){
    fetch('http://localhost:8000/api/excursiones')
    .then(res=>res.json())
    .then(datos=>{
      this.setState({excursiones: datos})
    })
  }

  handleClick = (e) => {
    this.setState({detalle: e})
  }

  goBack = () => {
    this.setState({detalle: null})
  }

  render(){

    if (this.state.detalle != null) {
      return (
        <div>
          <Container fluid> 
            <Navbar bg="light">
              <Navbar.Brand href="#home">
                <img alt="" src={logo} width="50" height="30" className="d-inline-block align-top"/>
                <span style={{marginLeft:'2vw'}}>Senderos Granada- React</span>
              </Navbar.Brand>
            </Navbar>
            
            <button style={{fontSize: "25px", margin: "10px"}} type="button" onClick={() => this.goBack()} className="btn btn-primary btn-lg">&#8249;</button>
          </Container>
          <div className="container" style={{marginTop: '15px'}}>
              <div className="card mb-3 mt-1">
                <div className="row g-0">
                  <div className="col-md-4">
                    <img className="img-fluid" style={{width: '25rem'}} src={"http://localhost:8000/static/images/" + this.state.detalle.file}/>
                  </div>
                  <div className="col-md-8">
                    <div className="card-body">
                      <h5 className="card-title">{this.state.detalle.nombre}</h5>
                      <p className="card-text">{this.state.detalle.descripcion}</p>
                      <div>
                        <span className="likes">👍</span>  <span className="likes">👎</span>   <span id="plikes">{this.state.detalle.likes}</span>
                      </div>
                      <div className="text-end mt-5">
                        <a href="#" className="btn btn-primary btn-lg">Unirse</a>
                      </div>                      
                    </div>
                  </div>
                </div>
              </div>
          </div>      
        </div>     
      )
    }
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

            <div className="mb-3 mt-1">
              <form method="post" action="#">
                <label class="form-label">Busca tu excursión</label>
                <input type="text" class="form-control" onChange={(event) => {this.setState({palabra: event.target.value})}} placeholder="..."/>
              </form>
            </div>

            <div className="d-flex flex-wrap mt-5 justify-content-around">
              {this.state.excursiones.filter((val) => {
                if(this.state.palabra == ""){
                  return val;
                }else if(val.nombre.toLowerCase().includes(this.state.palabra.toLowerCase())){
                  return val;
                }
              })
              .map((e) => (
                <div className="card me-3 mb-5" style={{width: '18rem'}}>
                  <img className="card-img-top" src={"http://localhost:8000/static/images/" + e.file}/>
                  <div className="card-body">
                    <h5>{e.nombre}</h5>
                    <p className="card-text">{e.descripcion}</p>
                    <button type="button" onClick={() => this.handleClick(e)} className="btn btn-primary">Más información</button>
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
