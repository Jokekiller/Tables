#Harry Robinson
#05-01-2015
#tables program

players = [
    ["killmAchine", 51, 49],
    ["Bob2247",5,99],
    ["hAxOr12",72,30]
]
table=(players)
def table(table):
    print("-"* 30)
    print("{0:<12} {1:<6} {2:<3}".format("Name", "Kills", "Deaths"))
    print("-"* 30)
    for count in range(3):
        print("{0:<12} {1:<6} {2:<3}".format(players[count][0],players[count][1],players[count][2])) 
        print("-"* 30)
    return
#main program
table(table)
