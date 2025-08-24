import re
import subprocess
import time
from datetime import datetime

#Defining the switches,current time
switches = ["-log","-verbose", "-times", "-delay"]
current_datetime = datetime.now()
current_time = current_datetime.strftime("%H:%M:%S")

#Saving incorrect syntaxes to show the user it's mistake
incorrect_syntaxes = []
with open('to-do-list.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            #Checks if the line starts with "do" runs the command
            check_do = re.match(r'^do\b(.*)', line)
            if check_do:
                #Defines anything after "do" as a command
                command = check_do.group(1).split()[0]
                try:
                    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                    #Checks the used switchs in lines
                    for switch in switches:
                        if switch in line:
                            if switch == "-log":
                                with open("logs.txt", "a") as logs:
                                    logs.write("=============== \n")
                                    logs.write(f"{result.stdout} \n")
                            if switch == "-verbose":
                                print("Output:\n",result.stdout)
                            if switch == "-times":
                                check_times = re.search(r'-times\s+(\S+)', line)
                                if check_times:
                                    try:
                                        value_after_times = int(check_times.group(1))
                                        times = value_after_times
                                        if times > 0:
                                            with open("logs.txt", "a") as logs:
                                                while times != 0:
                                                    print(f"===[{current_datetime}]===")
                                                    logs.write(f"===[{current_datetime}]===")
                                                    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                                                    print(f"Output:\n{result.stdout}")
                                                    logs.write("=============== \n")
                                                    logs.write(f"{result.stdout}")
                                                    times -= 1
                                        else:
                                            print("The Value Of -times Must Be A Positive Number")
                                    except ValueError as e:
                                        print(f"[ERROR]: {e}")
                                else:
                                    print("Value Of -times Is Empty !")
                            if switch == "-delay":
                                check_delay = re.search(r'-delay\s+(\S+)', line)
                                if check_delay:
                                    try:
                                        value_after_delay = int(check_delay.group(1))
                                        delay = value_after_delay * 60
                                        
                                        if delay > 0:
                                            with open("logs.txt", "a") as logs:
                                                while delay != 0:
                                                    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                                                    print(f"Output:\n{result.stdout}")
                                                    logs.write("===============\n")
                                                    logs.write(f"{result.stdout}")
                                                    time.sleep(delay)
                                                    delay -= 60
                                        else:
                                            print("The Value Of -delay Must Be A Positive Number !")
                                    except ValueError as e:
                                        print(f"[ERROR]: {e}")
                                else:
                                    print("Value Of -delay Is Empty !")


                except subprocess.CalledProcessError as e:
                    print(f"[ERROR]: {e}")
                    with open("logs.txt", "a") as logs:
                        logs.write("=============== \n")
                        logs.write(f"[ERROR]: {e}\n")
            else:
                incorrect_syntaxes.append(line)

#Shows the user it's wrong syntaxes
if len(incorrect_syntaxes) > 0:
    for incorrect_syntax in incorrect_syntaxes:
        print(f"[{incorrect_syntax}] Add (do) At First")




###   ###    ########    ###########    ##########
###   ###    ##          ###      ###   ##      ##
#########    ########    ###########    ##      ##
###   ###    ##          ###    ##      ##      ##
###   ###    ########    ###     ##     ##########