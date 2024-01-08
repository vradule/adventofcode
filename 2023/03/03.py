def get_input(file_name):
    file = open(file_name, "r")
    return file.read().split("\n")


def explore(grid, R, C, r, c):
    for rr in range(max(r - 1, 0), min(r + 2, R)):
        for cc in range(max(c - 1, 0), min(c + 2, C)):
            val = grid[rr][cc]
            if not (val.isdigit()) and val != ".":
                return (rr, cc, val)
    return None


def f(grid):
    nums = {}
    R, C = len(grid), len(grid[0])
    num, adj = "", None
    for r, row in enumerate(grid):
        for c, el in enumerate(row):
            if el.isdigit():
                num += el
                adj = adj or explore(grid, R, C, r, c)
            if len(num) and (not (el.isdigit()) or c == C - 1):
                if adj:
                    if not (adj in nums):
                        nums[adj] = []
                    nums[adj].append(int(num))
                num, adj = "", None

    res = [0, 0]
    for k, v in nums.items():
        res[0] += sum(v)
        if k[2] == "*" and len(v) == 2:
            res[1] += v[0] * v[1]
    return res


grid = get_input("example.txt")
assert f(grid) == [4361, 467835]

grid = get_input("input.txt")
res = f(grid)
print(res)
