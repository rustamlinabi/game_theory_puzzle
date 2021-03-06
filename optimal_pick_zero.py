"""
"winner3" function returns "winner", a pick with highest probability of winning.
It also returns the probability of winning of each pick and the
list of picks by each player.

'sections' variable indicates into how many equal sections we want to divide
[0,1]. The higher the 'sections' variable, more precise will the result be,
but the code will run exponentially longer. Therefore, I use sections1 list
to gradually increase the sections, while trying to get more precise answer.

1)Now we will try to iterate through all possible combination of picks by B and C, given that A picks 0, and
add their respective results to our list 'wins'

2)Now we will try to find out optimal picks by players B and C, given that A is 0.

3)Optimal pick by B.

"""

def winner3(a,b,c,n):
    adicto={}
    under_control={"a":0,"b":0,"c":0}
    for t in range(0,n):
        numbo = {"a":abs(a-t),"b":abs(b-t),"c":abs(c-t)}
        for z in numbo:
            if numbo[z]==min(numbo["a"],numbo["b"],numbo["c"]):
                adicto[t]=z
    for x in adicto:
        for z in under_control:
            if adicto[x]==z:
                under_control[z]+=1
    win=None
    for z in under_control:
        valo = []
        for zeto in under_control.values():
            valo.append(zeto)
        if under_control[z]==max(valo):
            valo.remove(under_control[z])
            win=[z,[under_control["a"]/n, under_control["b"]/n, under_control["c"]/n],[a,b,c]]
    return win
wins=[]
sections1=[10,20,50,100,200]
minb=[0,1]
minc=[0,1]
winners=[]
awinscopy=[]
#1
for sections in sections1:
    wins = []
    winners = []
    awinscopy = []
    if minb[0]==0:
        beginb=0
        endb=sections
    else:
        beginb=int(minb[0]*sections)
        endb=min(sections,int(minb[1]*sections)+5)
    for awin in range(0,1):
        for bwin in range(beginb,endb):
            for cwin in range(0,sections):
                if awin==bwin or bwin==cwin or awin==cwin:
                    pass
                else:
                    initial=winner3(awin,bwin,cwin,sections)
                    wins.append(initial)
    #2
    awinscopy=[]
    for awin in wins:
        reck=None
        eck=0
        check=True
        for alt in wins:
            if awin[2][0]==alt[2][0] and awin[2][1]==alt[2][1]:
                if alt[1][2]>alt[1][1]:
                    check=False
                    break
                if alt[1][2]>eck:
                    eck=alt[1][2]
                    reck=alt[2]
        if check==True and reck==awin[2]:
            awinscopy.append(awin)
    print(len(awinscopy))
    #3
    winner=['b', [0, 0, 0], [0, 0, 0]]
    winners=[]
    boptimal=[]
    for z in awinscopy:
        if z[1][1] > winner[1][1]:
            winner = z
    for zet in awinscopy:
        if zet[1]==winner[1]:
            winners.append(zet)
    for zet in winners:
        boptimal.append(zet[2][1] / sections)
    minb=[(0.75*min(boptimal)),(1.25*max(boptimal))]

print("The optimal choices of B and C, given that the value of A is 0: ")
for z in awinscopy:
    print("Choices: A: 0, B:", z[2][1]/sections1[-1],"C:", z[2][2]/sections1[-1], ", probability of winning: ", z[1])

if len(winners)==1:
    print("The most optimal position for each player, given that A is 0,: B:", winners[0][2][1]/sections1[-1],"C:", winners[0][2][2]/sections1[-1])
else:
    print("Optimal positions for B and C, given that A is zero")
    for zet in winners:
        print("A:", zet[2][0]/sections1[-1], "B:", zet[2][1]/sections1[-1],"C:", zet[2][2]/sections1[-1])
