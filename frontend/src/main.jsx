import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { IntlProvider } from 'react-intl'
import messages from './i18n/messages/en.json'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <IntlProvider locale="en" messages={messages}>
      <App />
    </IntlProvider>
  </StrictMode>,
)