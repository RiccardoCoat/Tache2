import streamlit as st

def main():
    st.title("Gestion des clients et des tâches")

    clients = ["Client 1", "Client 2", "Client 3"]
    tasks = ["Tâche 1", "Tâche 2", "Tâche 3", "Tâche 4", "Tâche 5", "Tâche 6", "Tâche 7", "Tâche 8", "Tâche 9"]

    selected_client = st.selectbox("Sélectionnez un client", clients)
    selected_task = st.selectbox("Sélectionnez une tâche", tasks)
    task_progress = st.slider("Progression de la tâche", 0, 100)

    st.write("Client sélectionné: ", selected_client)
    st.write("Tâche sélectionnée: ", selected_task)
    st.write("Progression de la tâche: ", task_progress, "%")

if __name__ == '__main__':
    main()
