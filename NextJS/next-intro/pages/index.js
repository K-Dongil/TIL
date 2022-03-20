import { useState } from "react"
import Seo from "../component/Seo";
// import Head from "next/head";
// import NavBar from "../component/NavBar";


export default function Home(){
  const [counter, setCounter] = useState(0);
  return (
    <div>
      {/* <Head>
        <title>Home | Next Movies</title>
      </Head> */}
      <Seo title="Home" />
      
      {/* <NavBar /> */}
      <h1>Hello {counter} </h1>
      <button onClick={ () => setCounter((a) => a + 1)}>+</button>
      {/* <style jsx global>
        {`
          a {
            color: white;
          }
        `}
      </style> */}
    </div>
  )
}