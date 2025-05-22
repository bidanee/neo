export default function Wrapper({children}) {
  const sytle = {
    border: '2px solid black',
    padding:'1rem',
  }
  return <div style={sytle}>{children}</div>
}