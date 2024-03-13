import logo from './logo.svg';
import './App.css';

function App() {
  const title = "Lynn's Blog";
  const likes = 50;

  return (
    <div className="App">
      <div className="content">
        <h1>{ title }</h1>
        <p>{ likes }</p>
      </div>
    </div>
  );
}

export default App;
