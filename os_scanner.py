# Analyzes data of the operating-system.
import os

outputs = []

outputs.append("Operating-System: %s" % (os.name))

enviroVars = ["USERNAME", "HOME", "LOGNAME", "DESKTOP_SESSION" "SHELL"]

outputs.append("Enviroment-Variables:")
for key, value in os.environ.items():
    if (key in enviroVars):
        outputs.append(key + ": " + value)

clear = lambda: os.system('clear')
clear()
print('\n'.join(outputs))
