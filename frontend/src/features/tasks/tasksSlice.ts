import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Task {
  id: number;
  title: string;
  description?: string;
  dueDate?: string;
  estimatedTimeMinutes: number;
  difficulty: number;
  priority: number;
  subjectId?: number;
  ownerId: number;
  createdAt: string;
}

interface TasksState {
  tasks: Task[];
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
  error: string | null;
}

const initialState: TasksState = {
  tasks: [],
  status: 'idle',
  error: null,
};

export const tasksSlice = createSlice({
  name: 'tasks',
  initialState,
  reducers: {
    addTask: (state, action: PayloadAction<Task>) => {
      state.tasks.push(action.payload);
    },
    setTasks: (state, action: PayloadAction<Task[]>) => {
      state.tasks = action.payload;
    },
    // Add more reducers for update, delete, etc.
  },
});

export const { addTask, setTasks } = tasksSlice.actions;

export default tasksSlice.reducer;
