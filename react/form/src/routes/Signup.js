import React, { useEffect, useState } from 'react'

function Signup() {
  const [nickname, nicknameChange] = useState("");
  const [age, ageChange] = useState("");
  const [radioChecked, setRadioChecked] = useState("");
  const [useNickName, addNickName] = useState(['Dongil', 'Kimdongil'])
  const [nickBtn, deactivateNickBtn] = useState(false)
  

  const changeNickName = e => {
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
    if ( (nickname in useNickName) ) {
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
    }, [nickname]
  ) 

  console.log(useNickName)
  console.log(typeof nickname)
  console.log(typeof useNickName[0])
  console.log(nickname)
  console.log(useNickName)
  console.log(nickname in useNickName)

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
        <input type='submit' value='완료' />
      </form>
  
    </div>
  )
}

export default Signup;