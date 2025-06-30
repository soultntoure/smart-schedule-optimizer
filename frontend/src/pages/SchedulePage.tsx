import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { schedulesApi } from '../api/api';
import Navbar from '../components/Navbar';
import { RootState } from '../app/store';

interface ScheduleBlock {
  type: string;
  start_time: string;
  end_time: string;
  task_id?: number;
  subject_id?: number;
  description?: string;
}

interface ScheduleData {
  id: number;
  user_id: number;
  date: string;
  schedule_data: ScheduleBlock[];
  generated_at: string;
}

const SchedulePage: React.FC = () => {
  const user = useSelector((state: RootState) => state.auth.user);
  const [schedule, setSchedule] = useState<ScheduleData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleGenerateSchedule = async () => {
    if (!user) return;

    setLoading(true);
    setError(null);
    try {
      // For a real app, this would send current tasks, preferences, etc.
      const today = new Date();
      const scheduleDate = new Date(today.getFullYear(), today.getMonth(), today.getDate());
      const response = await schedulesApi.generateSchedule({
        user_id: user.id, // Replace with actual user ID from auth
        date: scheduleDate.toISOString(),
        schedule_data: [] // Initial empty data, backend generates it
      });
      setSchedule(response.data);
    } catch (err) {
      console.error('Error generating schedule:', err);
      setError('Failed to generate schedule. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  // In a real app, you might fetch the current day's schedule on load
  useEffect(() => {
    // Example: fetch today's schedule if it exists
  }, [user]);

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <Navbar />
      <main className="flex-grow p-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-6">Your Personalized Schedule</h1>

        <button
          onClick={handleGenerateSchedule}
          disabled={loading}
          className="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 disabled:opacity-50"
        >
          {loading ? 'Generating...' : 'Generate Today\'s Optimized Schedule'}
        </button>

        {error && <p className="text-red-500 mt-4">{error}</p>}

        {schedule ? (
          <div className="mt-6 bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Schedule for {new Date(schedule.date).toLocaleDateString()}</h2>
            {schedule.schedule_data.length > 0 ? (
              <ul className="space-y-3">
                {schedule.schedule_data.map((block, index) => (
                  <li key={index} className="border-b pb-2 last:border-b-0">
                    <p className="font-medium">{new Date(block.start_time).toLocaleTimeString()} - {new Date(block.end_time).toLocaleTimeString()}</p>
                    <p><strong>Type:</strong> {block.type}</p>
                    {block.description && <p><strong>Details:</strong> {block.description}</p>}
                    {block.task_id && <p><strong>Task ID:</strong> {block.task_id}</p>}
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-gray-600">No schedule blocks generated for this day.</p>
            )}
          </div>
        ) : (
          <p className="mt-4 text-gray-600">Click 'Generate Today\'s Optimized Schedule' to create your personalized plan.</p>
        )}
      </main>
    </div>
  );
};

export default SchedulePage;
