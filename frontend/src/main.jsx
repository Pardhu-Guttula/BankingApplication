import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { IntlProvider } from 'react-intl'
import { BrowserRouter } from 'react-router-dom'
import './index.css'
import App from './App.jsx'
import messages from './i18n/messages/en.json'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <IntlProvider messages={messages} locale="en" defaultLocale="en">
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </IntlProvider>
  </StrictMode>,
)
