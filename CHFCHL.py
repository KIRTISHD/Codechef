import math



def getparity(ch):
    parity = 0
    while (ch):
        parity = ~parity
        ch = ch & (ch - 1)
    return parity


def give(no_of_ch,ch,new_ch):
    meanch=math.floor(sum(ch)/int(no_of_ch))
    xor = meanch ^ int(new_ch)
    parity = getparity(int(new_ch))
    if parity==0 or (xor>=meanch):
        return True
    return False



if __name__ == "__main__":
    cases = int(input())
    no_of_ch = 0
    ch = list()
    new_ch=0

    for x in range(cases):
        no_of_ch = input()
        ch = [int(x) for x in input().split()]
        new_ch = input()
        an=give(no_of_ch,ch,new_ch)
        if (an == True):
            print ("yes")
        else:
            print ("no")