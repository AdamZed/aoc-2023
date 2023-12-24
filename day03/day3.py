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
            return [x for x in f.read().strip().split()]
            
    def solve(self):
        DIRS = {(-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)}
        parts = []
        for x, line in enumerate(self.data):
            current_num = ''
            is_part = False
            for y, char in enumerate(line):
                if char.isdigit():
                    current_num += char
                    for dir in DIRS:
                        dx, dy = x + dir[0], y + dir[1]
                        if not (0 <= dx < len(self.data) and 0 <= dy < len(line)): continue
                        c = self.data[dx][dy] 
                        if not c.isdigit() and c != '.': is_part = True
                else:
                    if is_part: parts.append(int(current_num))
                    current_num = ''
                    is_part = False
            if is_part: parts.append(int(current_num))

        self.ans1 = sum(parts)



if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)