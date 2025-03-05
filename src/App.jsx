import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router";

// -- Page imports --
import TestPage from "./pages/TestPage";
import HomePage from "./pages/HomePage";


// -- Main page manager for the whole site --

function App() {
	return (
		<BrowserRouter>
			<Routes>
				{/* Link URLS to jsx pages here */}
				<Route path="/" element={<HomePage />} />
				<Route path="/test" element={<TestPage />} />
			</Routes>
		</BrowserRouter>
	);
}

export default App;
