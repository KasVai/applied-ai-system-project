## Reflections 

# What are the limitations or biases in your system?
Some of the limitations or biases in my system are that it is still dependent on keyword classification. It relies on a specialized model instead of a large scale live language model, it still may fail to categorize some inputs that may be overly complicated or vague. There is also definitely bias toward high-priority safety tasks since the system it is designed to be fail safe, which means it may overprioritize certain symptoms in order to make sure no medical emergency is ignored. 

# Could your AI be misused, and how would you prevent that?
The AI could be misused if people use it as a replacement for professional veterinarians or as 100% accurate medical advice. Since the system may assign "Critical" priority to sumptoms like bleeding, user might mistaken the app as a medical professional instead of just organizing a schedule. To prevent this, the system emphasizes that it is clearly a prioritization tool for care management and not an official medical tool. 

# What surprised you while testing your AI's reliability?
It was surprising to see how much word choice impacted the priority score. For example, the system identified "bleeding" as priority 5, but struggled with "tired" which is common symptom of boredom and illness, both on different ranges of priority. This showed that AI reliability isn't about code accuracy, but also about creating clear boundaries for how machines could interpret human language and context.  

# Describe your collaboration with AI during this project. Identify one instance when the AI gave a helpful suggestion and one instance where its suggestion was flawed or incorrect.
The collaboration followed a "Lead Architect" workflow, where I defined the core logic and the AI assisted in generating the structured components to fulfill specific requirements. 

1 instance of a helpful suggestion was when the AI recommended implementing a sorting algorithm. So, instead of sorting by priority, it recommended sorting by priority and then by time duration which maximized the number of tasks completed within a given time frame. 

An incorrect suggestion was when AI recommended methods like detect_time_conflict and rank_tasks_by_priority which were not defined in the core pawpal_system.py. This would have causes the program to crash and this needed a manual refactor to make the backend code match the script. 
