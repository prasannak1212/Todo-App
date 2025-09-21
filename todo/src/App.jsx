import './App.css'
import {useState} from 'react'
import Todo from './components/Todo'
import BackgroundParticles from "./components/ParticleBackground";

function App() {

  return(
    <>
      <BackgroundParticles />
      <Todo />
    </>
  )
}

export default App
