
import React, {Component} from "react";

class App extends Component {
  state = {
    count : 0
  }
  
  countup = () => {
    this.setState({
      count: this.state.count + 1
    })
  }
  countdown = () => {
    this.setState({
      count: this.state.count - 1
    })
  }
  
  render() {
    return (
      <div className="App">
      <h1>{this.state.count}</h1>
      <button onClick={this.countup}>Count Up!!</button>
      <button onClick={this.countdown}>Count Down!!</button>
    </div>
  )
}
}

export default App