import argparse

def main():
    command = dict()
    parser = argparse.ArgumentParser(prog="recovery automatic generator",description="given namefile and the z"+ 
                                     "where the print is stopped the program try to rebiold the remain gcode")
    parser.add_argument("filename",type= str,help="the name of the file witch is interrupted")
    parser.add_argument("zHeigth",type= float,help="the name of the file witch is interrupted")
    parser.add_argument("--noHome",action="store_true" )
    arg = parser.parse_args()
    fp = open(arg.filename,"r")
    output = open("RECOVERY_"+arg.filename,"w")
    for line in fp:
        if line[0] == ";" or line == "" or line =="\n":
            continue
        
        stringTemp = line.rstrip().split()
        if stringTemp[0] == "G28":
            if arg.noHome == False:
                output.writelines(line)
        elif stringTemp[0] == "G1":
            stringTemp.pop(0)
            for x in stringTemp:
                if x == ";":
                    break
                command[x[0]] = float(x[1:])
                if "Z" in command:
                    if command["Z"]  > arg.zHeigth:
                        output.writelines(line)     
        else:
            output.writelines(line)

main()