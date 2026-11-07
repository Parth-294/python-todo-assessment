Markdown
# To-Do List Manager
A lightweight, robust command-line application built in Python designed to help users manage daily tasks efficiently while demonstrating object-oriented programming (OOP) principles and clean version control practices.

## Features
- Incremental Task Management: Easily add, view, complete, and delete tasks.
- Input Validation: Prevents application crashes from empty strings or invalid numeric menu selections.
- Modular Design: Utilizes a dedicated `TaskManager` class separate from the CLI control loop.

## How to Run
1. Ensure you have Python installed on your machine.
2. Open your terminal or command prompt, navigate to the project directory, and run:
   ```bash
   python todo_app.py


## Limitations
- Tasks are stored in volatile runtime memory (list); data does not persist after closing the application.

## Changelog
- v1.0.0: Initial repository creation and class skeleton.
- v1.1.0: Implemented core dictionary manipulation and display logic.
- v1.2.0: Added input error handling and interactive menu loop.

## Reflection on Version Control 
I used Git throughout this project to ensure that I had a reliable way to track my progress and keep my code safe. I broke down my project into milestones and made small commits to my code from building the skeleton, to implementing methods and adding input validation. This meant if there was an error in my code such as when I had an issue handling indexes when deleting data, I could easily look through my recent commits. Version control helped me keep my code well structured. Knowing I could safely play around with refactoring my loops gave me more confidence. The biggest issue I faced was handling non integer inputs when selecting from the menu. I solved this by using try except blocks when parsing integers. If this project was completed as a team version control would be extremely important. Branching and pull requests allow multiple engineers to work on different parts of the project such as saving data or authentication. Having a version history makes it clear who is responsible for what. It also makes merging code easier as you can easily identify merge conflicts and look through your peers code before it goes live.