import { Home, Student, NotFound } from './pages';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">
			<BrowserRouter>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/student" element={<Student />} />
					<Route path="*" element={<NotFound />} />
				</Routes>
			</BrowserRouter>
    </div>
  );
}

export default App;
