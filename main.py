import os
import time
from random import randint
from constants import enemynames

def get_file(name,operation):
    # operation is "r" or "w" or whatever
    try: # a read only file
        return(open("data//{}//enemyparm.txt".format(name), mode=operation, encoding = 'iso-8859-15'))
    except:
        print("Thought you ought to know, but there was no enemyparm.txt file in data/{}.".format(name))
        return(False)

def randomize_file(name,mod,randomness,lean,safe): # where it all happens
    # mod is the max multiplier/divisor
    i = 0
    parmfile = get_file(name,"r")
    newfile = ""

    # check for special cases which don't have certain parameters
    if name not in ["imomushi","pelplant","pom","shijimichou"]:
        end = 49
    elif name in ["pelplant","pom","shijimichou"]:
        end = 46
    elif name in ["imomushi"]:
        end = 48
        
    for line in parmfile:
        # now start the line parsing and randomizing]
        if ((i > 1 and i < 7) or (i > 10)) and line[0] == "\t": # if there is a parameter
            if line[2] != "_" and line[10] != "-":
                number = randint(1*randomness,mod*randomness) / randomness
                if randint(0,1):
                    number = 1 / number

                if i >= end:
                    # if the parameter has only 1 or 3 digits or something
                    digits = 0
                    for char in line[10:]:
                        if char.isnumeric():
                            digits += 1
                        elif char == ".":
                            digits = 8
                            break
                        else:
                            break
                    #print(digits)
                    number = '{:.10f}'.format(float(line[10:10+digits]) / number * lean)
                    
                    # now do the digits thing
                    #print(digits,len(str(int(float(number) // 1))))
                    if digits != 8:
                        if len(str(int(float(number) // 1))) > digits:
                            number = ""
                            while len(number) != digits:
                                number += "9"
                        elif digits > len(str(int(float(number) // 1))):
                            digits = len(str(int(float(number) // 1)))
                    number = number[:digits]

                    if digits == 8:
                        while len(number) < 8:
                            number += "0"
                    #print(number)
                    # now construct the line
                    newline = line[:10]
                    for char in number:
                        newline = newline + char

                    newline = newline + line[11+digits]
                    if line[12+digits] == "#":
                        newline = newline + "\t" + line[12+digits:]
                    else:
                        newline = newline + line[12+digits:]
                else:
                    #print(i,end,number)
                    number = '{:.10f}'.format(float(line[10:18]) / number * lean)
                    number = number[:8]
            
                    while len(number) < 8:
                        number += "0"

                    # now construct the line
                    newline = line[:10]
                    for char in str(number):
                        newline = newline + char

                    newline = newline + line[19]
                    if line[20] == "#":
                        newline = newline + "\t" + line[20:]
                    else:
                        newline = newline + line[20:]

                
                newfile += newline
                #print(newline)
            else:
                newfile += line
        else:
            newfile += line
        i += 1
    #print(newfile)
    if safe != "y":
        parmfile = get_file(name,"w")
        parmfile.write(newfile)
    else:
        print(newfile)
    parmfile.close()

#randomize_file("tobi",2.0,2.0,1.0)

_initing = True
input("Hello there. I trust you have placed your extracted enemyParms.szs data folder in the same directory as this program and made backups of it just in case? ")
safemode = input("If you would like to enter safe mode, input y here -> ")
mode = int(input("\nGood. Now, would you like to:\n(1) Randomize every enemy\n(2) Randomize specified enemies\n Well? 1 or 2? "))
while mode not in [1,2]:
    mode = input("That's not 1 or 2. Try again -> ")
if safemode != "y":
    assurance = input("\nThis operation will overwrite files in the data folder. You are not in safe mode, after all. Press enter to consent.")

if mode == 2:
    still_randomizing = "y"
    while still_randomizing == "y":
        name = input("Which enemy's enemyparm.txt file would you like randomized? (Technical identifiers only) -> ")
        mod = input("Maximum random multiplier: ")
        randomness = input("Randomness multiplication modifier: ")
        lean = input("End product multiplier (lean) (no negative numbers): ")
        try:
            randomize_file(name,float(mod),float(randomness),float(lean),safemode)
        except:
            print("Error! {} {} {} {}".format(name,mod,randomness,lean))
        
        still_randomizing = input("Would you like to randomize another enemy? (y) -> ")
elif mode == 1:
    mod = input("Maximum random multiplier: ")
    randomness = input("Randomness multiplication modifier: ")
    lean = input("End product multiplier (lean) (no negative numbers): ")

    for enemy in enemynames.keys():
        if safemode:
            print("--" + enemy + "--")
        try:
            randomize_file(enemy,float(mod),float(randomness),float(lean),safemode)
        except:
            print("Error! {} {} {} {}".format(enemy,mod,randomness,lean))
    input("\nThere you go.")
else:
    print("Error! How the hell did you get here?")

