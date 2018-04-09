def calc(A):
    st = "chef"
    if st in A:
        return True
    else:
        return False



if __name__ == "__main__":
    cases = int(input())
    count=0
    for x in range(cases):
        s = input()
        sp=calc(s)
        if(s==True):
            count = count + 1
    print(count)