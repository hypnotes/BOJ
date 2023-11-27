import math
ahp, aatt, bhp, batt = map(int,input().split())
bp, bs = map(int,input().split())
sflag = 1


def game(limit):
    global ahp, aatt, bhp, batt, bs, sflag
    
    hits = (bhp-limit)//aatt

    bhp = bhp - (aatt*hits)
    ahp = ahp - (batt*hits)

    if ahp < 0:
        print("gg")
        return
    
    bhp -= aatt 
    if bhp < bp and sflag:
        bhp+=bs 
        sflag = 0
    elif bhp < 0:
        print("Victory!")
        return
    
    ahp -= batt
    if ahp < 0:
        print("gg")
        return 
    elif bhp < aatt:
        print("Victory!")
        return 
    else:
        game(0)
        


game(bp)