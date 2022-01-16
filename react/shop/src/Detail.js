import React, {useState} from 'react'
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


function Detail(props){

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
     <div className="my-alert-yellow">
       <p>재고가 얼마 남지 않았습니다</p>
     </div>
     <div className="row">
        <div className="col-md-6">
          <img src={firstUrl+middleUrl+endUrl} width="100%" />
        </div>
        <div className="col-md-6 mt-4">
          <h4 className="pt-5">{props.shoes[id].title}</h4>
          <p>{props.shoes[0].content}</p>
           <p>{props.shoes[0].price}</p>
           <button className="btn btn-danger">주문하기</button>
           <button className="btn btn-danger" onClick={()=>{
             history.goBack();
           }}>뒤로가기</button>
        </div>
       </div>
    </div> 
  )
}

export default Detail;