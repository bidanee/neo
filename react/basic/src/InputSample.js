import React,{useRef, useState} from 'react';

function InputSample(props) {
  const [inputs, setInputs] = useState({
    name:'',
    nickname:''
  })
  const nameInput = useRef()
  const {name, nickname} = inputs;
  const onChange = e => {
    const {value, name} = e.target;
    setInputs({
      ...inputs,
      [name]:value
    })
  }
  const onReset = () => {
    setInputs({
      name:'',
      nickname:''
    })
    nameInput.current.focus();
  }
  return (
    <div>
      <input name='name' onChange={onChange} value={name} placeholder='이름' ref={nameInput}/>
      <input name='nickname' onChange={onChange} value={nickname} placeholder='닉네임'/>
      <button onClick={onReset}>초기화</button>
      <div>값: {name} ({nickname})</div>
    </div>
  );
}

export default InputSample;