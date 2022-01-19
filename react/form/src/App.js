import './App.css';
import Signup from './routes/Signup';
import {BrowserRouter as Switch, Route} from "react-router-dom"

function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path='/'>
          <a href="./signup">회원가입</a>
        </Route>
        <Route path='/signup'>
          <Signup></Signup>
        </Route>
      </Switch>
    </div>
  );
}

export default App;
