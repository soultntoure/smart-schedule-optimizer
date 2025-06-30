import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import DashboardPage from './pages/DashboardPage';
import SchedulePage from './pages/SchedulePage';
import TasksPage from './pages/TasksPage';
import PreferencesPage from './pages/PreferencesPage';
import PrivateRoute from './components/PrivateRoute';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/" element={<PrivateRoute><DashboardPage /></PrivateRoute>} />
          <Route path="/schedule" element={<PrivateRoute><SchedulePage /></PrivateRoute>} />
          <Route path="/tasks" element={<PrivateRoute><TasksPage /></PrivateRoute>} />
          <Route path="/preferences" element={<PrivateRoute><PreferencesPage /></PrivateRoute>} />
          {/* Add more routes as needed */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
