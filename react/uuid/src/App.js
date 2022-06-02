import './App.css';
import uuid from 'react-uuid'
import Test from './Test';

function App() {
  return (
    <div className="App">
      <Test></Test>
      {/* 이미지 업로드할 때 파일명 그대로 쓰지말고 uuid로 생성되는 고유값을 쓰면 어떨까 해서 써보는 uuid*/}
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
      <p>{uuid()}</p>
    </div>
  );
}

export default App;
