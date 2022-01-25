import React from "react";
import styled from "styled-components";

function Slide({ img }) {
  return (
      <IMG src={img} />
  );
}

const IMG = styled.img`
  width: 60%;
  height: 70vh;
`;

export default Slide;