import React from 'react';
import { useSelector } from 'react-redux';
import { RootState } from '../app/store';
import Navbar from '../components/Navbar';

const DashboardPage: React.FC = () => {
  const user = useSelector((state: RootState) => state.auth.user);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />
      <main className="flex-grow p-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-6">Welcome, {user?.email || 'Student'}!</h1>
        <p className="text-lg text-gray-700 mb-4">This is your personalized dashboard. Here you'll find an overview of your schedule, upcoming tasks, and actionable insights.</p>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Today's Schedule</h2>
            <p className="text-gray-600">Your intelligent schedule for today will be displayed here.</p>
            {/* Placeholder for schedule component */}
          </div>

          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Upcoming Tasks</h2>
            <p className="text-gray-600">View and manage your tasks. Add new assignments, projects, and exams.</p>
            {/* Placeholder for tasks component */}
          </div>

          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Insights & Tips</h2>
            <p className="text-gray-600">Personalized recommendations to optimize your learning and productivity.</p>
            {/* Placeholder for insights component */}
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;
