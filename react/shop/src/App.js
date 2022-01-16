import React, {useState} from 'react'
import { Navbar, Container, Nav, NavDropdown, Button} from 'react-bootstrap';
import './App.css';
import Data from './data.js';
import { Link, Route, Switch } from 'react-router-dom'
import Detail from './Detail.js';

function App() {

  let [shoes, shoes변경] = useState(Data);
  
  return (
    <div className='App'>
       <Navbar bg="light" expand="lg">
          <Container>
            <Navbar.Brand href="#home">DongilShop</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Nav.Link ><Link to="/">Home</Link></Nav.Link>
                <Nav.Link ><Link to="/detail">Detail</Link></Nav.Link>
                <NavDropdown title="Dropdown" id="basic-nav-dropdown">
                  <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
                  <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                  <NavDropdown.Divider />
                  <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                </NavDropdown>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
      <Switch>
        <Route exact path="/">
          <div class="jumbotron background">
            <h1>20% Season Off</h1>
            <p>This is a simple hero unit, a simple jumbotron-style component for calling
              extra attention to featured content or information
            </p>
            <p>
              <Button variant="primary">Learn more</Button>
            </p>
          </div>
          <div className='container'>
            <div className="row">
              {
                shoes.map(function(신발, i){
                  return(
                    <Compo 전송데이터={shoes[i] } 순서={i}></Compo>
                  )
                })
              }
            </div>
          </div>
        </Route>
        <Route exact path="/detail/:id">
          <Detail shoes={shoes}/>
        </Route>
        <Route exact path="/:id">
          <div>아무거나 적었을 때 이거 보여주세요</div>
        </Route>
      </Switch>

      
    </div>
  );
}

function Compo(props) {
  let firstUrl = "https://codingapple1.github.io/shop/shoes"
  let endUrl = ".jpg"
  let middleUrl = props.순서 + 1
  return (
    <div className='col-md-4'>
      <img src={firstUrl+middleUrl+endUrl} width="100%"></img>
      <h4>{ props.전송데이터.title }</h4>
      <p>{ props.전송데이터.content } & { props.전송데이터.price }</p>
    </div>
  )
}

export default App;