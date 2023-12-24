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
                m = re.search(r"Game ([0-9]*): (.*)", line)
                game, rolls = m.groups()
                game_rolls = [g.strip() for s in rolls.split(";") for g in s.strip().split(",")]
                #[[g.strip() for g in s.strip().split(",")] for s in rolls.split(";")]
                data.append((game, game_rolls))
            return data
                    
    def solve(self):
        M = {'red': 12, 'green': 13, 'blue': 14}
        possibles = []
        for game, rolls in self.data:
            no = False
            for rset in rolls:
                count, colour = re.search(r'([0-9]*) (red|green|blue)', rset).groups()
                if M[colour] < int(count):
                    no = True
                    break
            if not no: possibles.append(int(game))
        self.ans1 = sum(possibles)
            
if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)