import React from 'react';
function Hello({name,color, isSpecial}) {
  return (
    <div>
      <div style={{color}}>Hello~ {name?name:"NoName"}</div>
      <div>{isSpecial ? <b>*</b>:<p>*</p>}</div>
    </div>
    
  )
}

// Hello.defaultProps = {
//   name : 'NoName',
// }

export default Hello