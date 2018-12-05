'''
Log entry object

Holds a timestamp for the log entry (used for sorting)
And the activity for that log entry
'''

class Log:

    def __init__(self, ts, act):
        self.timestamp = ts
        self.activity = act
    