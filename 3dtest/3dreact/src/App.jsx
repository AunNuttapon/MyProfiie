import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Content3D from './components/Content3D'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Content3D />
    </>
  )
}

export default App
