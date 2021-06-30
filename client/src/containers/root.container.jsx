import React from 'react'
import { Route, Link } from 'react-router-dom'
import Home from './home'
import About from './about'

const App = () => (
  <div>
    <header>
      <Link to="/">Home2</Link>
      <Link to="/about-us">About (Products)</Link>
    </header>

    <main>
      <Route exact path="/" component={Home} />
      <Route exact path="/about-us" component={About} />
    </main>
  </div>
)

export default App
