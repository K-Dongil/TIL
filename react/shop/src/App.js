import React, {useContext, useState} from 'react'
import { Navbar, Container, Nav, NavDropdown, Button} from 'react-bootstrap';
import './App.css';
import Data from './data.js';
import { Link, Route, Switch } from 'react-router-dom'
import Detail from './Detail.js';
import axios from 'axios';
import Cart from './Cart';

let 재고context = React.createContext();

function App() {

  let [shoes, shoes변경] = useState(Data);
  let [재고, 재고변경] = useState([10, 11, 12]);
  
  return (
    <div className='App'>
       <Navbar bg="light" expand="lg">
          <Container>
            <Navbar.Brand href="#home">DongilShop</Navbar.Brand>
            <Navbar.Toggle aria-controls="basic-navbar-nav" />
            <Navbar.Collapse id="basic-navbar-nav">
              <Nav className="me-auto">
                <Link to="/detail" className="link_css">Test</Link>
                <Nav.Link as={Link} to="/">Home</Nav.Link>
                <Nav.Link as={Link} to="/detail">Detail</Nav.Link>
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
          <div className="container">
            <재고context.Provider value={재고}>
              <div className="row">
                {
                  shoes.map(function(신발, i){
                    return(
                      <Compo 전송데이터={shoes[i] } 순서={i} key={i}></Compo>
                    )
                  })
                }
              </div>
            </재고context.Provider>
            <button className="btn btn-primary" onClick={()=>{
              axios.get("https://codingapple1.github.io/shop/data2.json") // 서버에 get요청하는 코드, aixos.get(데이터 요청할URL)
              .then((result)=>{
                shoes변경( [...shoes, ...result.data ] )
              })
              .catch((result)=>{
                console.log("실패")
              })
            }}>더보기</button>
          </div>
        </Route>

        <Route path="/detail/:id">
          <Detail shoes={shoes} 재고={재고} 재고변경={재고변경}/>
        </Route>

        <Route path="/cart">
          <Cart></Cart>
        </Route>


      </Switch>

      
    </div>
  );
}

function Compo(props) {
  let firstUrl = "https://codingapple1.github.io/shop/shoes"
  let endUrl = ".jpg"
  let middleUrl = props.순서 + 1
  let 재고 = useContext(재고context)
  return (
    <div className='col-md-4'>
      <img src={firstUrl+middleUrl+endUrl} width="100%"></img>
      <h4>{ props.전송데이터.title }</h4>
      <p>{ props.전송데이터.content } & { props.전송데이터.price }</p>
      {재고}
    </div>
  )
}

export default App;