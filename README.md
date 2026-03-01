# CLI To-Do List

A beginner-friendly command-line to-do list app written in Python.

The program lets you add tasks with a date and time, view all saved tasks and delete tasks by their number.  
You can type `quit` at any time to exit and type `back` during the "Add task" flow to cancel and return to the menu.

---

## Features

- Add a task with date (DD/MM/YYYY), time (HH:MM) and task text
- View all tasks in a numbered list
- Delete tasks by number
- Input validation for dates, times and menu options
- `quit` command to exit at any time
- `back` command to cancel adding a task and return to the menu

---

## How It Works

The program runs in a continuous loop displaying a menu with four options:

1. Add a new task
2. View tasks
3. Delete tasks
4. Quit

When adding a task, the user is guided step-by-step through date,
time, and task input. If all inputs are valid, the task is stored in memory.

Tasks are saved in three internal lists:
- Date list
- Time list
- Task list

Each task is displayed in a numbered format for easy deletion.

---

## Usage

```bash
python to_do_list.py
```

---

## Example

```text
===== MENU OPTIONS =====
1. Add a new task
2. View the tasks
3. Delete tasks
4. Quit

Your choice: 1
```

---

## Project Structure

- `to_do_list.py` – main program file

---

## License

MIT
