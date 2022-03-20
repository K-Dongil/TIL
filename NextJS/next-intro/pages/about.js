// import NavBar from "../component/NavBar";
// import { Head } from "next/document";
import Seo from "../component/Seo";

export default function Potato(){
  return (
    <div>
      {/* <Head>
        <title>Home | Next Movies</title>
      </Head> */}
      <Seo title="about" />
      
      {/* <NavBar /> */}
      <h1>About</h1>
    </div>
  )
}