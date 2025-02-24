import streamlit as st

# # App title
# st.title("Simple To-Do List App")

# # Initialize session state
# if "tasks" not in st.session_state:
#     st.session_state.tasks = []

# st.sidebar.header("Manage Your Task")

# # Add new task
# new_task = st.sidebar.text_input("Enter Your New Task")
# if st.sidebar.button("Add Task"):
#     if new_task.strip():
#         st.session_state.tasks.append({"task": new_task, "completed": False})
#         st.sidebar.success("Task added successfully!")
#     else:
#         st.sidebar.warning("Task cannot be empty!")

# # Display tasks
# st.subheader("Your Tasks")
# if st.session_state.tasks:
#     for i, task in enumerate(st.session_state.tasks):
#         col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
#         col1.write(f"{task['task']}")


#         # Edit task
#         if col2.button("Edit", key=f"edit_{i}"):
#             new_task = st.text_input("Edit Task", task["task"], key=f"edit_input_{i}")
#             if st.button("Save", key=f"save_{i}"):
#                 if new_task.strip():
#                     st.session_state.tasks[i]["task"] = new_task
#                     st.rerun()
#                 else:
#                     st.warning("Task cannot be empty!")

#         # Delete task
#         if col3.button("Delete", key=f"delete_{i}"):
#             del st.session_state.tasks[i]
#             st.rerun()
# else:
#     st.info("No tasks added yet. Start by adding one!")

# # Clear all tasks
# if st.button("Clear All Tasks"):
#     st.session_state.tasks = []
#     st.success("All tasks deleted successfully!")
#     st.rerun()
   


import streamlit as st

# App title
st.title("📝 Simple To-Do List App")

# Initialize session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.sidebar.header("🛠️ Manage Your Task")

# Add new task
new_task = st.sidebar.text_input("Enter Your New Task")
if st.sidebar.button("➕ Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.sidebar.success("Task added successfully!")
    else:
        st.sidebar.warning("Task cannot be empty!")

# Display tasks
st.subheader("📋 Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
        col1.write(f" {task['task']}")

        # Edit task
        if col2.button("✏️ Edit", key=f"edit_{i}"):
            new_task = st.text_input("Edit Task", task["task"], key=f"edit_input_{i}")
            if st.button("Save", key=f"save_{i}"):
                if new_task.strip():
                    st.session_state.tasks[i]["task"] = new_task
                    st.rerun()
                else:
                    st.warning("Task cannot be empty!")

        # Delete task
        if col3.button("❌ Delete", key=f"delete_{i}"):
            del st.session_state.tasks[i]
            st.rerun()
else:
    st.info("⚠️ No tasks added yet. Start by adding one!")

# Clear all tasks
if st.button("🗑️ Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks deleted successfully!")
    st.rerun()
