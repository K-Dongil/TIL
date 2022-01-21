import {BrowserRouter as Router, Switch, Route} from "react-router-dom"
import CommentList from "./routes/Post/CommentList";

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/post/:num"><CommentList /></Route>
      </Switch>
    </Router>
  );
}

export default App;