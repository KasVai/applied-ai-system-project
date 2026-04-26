from pawpal_system import Owner, Pet, Task, Scheduler
from ai_interpreter import AIInterpreter

def main():
    # 1. Setup Core Entities
    owner = Owner("Alice Johnson", contact_info="alice@gmail.com")
    mochi = Pet("Mochi", "Dog")
    owner.add_pet(mochi)
    
    interpreter = AIInterpreter()
    
    print("=" * 70)
    print("🐾 PAWPAL+ AI SYSTEM - CLI VERIFICATION DEMO")
    print("=" * 70)

    # 2. Simulate Natural Language Inputs (The "Smart" part)
    raw_inputs = [
        "Mochi needs his heartworm medicine now",
        "Take Mochi for a quick 15 min walk",
        "Mochi is bleeding from his paw"
    ]

    print(f"\n📥 PROCESSING {len(raw_inputs)} NATURAL LANGUAGE INPUTS...")
    for text in raw_inputs:
        # AI Classifies the input
        data = interpreter.parse_input(text)
        
        # System creates a Task object with the AI's priority
        new_task = Task(
            description=data["desc"],
            time=data["time"],
            frequency=data["freq"],
            priority=data["priority"]
        )
        mochi.add_task(new_task)
        print(f"  ✅ Parsed: '{text}' -> Priority: {data['priority']}")

    # 3. Demonstrate Algorithmic Sorting
    scheduler = Scheduler(owner, available_time_minutes=60)
    all_tasks = scheduler.retrieve_all_tasks()
    
    print("\n" + "=" * 70)
    print("⚖️  ALGORITHMIC SCHEDULING (Priority High -> Low)")
    print("-" * 70)
    
    # Use your new sorting method
    optimized_tasks = scheduler.sort_by_priority_and_time(all_tasks)
    final_plan = scheduler.fit_tasks_in_time(optimized_tasks)

    for i, task in enumerate(final_plan, 1):
        print(f"{i}. [P: {task.priority}] {task.description} ({task.time}m)")

    # 4. Explain the Logic
    print("\n" + "=" * 70)
    print("🔍 SYSTEM REFLECTION")
    print("-" * 70)
    print(scheduler.explain_schedule(final_plan))
    print("=" * 70)

if __name__ == "__main__":
    main()