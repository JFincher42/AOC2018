'''
Day 9, AoC 2018
'''

from collections import deque

def part1():
    # Input data
    player_count = 468
    last_marble = 71010 * 100

    # Sample Input data
    # player_count = 10
    # last_marble = 1618

    # Setup
    marbles = deque([0,1],maxlen=last_marble+1)
    players = [0]*player_count

    round = 2
    current_player = 0
    while round <= last_marble:
        # Is this marble divisble by 23?
        if round % 23 > 0:
            # Spin the deque counter-clockwise, so [0] is a clockwise step
            marbles.rotate(-2)
            marbles.appendleft(round)
        else:
            # Add the current marble to the current player's score
            players[current_player] += round
            # Spin clockwise, so we step counter-clockwise
            marbles.rotate(7)
            # Remove this marble, and add it to the players score
            players[current_player] += marbles.popleft()
        # Next player, next round
        current_player = (current_player+1) % player_count
        round += 1

    print(f"Part 1: Max score is {max(players)}")
        


if __name__ == "__main__":
    part1()