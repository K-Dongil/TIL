import {Route} from "react-router-dom"
import Nested2 from "./Nested2";
import Nested3 from "./Nested3";

function Nested1() {
  return(
    <>
    <div>Nested1 입니다.</div>
    <Route path="/nested/2" component={Nested2}/>
    <Route path="/nested/3" component={Nested3}/>
    </>
  )
}

export default Nested1;