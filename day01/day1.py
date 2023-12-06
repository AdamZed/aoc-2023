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
        for line in self.data:
            nums1 = []
            nums2 = []
            for i, ch in enumerate(line):
                if ch.isdigit():
                    nums1.append(int(ch))
                    nums2.append(int(ch))
                for n, num in enumerate(["zero","one","two","three","four","five","six","seven","eight","nine"]):
                    if line[i:].startswith(num):
                        nums2.append(n)
            self.ans1 += nums1[0] * 10 + nums1[-1]
            self.ans2 += nums2[0] * 10 + nums2[-1]

if __name__ == "__main__":
    import sys
    filename = 'input.txt' if len(sys.argv) <= 1 else sys.argv[1] 
    Solution(filename)