"""
to_do_list.py

This is a CLI to-do list.

It's a beginner-friendly program made without using any AI tool.

Notes:
- Type 'quit' to exit the program.
- Type 'back' (inside Add flow) to cancel the current entry and return to the menu.

"""

WELCOME_MESSAGE = """
===== To-Do List =====

Welcome to my to-do list.

Enter your daily, weekly or monthly tasks you want to add to your to-do list.

"""

print(WELCOME_MESSAGE)

DATE_LIST = []
TASK_LIST = []
TIME_LIST = []

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

program_quit = False

while True:
    print("\n===== MENU OPTIONS =====")
    choice = input(
        "\n1. Add a new task: Type '1'."
        "\n2. View the tasks: Type '2'."
        "\n3.Delete tasks: Type '3'."
        "\n4. Quit: Type '4'."
        "\nYour choice: "
    ).strip()

    if choice == "1":
        # Flags used only during Add flow
        user_quit = False
        user_back = False

        # Day(DD)
        while True:
            date_input = input(
                "Enter the day number of the month (DD) (type 'back' or 'quit'):"
            ).strip()

            if date_input.lower() == "quit":
                user_quit = True
                break

            if date_input.lower() == "back":
                user_back = True
                break

            if date_input == "":
                print("Invalid input! Please enter a number!")
                continue

            is_valid_digits = True
            for char in date_input:
                if char not in DIGITS:
                    is_valid_digits = False
                    break

            if is_valid_digits is False:
                print("Only numbers are valid!")
                continue

            if len(date_input) != 1 and len(date_input) != 2:
                print("Day must be 1 or 2 digits!")
                continue

            day_number = int(date_input)

            if day_number < 1 or day_number > 31:
                print("Day must be between 1 and 31!")
                continue

            if day_number < 10:
                DD = "0" + str(day_number)
            else:
                DD = str(day_number)
            break

        # If user asked to quit/back, stop Add flow immediately
        if user_quit:
            program_quit = True
            # Break out of the Add flow and let the main loop exit cleanly
            # so we pring Goodbye once.
            # This break exits the "choice == 1" block (the main menu continues below)
            pass

        if user_back:
            # Cancel this entry and return to menu(do not continue to month/year/etc.)
            continue
        if program_quit:
            print("\nGoodbye! :-)")
            break

        # Month(MM)
        while True:
            month_input = input(
                "Enter the number of month (MM) (type 'back' or 'quit'):"
            ).strip()

            if month_input.lower() == "quit":
                user_quit = True
                break

            if month_input.lower() == "back":
                user_back = True
                break

            if month_input == "":
                print("Invalid input! Please enter a number:")
                continue

            is_valid_digits = True
            for char in month_input:
                if char not in DIGITS:
                    is_valid_digits = False
                    break

            if is_valid_digits is False:
                print("Only numbers are valid!")
                continue

            if len(month_input) != 1 and len(month_input) != 2:
                print("Month must be 1 or 2 digits!")
                continue

            month_number = int(month_input)

            if month_number < 1 or month_number > 12:
                print("Month must be between 1 and 12!")
                continue

            if month_number < 10:
                MM = "0" + str(month_number)
            else:
                MM = str(month_number)
            break

        if user_quit:
            program_quit = True
        if user_back:
            continue
        if program_quit:
            print("\nGoodbye! :-)")
            break

        # Year(YYYY)
        while True:
            year_input = input(
                "Enter the number of year (YYYY) (type 'back' or 'quit'):"
            ).strip()

            if year_input.lower() == "quit":
                user_quit = True
                break

            if year_input.lower() == "back":
                user_back = True
                break

            if year_input == "":
                print("Invalid input! Please enter a number.")
                continue

            is_valid_digits = True
            for char in year_input:
                if char not in DIGITS:
                    is_valid_digits = False
                    break

            if is_valid_digits is False:
                print("Only numbers are valid!")
                continue

            if len(year_input) != 4:
                print("Year must be 4 digits!")
                continue

            year_number = int(year_input)

            if year_number < 1900 or year_number > 2100:
                print("Enter a year number from 1900 to 2100.")
                continue

            YYYY = str(year_number)
            break

        if user_quit:
            program_quit = True
        if user_back:
            continue
        if program_quit:
            print("\nGoodbye! :-)")
            break

        # Hour(HH)
        while True:
            hour_input = input(
                "Enter the hour (00-23, 1-2 digits accepted) (type 'back' or 'quit'):"
            ).strip()

            if hour_input.lower() == "quit":
                user_quit = True
                break

            if hour_input.lower() == "back":
                user_back = True
                break

            if hour_input == "":
                print("Invalid input! Please enter an hour.")
                continue

            is_valid_digits = True
            for char in hour_input:
                if char not in DIGITS:
                    is_valid_digits = False
                    break

            if is_valid_digits is False:
                print("Only numbers are valid!")
                continue

            if len(hour_input) != 1 and len(hour_input) != 2:
                print("Hour must be 1 or 2 digits.")
                continue

            hour = int(hour_input)

            if hour < 0 or hour > 23:
                print("Invalid number! Please enter an hour from 0 to 23.")
                continue

            if hour < 10:
                HH = "0" + str(hour)
            else:
                HH = str(hour)
            break

        if user_quit:
            program_quit = True
        if user_back:
            continue
        if program_quit:
            print("\nGoodbye! :-)")
            break

        # Minute(MM)
        while True:
            minute_input = input(
                "Enter the minute (two-digits 00-59) (type 'back' or 'quit'):"
            ).strip()

            if minute_input.lower() == "quit":
                user_quit = True
                break

            if minute_input.lower() == "back":
                user_back = True
                break

            if minute_input == "":
                print("Invalid input! Please enter a number.")
                continue

            is_valid_digits = True
            for char in minute_input:
                if char not in DIGITS:
                    is_valid_digits = False
                    break

            if is_valid_digits == False:
                print("Only numbers are valid!")
                continue

            if len(minute_input) != 1 and len(minute_input) != 2:
                print("Minute must be 1 or 2 digits.")
                continue

            minute = int(minute_input)

            if minute < 0 or minute > 59:
                print("Invalid number! Please enter a number from 0 to 59.")
                continue

            if minute < 10:
                MMIN = "0" + str(minute)
            else:
                MMIN = str(minute)
            break

        if user_quit:
            program_quit = True
        if user_back:
            continue
        if program_quit:
            print("\nGoodbye! :-)")
            break

        # Task
        while True:
            task_input = input(
                "Enter the task you want to add (type 'back' or 'quit'):"
            ).strip()

            if task_input.lower() == "quit":
                user_quit = True
                break

            if task_input.lower() == "back":
                user_back = True
                break

            if task_input == "":
                print("Invalid task! Please enter a task.")
                continue

            break

        if user_quit:
            program_quit = True
        if user_back:
            continue
        if program_quit:
            print("\nGoodbye! :-)")
            break

        # Commint point: save only if everything is valid and not cancelled.
        complete_date = f"{DD}/{MM}/{YYYY}"
        complete_time = f"{HH}:{MMIN}"

        DATE_LIST.append(complete_date)
        TIME_LIST.append(complete_time)
        TASK_LIST.append(task_input.capitalize())

        print(
            f"Added: \n\tDate: {complete_date} \n\tTime: {complete_time} \n\tTask: {task_input.capitalize()}"
        )

    elif choice == "2":
        if len(TASK_LIST) == 0:
            print("\nNo tasks yet.")
        else:
            print("\nYour tasks so far:")
            for i in range(len(TASK_LIST)):
                print("\t", i + 1, ")", DATE_LIST[i], TIME_LIST[i], TASK_LIST[i])

    elif choice == "3":
        while True:
            if len(TASK_LIST) == 0:
                print("\nNo tasks to delete.")
                break
            else:
                print("Tasks:")
                for i in range(len(TASK_LIST)):
                    print("\t", i + 1, ")", DATE_LIST[i], TIME_LIST[i], TASK_LIST[i])

            del_input = input("Enter task number to delete(or 'back'):").strip()
            if del_input.lower() == "back":
                break

            if del_input == "":
                print("Invalid input! Please enter a number.")
                continue

            is_valid_digits = True
            for char in del_input:
                if char not in DIGITS:
                    is_valid_digits = False
                    break

            if is_valid_digits is False:
                print("Invalid choice! Please enter digits only.")
                continue

            num = int(del_input)

            if num < 1 or num > len(TASK_LIST):
                print("Invalid choice! Please try again.")
                continue

            idx = num - 1
            del DATE_LIST[idx]
            del TIME_LIST[idx]
            del TASK_LIST[idx]
            print("Deleted.")
            break

    elif choice == "4" or choice.lower() == "quit":
        program_quit = True
        print("\nGoodbye! :-)")
        break
    else:
        print("\nInvalid choice!")
    # If Add flow requested a program quit, exit here and print goodbye once.
    if program_quit:
        print("\nGoodbye! :-)")
        break
