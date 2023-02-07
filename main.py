import streamlit as st

clients = ["EMS1", "VEL1", "SEN1"]
tasks = {
    "Client 1": ["Incoming", "Masking", "RUN", "Demasking", "Conditionning", "Sending"],
    "Client 2": ["Incoming", "Masking", "RUN", "demasking", "conditionning", "Sending"],
    "Client 3": ["Incoming", "Masking", "RUN", "demasking", "conditionning", "Sending"],
}
progress = {
    "EMS1": [0, 0, 0, 0, 0, 0],
    "VEL1": [0, 0, 0, 0, 0, 0],
    "SEN1": [0, 0, 0, 0, 0, 0],
}

st.title("Task Management App")

selected_client = st.selectbox("Select a client", clients)
selected_task = st.selectbox("Select a task", tasks[selected_client])
task_index = tasks[selected_client].index(selected_task)

if st.button("Mark as Complete"):
    progress[selected_client][task_index] = 100

st.write("Progress: ", progress[selected_client][task_index], "%")

st.write("Tasks:")
for i in range(len(tasks[selected_client])):
    st.write("- ", tasks[selected_client][i], ": ", progress[selected_client][i], "%")
