import React, {useRef,useState, useMemo, useCallback} from "react";
import Hello from "./Hello"
import Wrapper from "./Wrapper";
import "./App.css"
import Counter from "./Counter"
import InputSample from "./InputSample"
import UserList from "./UserList"
import CreateUser from "./CreateUser"

function countActiveUsers(users) {
  console.log('활성 사용자 수를 세는 중...')
  return users.filter(user => user.active).length;
}

function App() {
  // const name='react';
  // const style = {
  //   backgroundColor: 'black',
  //   color:'aqua',
  //   fontSize:'20px',
  //   padding:'1rem',
  // }
  const [inputs,setInputs] = useState({
    username:'',
    email:'',
  })
  const {username, email} = inputs;

  const onChange = useCallback((e) => {
    const {value, name} = e.target;
    setInputs(inputs =>({
      ...inputs,
      [name]:value
    }))
  },[])
  const [users, setUsers] = useState([
    {id:1, username:'developer', email:'public.developer@gmail.com'},
    {id:2, username:'tester', email:'public.tester@gmail.com'},
    {id:3, username:'lee', email:'public.lee@gmail.com'},
  ])

  const nextId = useRef(4);
  const onCreate = useCallback(() => {
    const user = {
      id: nextId.current,
      username,
      email,
    }
    setUsers(users => users.concat(user))
    setInputs({
      username:'',
      email:'',
    })
    nextId.current += 1;
  },[users, username, email])
  const onRemove = useCallback(id => {
    setUsers(users => users.filter(user => user.id !== id))
  },[])
  const onToggle = useCallback(id => {
    setUsers(users => users.map(user => user.id === id ? {...user, active: !user.active} : user))
  },[])

  const count = useMemo( () => countActiveUsers(users), [users])
  return (
    // <Wrapper>
    //   <Hello name="React!!" color="red" isSpecial={false}/>
    //   <Hello name="hihi" isSpecial={false}/>
    //   <Hello color="pink"isSpecial={true}/>
    //   <hr/>
    //   <div style={style}>{name}</div>
    //   <div className="gray-box"></div>
    //   <Counter/>
    // </Wrapper>
    // <InputSample/>
    <>
    <CreateUser username={username} email={email} onChange={onChange} onCreate={onCreate}/>
    <UserList users={users} onRemove={onRemove} onToggle={onToggle}/>
    <div>활성 사용자 수 : {count}</div>
    </>
  )
}

export default App