import React, { useEffect, useState } from 'react'

function Signup() {
  const [nickname, nicknameChange] = useState("");
  const [age, ageChange] = useState("");
  const [radioChecked, setRadioChecked] = useState("");
  const [useNickName, addNickName] = useState(['Dongil', 'Kimdongil'])
  const [nickBtn, deactivateNickBtn] = useState(false)
  const [submitBtn, deactivateSubmitBtn] = useState(true)
  

  const changeNickName = (e) => {
    nicknameChange(e.target.value);
  }

  const changeRadioChecked = e => {
    if (e.target.checked) { // e.target.checked는 radio버튼 클릭되면 true
      setRadioChecked(e.target.id); 
    }
  }

  const changeAge = e => {
    ageChange(e.target.value);
  }

  const checkNickName = () => {
    // 닉네임 중복에 대한 결과값을 Back에서 받아온다.
    let resultOverlap = false
    for (let nick of useNickName){
      if (nickname === nick) {
        resultOverlap = true
      }
    }
    if ( resultOverlap ) {
      return (
        alert("중복입니다")
      )
    } else {
      addNickName( [...useNickName, nickname] )
      deactivateNickBtn(true)
      return (
        alert("사용가능합니다")
      )
    }
  }

  useEffect( () => {
    deactivateNickBtn(false)
    deactivateSubmitBtn(true)
    console.log(nickname)
    }, [nickname]
  )

  useEffect( () => {
    if (nickBtn && radioChecked && age) {
      deactivateSubmitBtn(false)
    }
    }, [nickBtn, nickname, radioChecked, age]
  )

  return(
    <div className="Signup">
      <form action='./login'>
        <h2>회원가입</h2>
        <label>별명:</label>
        <input
          type="text"
          name="nickname"
          value={ nickname }
          onChange={ changeNickName }
        />
        <button type="button" onClick={ checkNickName } disabled={ nickBtn }>중복확인</button> <br/>
        <label>성별:</label>
        <label>
          <input
            type="radio"
            id = "men"
            name="radioChecked"
            value={ radioChecked }
            onChange={ changeRadioChecked }
          />
          남
        </label>
        <label>
          <input
            type="radio"
            id = "women"
            name="radioChecked"
            value={ radioChecked }
            onChange={changeRadioChecked}
          />
          여
        </label><br/>
        <label>나이:</label>
        <input
          placeholder="나이를 입력해주세요"
          type="text"
          name="age"
          value={ age }
          onChange={ changeAge }
        /><br/>
        <button type="submit" disabled={ submitBtn }>완료</button>
      </form>
  
    </div>
  )
}

export default Signup;