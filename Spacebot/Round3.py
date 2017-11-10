







def MOV(num, Rxx, finalDict):
    if num.isnumeric():
        finalDict[Rxx] = int(num)
    else :
        finalDict[Rxx] = int(finalDict[num])
    return finalDict

def ADD(Rxx,Ryy, finalDict):
    finalDict[Rxx] = (int(finalDict[Rxx]) + int(finalDict[Ryy]))%(2^32)


def DEC(Rxx, finalDict):
    if finalDict[Rxx] == 0 :
        finalDict[Rxx] = (2^32) -1
    else :
        finalDict[Rxx] = int(finalDict[Rxx]) - 1


def INC(Rxx, finalDict):
    if finalDict[Rxx] == (2^32) -1 :
        finalDict[Rxx] = 0
    else :
        finalDict[Rxx] = int(finalDict[Rxx]) + 1

def INV(Rxx, finalDict):
     finalDict[Rxx] = int(~finalDict[Rxx])




subroutine =  ["DEC R42",
 "INC R01",
 "ADD R02,R01",
 "ADD R00,R02",
 "ADD R00,R42",
 "JZ 1"]




def cpuEmulator(subroutine):
    j = 0

    finalDict = {'R00':0,
                 'R01':0,
                 'R02':0,
                 'R03':0,
                 'R04':0,
                 'R05':0,
                 'R05':0,
                 'R07':0,
                 'R08':0,
                 'R09':0,
                 'R10':0,
                 'R11':0,
                 'R12':0,
                 'R13':0,
                   'R14':0,
                   'R15':0,
                   'R16':0,
                   'R17':0,
                   'R18':0,
                   'R19':0,
                   'R20':0,
                   'R21':0,
                   'R22':0,
                   'R23':0,
                    'R24':0,
                    'R25':0,
                    'R26':0,
                    'R27':0,
                    'R28':0,
                    'R29':0,
                    'R30':0,
                    'R31':0,
                    'R32':0,
                    'R33':0,
                    'R34':0,
                    'R35':0,
                    'R36':0,
                    'R37':0,
                    'R38':0,
                    'R39':0,
                    'R40':0,
                    'R41':0,
                    'R42':0}


    while j <= len(subroutine) - 1:
       # print(j)
       # print(subroutine[j])
        print(finalDict['R42'])
        if  subroutine[j] == 'NOP':
            j += 1
            continue

        if "," in subroutine[j]:
            cmd1, val = subroutine[j].split(',')
        else:
            cmd1 = subroutine[j]
        cmd11, val1 = cmd1.split(' ')
        if "MOV" == cmd11:
            MOV( val1,val, finalDict )
        if "ADD" == cmd11:
            ADD(val1 ,val , finalDict)
        if "DEC" == cmd11:
            DEC(val1, finalDict)
        if "JMP" == cmd11:
            j = int(val1) - 1
            continue

        if "JZ" == cmd11:
            if finalDict["R00"] == 0:
                j = int(val1) - 1
                continue

        if "INC" == cmd11:
            INC(val1, finalDict)

        if "INV" == cmd11:
            INV(val1, finalDict)

        j += 1
    return finalDict["R42"]

print(cpuEmulator(subroutine))