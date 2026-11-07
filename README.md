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



## Reflection on Version Control Throughout this development process, Git served as a reliable system for tracking progress and safeguarding my codebase. By dividing the project into distinct milestones, I utilized incremental commits—starting with the structural skeleton, adding core methods, and finally refining input validation. This approach allowed me to isolate errors quickly; when an index-handling bug arose during deletion logic, I could review my recent changes methodically. The primary benefit of version control was the structural organization it provided. Knowing I could safely experiment with refactoring loops without fear of permanently breaking a working script gave me greater confidence. The main challenge I encountered was handling non-integer inputs during menu selection, which I resolved by wrapping numeric parsing in robust `try-except` blocks. In a team-based project, version control is indispensable. Features like branching and pull requests allow multiple engineers to work on separate components—such as data persistence or user authentication—simultaneously without overwriting each other's code. Version history provides clear accountability, making it easier to merge codebases, resolve merge conflicts systematically, and review peer contributions prior to production release.
