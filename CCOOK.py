
def calc(A):
    A_max = 0
    for y in range(0,5):
        if (A[y] == 1):
            A_max = A_max+1
    if A_max == 0:
        return "Beginner"
    if A_max == 1:
        return "Junior Developer"
    if A_max == 2:
        return "Middle Developer"
    if A_max == 3:
        return "Senior Developer"
    if A_max == 4:
        return "Hacker"
    if A_max == 5:
        return "Jeff Dean"


if __name__ == "__main__":
    cases = int(input())
    ans = list()

    for x in range(cases):
        s = input()
        A = list(map(int, s.split()))
        print(calc(A))