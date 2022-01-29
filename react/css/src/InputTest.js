import React from "react"
// import './InputTest.css'

import { ReactComponent as AB } from './abdc.svg';

function inputTest() {
  return(
    <div class="input">
      <div class="text">
          <input type="text" placeholder="Placeholder" />
      </div>
      <button class="clear">
        <AB />
      </button>
    </div>
  )
}

export default inputTest;