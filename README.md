# PawPal+ AI: New Intelligent Pet Care System 

## Original Project: 

The goal of this project was to track daily pet routines designed for humans. The purpose includes manage different pet tasks easily and prioritize and organize them. It was meant to provide a basic interface for tracking daily pet routines including feeding and walks, while also calculating the total time requirements. 

## Project Title and Summary: 

PawPal+ AI is a pet care management system that includes Natural Language Processing (NLP) to handle pet routines. Most tradditional apps require manual data entry for task. But, PawPal+ AI allows owners to input their updates in plain English text, while the system using a specificaled AI classification model to parse these inputs, identify the underlying task, adn assign a dynamic priority level. By using a sorting algorithm, this new system automatically reorganizes the daily schedule making sure that important tasks (ex: medication related) are prioritized before leisure-related tasks. 

## Architecture Overview: 

# This system follows a modular archiecture consisting 4 different parts: 

- Pet and Task Models: These are the data entities and tasks now include an AI-generated priority attribute. 
- AI Interpreter: Classified raw text into structured data.
- Scheduler: Uses sorting algorithm to prioritze tasks 
- Streamlit UI: A modern web interface for user interaction and schedule visualization.

Set Up Instructions: 
1) Clone repo 
2) Install dependencies: pip install streamlit
3) Run System Demo: python3 main.py
4) Launch Web UI: streamlit run app.py

## Sample Interactions: 
# Example 1: 
- User Input: "Mochi is bleeding from his paw"
- AI Interpretation: Priority: 5 (Critical)
- Resulting Action: Flagged as URGENT and moved to top of schedule.

# Example 2: 
- User Input: "Feed Mochi dinner"
- AI Interpretation: Priority: 4 (Essential)
- Resulting Action: Added with emoji and prioritized above walks.

# Example 3: 
- User Input: "Time for a walk"
- AI Interpretation: Priority: 3 (Routine)
- Resulting Action: Added to schedule as an Exercise task.

## Desgin Decisions: 
- I used keyword-based specialized model approach for the interpreter.
- I implemented a two-tier sorting algorithm. It first sorts by Priority (descending) to ensure safety, and then by Time (ascending) to fit as many routine tasks as possible into the user's available window.
- I sacrificed "Natural Language Generation" in favor of "Natural Language Understanding" to make sure the system is a functional tool rather than just a chatbot.

## Testing Summary: 
- What worked: test_ai.py verified that emergency keywords ("blood", "meds") triggered Priority 5 with 100% accuracy.
- What Didn't: Ambiguous inputs like "Mochi is tired" were getting flagged as high priority.
- Learning: Reliability in AI systems comes from clear classification boundaries.

## Reflection: 
This project showed me that the best use of AI is not just making text, but organizing messy information. By changing a confusing sentence into a clear number, I helped solve a real problem: keeping pets safe on a busy day. It also showed me how important "Safe-Fail" designs are byy making sure that if the AI is unsure, it follows a safe and clear way.

# DEMO WALKTHROUGH: https://www.loom.com/share/41896cc07cb9431d9bac7956d4044ddc