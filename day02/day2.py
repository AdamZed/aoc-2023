import re

class Solution:

    def __init__(self, fname):
        self.data = self.parse_file(fname)
        self.ans1 = 0
        self.ans2 = 0

        self.solve()
        
        print(f'Part 1: {self.ans1}')
        print(f'Part 2: {self.ans2}')

    def parse_file(self, fname):
        with open(fname) as f:
            data = []
            for line in f.readlines():
                rolls = re.findall(r"([0-9]*) (red|blue|green)", line)
                game_rolls = [(int(count), col) for count, col in rolls]
                data.append(game_rolls)
            return data
                    
    def solve(self):
        M = {'red': 12, 'green': 13, 'blue': 14}
        possibles = []
        powers = []
        for game_idx, rolls in enumerate(self.data):
            impossible = False
            m = {'red': 0, 'green': 0, 'blue': 0}
            for count, colour in rolls:
                m[colour] = max(m[colour], count)
                if M[colour] < count:
                    impossible = True
            if not impossible: possibles.append(game_idx + 1)
            powers.append(m['blue'] * m['green'] * m['red'])
        self.ans1 = sum(possibles)
        self.ans2 = sum(powers)
            
if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)