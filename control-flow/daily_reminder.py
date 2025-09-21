# daily_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case for priority handling
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# If time-sensitive, append special message
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print final reminder
print("\nReminder:", reminder)

# Optional loop to keep reminding until user says stop
while True:
    again = input("\nDo you want to be reminded again? (yes/no): ").lower()
    if again == "yes":
        print("Reminder:", reminder)
    else:
        print("Okay, no more reminders for now.")
        break
