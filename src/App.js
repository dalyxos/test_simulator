import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Button } from 'antd';
import StatusPanel from './StatusPanel';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Button type="primary">Button</Button>
        <StatusPanel />
      </header>
    </div>
  );
}

export default App;
