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
        pass


if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)