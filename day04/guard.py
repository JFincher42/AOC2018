'''
Guard object

Holds the guards ID and the times they sleep

Provides methods for:
- adding to the sleep, 
- figuring out the total sleep time, and
- returning time they sleep the most
'''

class Guard:

    def __init__(self, id):
        self.id = id
        self.sleepcount = [0]*60

    def set_sleep(self, start, end):
        for minute in range(start,end):
            self.sleepcount[minute] += 1
        
    def get_total_sleep(self):
        return sum(self.sleepcount)

    def most_likely_sleeptime(self):
        max_sleep = max(self.sleepcount)
        for i in range(60):
            if self.sleepcount[i]==max_sleep:
                return i
    