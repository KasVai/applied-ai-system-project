Original Project: PawPal+ AI: New Intelligent Pet Care System 

Original Project: The goal of this project was to track daily pet routines designed for humans. The purpose includes manage different pet tasks easily and prioritize and organize them. It was meant to provide a basic interface for tracking daily pet routines including feeding and walks, while also calculating the total time requirements. 

Project Title and Summary: PawPal+ AI is a pet care management system that includes Natural Language Processing (NLP) to handle pet routines. Most tradditional apps require manual data entry for task. But, PawPal+ AI allows owners to input their updates in plain English text, while the system using a specificaled AI classification model to parse these inputs, identify the underlying task, adn assign a dynamic priority level. By using a sorting algorithm, this new system automatically reorganizes the daily schedule making sure that important tasks (ex: medication related) are prioritized before leisure-related tasks. 

Architecture Overview: This system follows a modular archiecture consisting 4 different parts: 
- Pet and Task Models: These are the data entities and tasks now include an AI-generated priority attribute. 
- AI Interpreter: Classified raw text into structured data.
- Scheduler: Uses sorting algorithm to prioritze tasks 