import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "../styles/Home.css";
import TopPanelBar from "../components/TopPanelBar.jsx";

function HomePage() {
  return <>
    <TopPanelBar/>
  </>;
}

export default HomePage;