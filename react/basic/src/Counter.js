import { useState } from "react"
export default function Counter () {
  const [number, setNumber] = useState(0)
  const onIcrease = () => setNumber(prevNumber => prevNumber + 1)
  const onDecrease = () => {number > 0 && setNumber(prevNumber=> prevNumber -1)}
  return(
    <div>
      <h1>{number}</h1>
      <button onClick={onIcrease}>+1</button>
      <button onClick={onDecrease}>-1</button>
    </div>
  )
}