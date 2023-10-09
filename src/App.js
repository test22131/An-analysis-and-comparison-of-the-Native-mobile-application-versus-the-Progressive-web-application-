import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Camera from './components/Camera';
import Header from './components/Header';
import Gallery from './components/Gallery';
import Contacts from './components/Contacts';
import PhoneInCall from './components/PhoneInCall';

import './App.css';
import { ThemeProvider, createTheme } from '@mui/material/styles';


const theme = createTheme();

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Router>
        <div className="App">
          <Header />
          <Routes>
            <Route exact path="/" element={<Home />} />
            <Route path="/camera" element={<Camera />} />
            <Route path="/gallery" element={<Gallery />} />
            <Route path="/contacts" element={<Contacts />} /> 
            <Route path="/phoneincall" element={<PhoneInCall />} />
          </Routes>
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
