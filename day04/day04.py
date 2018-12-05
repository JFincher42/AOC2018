'''
Day 4, AoC 2018
'''

import datetime, guard, log, re

def part1():
    # Starting point
    log_entries = []
    guards = []
    guard_re = re.compile("([0-9]+)")

    # Open the file and read each line
    filename = "./day04/day04input.txt"
    #filename = "./day04/sample.txt"
    with open(filename, "r") as infile:
        for line in infile:
            # Skipping the first char, split the line based on the end of the timestamp
            parts = line[1:].split("] ")

            # Parse the timestamp, and create a new Log object using that timestamp
            date = datetime.datetime.strptime(parts[0],"%Y-%m-%d %H:%M")
            log_entries.append(log.Log(date, parts[1].strip()))

    # Sort the log entries so we can process them again
    log_entries.sort(key=lambda log: log.timestamp, reverse = False)

    # Now we can go through the log entries
    # We first look for a "Guard #" entry
    # After that, we look for a "falls asleep" entry, followed by a "wakes up"
    # We then process the guard entry with the time they were asleep

    current_entry = 0
    while current_entry < len(log_entries):
        match = guard_re.search(log_entries[current_entry].activity)
        if match:
            # Get the guard ID
            guard_id = int(match.group(0))
            current_entry += 1

            while current_entry < len(log_entries) and log_entries[current_entry].activity.startswith("falls"):
                # Find out when they fell asleep and woke up
                sleep_time = log_entries[current_entry].timestamp.minute
                current_entry += 1
                wake_time =  log_entries[current_entry].timestamp.minute
                current_entry += 1

                # Find the guard in the list - if he's not there, add him
                found_guard = False
                for i in range(len(guards)):
                    if guards[i].id == guard_id:
                        guards[i].set_sleep(sleep_time, wake_time)
                        found_guard = True
                        break
                if not found_guard:
                    new_guard = guard.Guard(guard_id)
                    new_guard.set_sleep(sleep_time, wake_time)
                    guards.append(new_guard)

    # Now we scan the list of guards and find the one with the highest sleep
    total_sleep = 0
    sleepy_guard = None

    for current_guard in guards:
        if current_guard.get_total_sleep() > total_sleep:
            total_sleep = current_guard.get_total_sleep()
            sleepy_guard = current_guard
    
    print(f"Sleepy guard is {sleepy_guard.id}, likely sleeptime is {sleepy_guard.most_likely_sleeptime()}, product is {sleepy_guard.most_likely_sleeptime() * sleepy_guard.id}.")

if __name__ == "__main__":
    part1()
    #part2()