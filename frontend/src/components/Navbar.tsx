import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import { logout } from '../features/auth/authSlice';

const Navbar: React.FC = () => {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleLogout = () => {
    dispatch(logout());
    navigate('/login');
  };

  return (
    <nav className="bg-indigo-600 p-4 text-white shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold">Smart Scheduler</Link>
        <div className="space-x-4">
          <Link to="/dashboard" className="hover:text-indigo-200">Dashboard</Link>
          <Link to="/schedule" className="hover:text-indigo-200">Schedule</Link>
          <Link to="/tasks" className="hover:text-indigo-200">Tasks</Link>
          <Link to="/preferences" className="hover:text-indigo-200">Preferences</Link>
          <button onClick={handleLogout} className="hover:text-indigo-200">Logout</button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
