import { Routes, Route } from 'react-router-dom';
import '@styles/App.css';
import BoardList from '@pages/boardlist.jsx'
import Home from '@pages/home.jsx'

function App() {

  return (
    <div className="app-main">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/board/:id" element={<BoardList />} />
      </Routes>
    </div>
  );
}

export default App;
