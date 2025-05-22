import React, { useEffect } from "react"

const User = React.memo(function User({user, onRemove, onToggle}){
  useEffect(() => {
    console.log('user value setted...')
    console.log(user)
    return () => {
      console.log('before user value')
      console.log(user)
    }
  },[user])
  return(
  <div>
    <b style={{cursor:'pointer', color: user.active ? 'green':'black'}} onClick = {() => onToggle(user.id)}>{user.username}</b>-<span>{user.email}</span>
    <button onClick = {() => onRemove(user.id)}>삭제</button>
  </div>
  ) 
})


export default React.memo(function UserList({users,onRemove, onToggle}){
  // const users = [
  //   {id:1, username:'developer', email:'public.developer@gmail.com'},
  //   {id:2, username:'tester', email:'public.tester@gmail.com'},
  //   {id:3, username:'lee', email:'public.lee@gmail.com'},
  // ]
  return (
    <div>
      {
        users.map(user =>(
          <User key={user.id} user={user} onRemove={onRemove} onToggle={onToggle}/>
        ))
      }
    </div>
    
  )
})