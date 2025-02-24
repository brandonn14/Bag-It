import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './Styles.css'
import TopPanelBar from './TopPanelBar.jsx'



createRoot(document.getElementById('root')).render(
  <StrictMode>
    <TopPanelBar />
  </StrictMode>,
)
