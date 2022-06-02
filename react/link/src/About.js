import React from 'react';
import { Link } from 'react-router-dom'
import { useRouter } from './UseRouter';

function About(){
  const router = useRouter();
  return (
    <>
      <nav>
        <Link to="/" style={{color: router.pathname === "/" ? "red" : "blue"}}>Home</Link><br />
        <Link to="/about" style={{color: router.pathname === "/" ? "red" : "red"}}>About</Link>
      </nav>
    </>
  )
}

export default About;