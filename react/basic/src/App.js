import React, {Component} from "react";
import Hello from "./Hello"
import Wrapper from "./Wrapper";
import "./App.css"
import Counter from "./Counter"

function App() {
  const name='react';
  const style = {
    backgroundColor: 'black',
    color:'aqua',
    fontSize:'20px',
    padding:'1rem',
  }
  return (
    <Wrapper>
      <Hello name="React!!" color="red" isSpecial={false}/>
      <Hello name="hihi" isSpecial={false}/>
      <Hello color="pink"isSpecial={true}/>
      <hr/>
      <div style={style}>{name}</div>
      <div className="gray-box"></div>
      <Counter/>
    </Wrapper>
  )
}

export default App