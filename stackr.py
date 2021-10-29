from stackr_commands import stackr
import sys

stackr = stackr()

if len(sys.argv) == 1:
    while True:
        text = input(">>>")
        stackr.run_command(text)
elif len(sys.argv) > 1:
    droppedfile = sys.argv[1]
    droppedfile = open(droppedfile, "r")
    lines = droppedfile.readlines()

    for line in lines:
        line.strip("\n")
        stackr.run_command(line)

input()