
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from "react-router";
import { CookiesProvider } from 'react-cookie'
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
    <CookiesProvider defaultSetOptions={{ path: '/', maxAge: (60 * 60 * 24), secure: true, sameSite: 'lax' }}>
      <BrowserRouter>
          <App />
      </BrowserRouter>
    </CookiesProvider>
)
