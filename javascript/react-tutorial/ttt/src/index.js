import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Square extends React.Component {
    // every component inherits from React.Component
    // render returns what you want to see on screen

    constructor(props) {
        // in JS, you have to always call 'super' when defining the constructor of a subclass.
        // React component classes that have a constructor start with a super(props) call.
        super(props);
        this.state = {
                value: null,
            };
        }
    
    render() {
      return (
        <button
         className="square"

         onClick={() => this.setState({value: 'X'})}>
            {/* javascript expressions use {} inside JSX */}
          {this.state.value}
        </button>
      );
    }
  }
  
  class Board extends React.Component {
      // data is passed from Board to Square using a property or prop called 'value'
    renderSquare(i) {
      return <Square value={i}/>;
    }
  
    render() {
      const status = 'Next player: X';
  
      return (
        <div>
          <div className="status">{status}</div>
          <div className="board-row">
            {this.renderSquare(0)}
            {this.renderSquare(1)}
            {this.renderSquare(2)}
          </div>
          <div className="board-row">
            {this.renderSquare(3)}
            {this.renderSquare(4)}
            {this.renderSquare(5)}
          </div>
          <div className="board-row">
            {this.renderSquare(6)}
            {this.renderSquare(7)}
            {this.renderSquare(8)}
          </div>
        </div>
      );
    }
  }
  
  class Game extends React.Component {
    render() {
      return (
        <div className="game">
          <div className="game-board">
            <Board />
          </div>
          <div className="game-info">
            <div>{/* status */}</div>
            <ol>{/* TODO */}</ol>
          </div>
        </div>
      );
    }
  }
  
  // ========================================
  
  const root = ReactDOM.createRoot(document.getElementById("root"));
  root.render(<Game />);
  