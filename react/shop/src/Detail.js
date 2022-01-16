import React, {useState} from 'react'
import { useHistory, useParams } from 'react-router-dom';

function Detail(props){
  let { id } = useParams();
  let history = useHistory();
  let firstUrl = "https://codingapple1.github.io/shop/shoes"
  let endUrl = ".jpg"
  let middleUrl = id + 1
  return (
    <div className="container">
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