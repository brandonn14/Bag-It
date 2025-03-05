import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router";

import TestPage from "./pages/TestPage";
import HomePage from "./pages/HomePage";

function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<HomePage />} />
				<Route path="/test" element={<TestPage />} />
			</Routes>
		</BrowserRouter>
	);
}

export default App;
