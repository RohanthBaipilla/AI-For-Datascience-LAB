import sys
input = sys.stdin.readline

MOD = 1000000007
SIZE = int(1e6) + 2

def kk():
    kik, kikk, kikkk, w = map(int, input().split())
    ij = 0
    ijk = 1
    ans = 0
    for i in range(kik):
        for i in range(kik):
            t = int(input())
            if ij == 0 or ijk <= t:
                ans += 1
                ij = kikk - 1
                ijk = t + w + kikkk + 1
            else:
                ij -= 1
    print(ans)

def main():
    t = int(input())
    for i in range(t):
        kk()

if __name__ == '__main__':
    main()
