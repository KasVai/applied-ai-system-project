import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler
from ai_interpreter import AIInterpreter

# Initialize AI Interpreter
interpreter = AIInterpreter()

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="wide")

# Persistent Session State
if "owner" not in st.session_state:
    st.session_state.owner = Owner("User", contact_info="user@email.com")

st.title("🐾 PawPal+ Care Planner")

# --- SIDEBAR: ADD PETS ---
with st.sidebar:
    st.header("🐶 Add a Pet")
    p_name = st.text_input("Name", placeholder="Mochi")
    p_species = st.selectbox("Species", ["Dog", "Cat", "Bird", "Other"])
    if st.button("Add Pet"):
        if p_name:
            new_pet = Pet(name=p_name, species=p_species)
            st.session_state.owner.add_pet(new_pet)
            st.success(f"Added {p_name}!")
        else:
            st.error("Please enter a name.")

# --- MAIN UI ---
owner_pets = st.session_state.owner.get_pets()
col1, col2 = st.columns([1, 1])

with col1:
    # --- NEW: SMART AI ENTRY ---
    st.subheader("✨ Smart Task Entry")
    if owner_pets:
        ai_pet_name = st.selectbox("Assign to (AI):", [p.name for p in owner_pets], key="ai_pet")
        user_input = st.text_input("Describe the situation:", placeholder="Max needs his meds")
        
        if st.button("AI Process & Add"):
            if user_input:
                data = interpreter.parse_input(user_input)
                target_pet = next(p for p in owner_pets if p.name == ai_pet_name)
                
                # Create Task with the AI-suggested priority
                new_task = Task(
                    description=data["desc"], 
                    time=data["time"], 
                    frequency=data["freq"], 
                    priority=data.get("priority", 3) # Defaults to 3 if not found
                )
                target_pet.add_task(new_task)
                st.success(f"AI added '{data['desc']}' with Priority {data['priority']}!")
    
    st.divider()

    # --- MANUAL ENTRY (Optional fallback) ---
    st.subheader("📝 Manual Task Entry")
    if owner_pets:
        m_pet_name = st.selectbox("Assign to (Manual):", [p.name for p in owner_pets], key="manual_pet")
        t_desc = st.text_input("Task name:", placeholder="Feeding")
        t_time = st.number_input("Minutes", min_value=5, max_value=300, step=5, value=20)
        t_priority = st.slider("Priority (1-Low, 5-Critical)", 1, 5, 3)
        
        if st.button("Add Manual Task"):
            target_pet = next(p for p in owner_pets if p.name == m_pet_name)
            target_pet.add_task(Task(description=t_desc, time=t_time, frequency="Daily", priority=t_priority))
            st.toast(f"Manual task added for {m_pet_name}!")
    else:
        st.info("Add a pet in the sidebar first!")

with col2:
    st.subheader("📋 Current Pet List")
    for pet in owner_pets:
        # Shows priority if available
        tasks = pet.get_active_tasks()
        st.write(f"**{pet.name}** ({pet.species})")
        for t in tasks:
            st.caption(f"- {t.description} (P: {t.priority}, {t.time}m)")

st.divider()

# --- SCHEDULING ENGINE ---
st.subheader("📅 Generate Today's Schedule")
available_time = st.slider("Available time today (minutes)", 30, 720, 480)

if st.button("Build Optimized Plan"):
    if not owner_pets:
        st.error("No pets found.")
    else:
        scheduler = Scheduler(st.session_state.owner, available_time_minutes=available_time)
        all_tasks = scheduler.retrieve_all_tasks()
        
        if not all_tasks:
            st.warning("No active tasks found.")
        else:
            # UPDATED: Uses the new Priority + Time sorting
            sorted_tasks = scheduler.sort_by_priority_and_time(all_tasks)
            final_plan = scheduler.fit_tasks_in_time(sorted_tasks)
            
            st.success("Optimized Plan Generated!")
            display_data = [
                {"Priority": t.priority, "Task": t.description, "Duration": f"{t.time}m"} 
                for t in final_plan
            ]
            st.table(display_data)
            
            with st.expander("🔍 Logic Breakdown"):
                st.write(scheduler.explain_schedule(final_plan))