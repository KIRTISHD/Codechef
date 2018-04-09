
def calc(N,A,B):
    A_max = 0
    B_max = 0
    A_sum = 0
    B_sum = 0
    for y in range(N):
        if A[y] > A_max:
            A_max = A[y]
        A_sum = A_sum + A[y]
        if B[y] > B_max:
            B_max = B[y]
        B_sum = B_sum + B[y]
    A_sum = A_sum - A_max
    B_sum = B_sum - B_max

    if A_sum < B_sum:
        return "Alice"
    if B_sum < A_sum:
        return  "Bob"
    if A_sum == B_sum:
        return "Draw"


if __name__ == "__main__":
    cases = int(input())
    ans = list()

    for x in range(cases):
        N = int(input())
        s = input()
        A = list(map(int, s.split()))
        s = input()
        B= list(map(int, s.split()))
        ans.append(calc(N,A,B))
    print(*ans, sep="\n")