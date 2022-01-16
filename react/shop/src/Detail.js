import React, {useEffect, useState} from 'react'
import { useHistory, useParams } from 'react-router-dom';
import styled from 'styled-components';
import './Detail.scss';

let 박스 = styled.div`
  padding : 20px;
`;

let 제목 = styled.h4`
  font-size : 25px;
  color : ${ props => props.색상 }
`;

// class Detail2 extends React.Component {
//   componentDidMount(){
//     // Detail2 컴포넌트가 Mount(등장) 되었을 때 실행할 코드
//   }

//   componentWillUnmount(){
//     // Detail2 컴포넌트가 UnMount(퇴장) 되었을 때 실행할 코드
//   }
// }

function Detail(props){

  

  useEffect(()=>{
    return function 컴포넌트퇴장() { console.log('unmount') }
  });

  let [alert, alert변경] = useState(true);
  let [inputData, inputData변경] = useState();

  useEffect(()=>{
    // 2초 후에 alert 창을 안 보이게 하기
    //let 타이머 = setTimeout(()=>{}, 2000)
    let 타이머 = setTimeout(()=> {alert변경(false)}, 2000);
    return ()=>{ clearTimeout(타이머) }
  }, [alert]);

  let { id } = useParams();
  let history = useHistory();
  let firstUrl = "https://codingapple1.github.io/shop/shoes"
  let endUrl = ".jpg"
  let middleUrl = id

  return (
    <div className="container">
     <박스>
      {/* <제목 색상={'red'}>Detail</제목> */}
      <제목 className="red">Detail</제목>
     </박스>

     { inputData }
     <input onChange={(e)=>{inputData변경(e.target.value)}}></input>
     
     {
       alert == true
       ? (<div className="my-alert-yellow">
           <p>재고가 얼마 남지 않았습니다</p>
           </div>)
       : null
     }
     
     <div className="row">
        <div className="col-md-6">
          <img src={firstUrl+middleUrl+endUrl} width="100%" />
        </div>
        <div className="col-md-6 mt-4">
          <h4 className="pt-5">{props.shoes[id].title}</h4>
          <p>{props.shoes[0].content}</p>
           <p>{props.shoes[0].price}원</p>
           <Info 재고={props.재고}></Info>
           <button className="btn btn-danger" onClick={()=>{ props.재고변경([9, 11, 12]) }}>주문하기</button>
           <button className="btn btn-danger" onClick={()=>{
             history.goBack();
           }}>뒤로가기</button>
        </div>
       </div>
    </div> 
  )
}
function Info(props){
  return (
    <p>재고 : {props.재고[0]}</p>
  )
}
export default Detail;