import { combineReducers, createStore } from "redux"
import axios from 'axios';
import { useState } from "react";


var a = null
// const jsonAsync = async () =>{
//   let jsonData = await axios.get("http://localhost:3000/data/commentData.json")
//   return jsonData.data
// }

// const promise = getPromise()
// const getData = () => {
//   promise.then( jsonAsync => {
//     console.log(jsonAsync);
//   });
// };
// getData()

// const jsonAsync = async () =>{
//   const jsonData = await axios.get("http://localhost:3000/data/commentData.json").then((data)=>console.log(data))
// }
// jsonAsync()
// console.log()

// const jsonAsync = async () =>{
//   const jsonData = await axios.get("http://localhost:3000/data/commentData.json").then((data)=>console.log(data))
//   return jsonData
// }
// console.log(jsonAsync())

const jsonAsync = async () => {
  let jsonData = await axios.get("http://localhost:3000/data/commentData.json")
  a = await jsonData.data
  console.log(a)
}

jsonAsync()
console.log('asdasdasd')
console.log(a)



const reducer = (state = [], action) => {
  
  if (action.type === "recent"){
    return [{text:'POPULAR'}]
  } else {
    return [{text:'RECENT'}]
  }
}

const commentReducer = (state = [], action) => {
  console.log(state)
  if (action.type === "add"){
    console.log(state)
    const copyCommentList = [...state, action.inputComment]
    return copyCommentList
  }else if (action.type === "change"){
    const copyCommentList = [...state]
    // copyCommentList[action.i]
    return copyCommentList
  }
  else{
    return state
  }
}



const store = createStore( combineReducers( {reducer, commentReducer} ))
export default store;