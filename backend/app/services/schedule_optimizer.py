from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
import random

from .. import schemas, models
from ..crud import task as crud_task
from ..crud import preference as crud_preference

def generate_and_optimize_schedule(db: Session, user_id: int, schedule_data: schemas.ScheduleCreate) -> schemas.ScheduleCreate:
    """
    Generates and optimizes a personalized schedule for a user.
    This is a simplified heuristic model for demonstration.
    A real implementation would involve more complex algorithms, ML models,
    and deeper analysis of user preferences and historical data.
    """
    user_tasks = crud_task.get_tasks_by_user(db, user_id=user_id)
    user_preferences = crud_preference.get_preferences_by_user(db, user_id=user_id)

    # Example: Parse preferences (simplified)
    preferred_study_time_start = datetime.strptime('08:00', '%H:%M').time()
    preferred_study_time_end = datetime.strptime('17:00', '%H:%M').time()
    preferred_break_duration_minutes = 15
    study_block_duration_minutes = 60

    for pref in user_preferences:
        if pref.key == 'preferred_study_start' and pref.value:
            preferred_study_time_start = datetime.strptime(pref.value, '%H:%M').time()
        if pref.key == 'preferred_study_end' and pref.value:
            preferred_study_time_end = datetime.strptime(pref.value, '%H:%M').time()
        if pref.key == 'preferred_break_duration_minutes' and pref.value.isdigit():
            preferred_break_duration_minutes = int(pref.value)

    # Basic scheduling logic
    current_time = datetime.combine(schedule_data.date.date(), preferred_study_time_start)
    end_of_day = datetime.combine(schedule_data.date.date(), preferred_study_time_end)
    optimized_blocks: List[schemas.ScheduleBlock] = []

    remaining_tasks = sorted(user_tasks, key=lambda t: (t.priority, t.difficulty), reverse=True)

    while remaining_tasks and current_time < end_of_day:
        task = remaining_tasks.pop(0) # Take the highest priority/difficulty task
        
        # Schedule study block
        block_end_time = current_time + timedelta(minutes=min(task.estimated_time_minutes, study_block_duration_minutes))
        if block_end_time > end_of_day:
            break # No more time in the day

        optimized_blocks.append(schemas.ScheduleBlock(
            type='study',
            start_time=current_time,
            end_time=block_end_time,
            task_id=task.id,
            subject_id=task.subject_id,
            description=task.title
        ))
        task.estimated_time_minutes -= min(task.estimated_time_minutes, study_block_duration_minutes)
        if task.estimated_time_minutes > 0:
            # If task not finished, put it back to be scheduled later
            remaining_tasks.append(task)
            remaining_tasks.sort(key=lambda t: (t.priority, t.difficulty), reverse=True)

        current_time = block_end_time

        # Add a break if there's time and it's not the end of the day
        if current_time + timedelta(minutes=preferred_break_duration_minutes) < end_of_day:
            optimized_blocks.append(schemas.ScheduleBlock(
                type='break',
                start_time=current_time,
                end_time=current_time + timedelta(minutes=preferred_break_duration_minutes),
                description='Short break'
            ))
            current_time += timedelta(minutes=preferred_break_duration_minutes)

    # Add placeholder for potential conflict resolution or workload balancing here
    # e.g., if total scheduled time exceeds capacity, or if specific subjects are grouped.
    # For this blueprint, we assume it fits.

    # Return a new ScheduleCreate object with the optimized blocks
    # The actual user_id should come from the authenticated user
    return schemas.ScheduleCreate(
        user_id=user_id,
        date=schedule_data.date,
        schedule_data=optimized_blocks
    )

