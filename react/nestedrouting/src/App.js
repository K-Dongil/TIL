import {BrowserRouter as Switch, Route} from "react-router-dom"
import Nested1 from "./Nested1"

function App() {
  return (
    <div className="App">
      <Switch>
        <Route path="/nested" component={Nested1} />
      </Switch>
    </div>
  );
}

export default App;
