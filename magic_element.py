def calc(ply,sear):
    total=0
    total_sum= sum(sear)
    for x in range(ply[0]):
        sum1 = sear[x]+ply[1]
        sum2 = total_sum- sear[x]
        if(sum1>sum2):
            total = total + 1
    return total



if __name__ == "__main__":
    cases = int(input())
    ply= [0]*2
    count=0
    for x in range(cases):
        ply = [int(x) for x in input().split()]
        sear = [0]*ply[0]
        sear = [int(x) for x in input().split()]
        sp=calc(ply,sear)
        print(sp)