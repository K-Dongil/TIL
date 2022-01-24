import React from 'react';
import {Table} from 'react-bootstrap'
import { connect, useDispatch, useSelector } from 'react-redux';

function Cart() {

  let state = useSelector((state) => state) //redux안에 있던 모든 state return시키면서 props
  let dispatch = useDispatch();


  return(
    <div>
      <Table responsive>
        <thead>
          <tr>
            <th>#</th>
            <th>상품명</th>
            <th>수량</th>
            <th>변경</th>
          </tr>
        </thead>
        <tbody>
          {
            state.reducer1.map((a, i)=>{
              return(
                <tr key={i}>
                  <td>{ a.id }</td>
                  <td>{ a.name }</td>
                  <td>{ a.quan }</td>
                  <td>Table cell</td>
                  <td>
                    <button onClick={()=>{ dispatch( { type : '수량증가', payload : i} ) }}>+</button>
                    <button onClick={()=>{ dispatch( { type : '수량감소', payload : i} ) }}>-</button>
                  </td>
                </tr>
              )
            })
          }
        </tbody>
      </Table>
      {
        state.reducer2
        ? (<div calssName="my-alert2">
            <p>지금 구매하시면 신규할인 20%</p>
            <button onClick={()=>{ dispatch( { type : '닫기버튼'} ) }}>닫기</button>
          </div>)
        : null
      }
    </div>
  )
}

// function 함수명(state) {
//   return {
//     state : state.reducer1,
//     alert열렸니 : state.reducer2
//   }
// }

// export default connect(함수명)(Cart)

export default Cart;