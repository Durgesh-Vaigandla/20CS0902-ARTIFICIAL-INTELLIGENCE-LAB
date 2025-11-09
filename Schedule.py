people = ["Sandeep", "Hari", "Megh", "Satya", "Ishaan"]

busy = {
    "Sandeep": [("Monday", "10:00 AM")],
    "Hari": [("Monday", "10:00 AM"), ("Monday", "11:00 AM")],
    "Megh": [("Monday", "10:00 AM")],
    "Satya": [("Monday", "2:00 PM")],
    "Ishaan": [("Tuesday", "10:00 AM")]
}

default_day = "Monday"
default_time = "10:00 AM"
default_place = "Meeting Room 1"

possible_slots = [
    ("Monday", "10:00 AM"),
    ("Monday", "11:00 AM"),
    ("Monday", "2:00 PM"),
    ("Tuesday", "10:00 AM"),
    ("Tuesday", "11:00 AM")
]

def is_free(person, day, time):
    return (day, time) not in busy[person]

def find_meeting_time():
    for day, time in possible_slots:
        free_people = [p for p in people if is_free(p, day, time)]
        if len(free_people) == len(people):
            return day, time, default_place
    return None

print("Scheduling Meeting for:", ", ".join(people))
result = find_meeting_time()
if result:
    day, time, place = result
    print(f"\nMeeting Scheduled!")
    print(f"Day   : {day}")
    print(f"Time  : {time}")
    print(f"Place : {place}")
else:
    print("\nNo common free slot available.")
