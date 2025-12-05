import streamlit as st
import pandas as pd

st.set_page_config(page_title='To-Do List App', page_icon='📝')

st.title('📝 To-Do List App')
st.markdown('A simple app to manage your tasks')

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Sidebar inputs
with st.sidebar:
    st.header('Settings')
    new_task = st.text_input('Enter new task')

# Main content
if st.button('Add Task'):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f'Task added: {new_task}')
    else:
        st.error('Please enter a task')

# Display tasks
st.header('Your Tasks')
if st.session_state.tasks:
    task_df = pd.DataFrame(st.session_state.tasks, columns=['Task'])
    st.write(task_df)
else:
    st.info('No tasks added yet')

# Delete task
with st.expander('Delete Task'):
    task_index = st.number_input('Enter task number to delete (1-indexed)', min_value=1, step=1)
    if st.button('Delete'):
        try:
            if task_index <= len(st.session_state.tasks):
                del st.session_state.tasks[task_index - 1]
                st.success('Task deleted')
            else:
                st.error('Invalid task number')
        except Exception as e:
            st.error(f'Error deleting task: {str(e)}')

# Edit task
with st.expander('Edit Task'):
    task_index = st.number_input('Enter task number to edit (1-indexed)', min_value=1, step=1)
    new_task_edit = st.text_input('Enter new task description')
    if st.button('Edit'):
        try:
            if task_index <= len(st.session_state.tasks):
                st.session_state.tasks[task_index - 1] = new_task_edit
                st.success('Task edited')
            else:
                st.error('Invalid task number')
        except Exception as e:
            st.error(f'Error editing task: {str(e)}')

# Clear all tasks
if st.button('Clear All Tasks'):
    st.session_state.tasks = []
    st.success('All tasks cleared')