# This script places loopback-ip-addresses in the hostfile,
# in order to block the websites entered at it's prompt.
# They can also be removed again.

def getBlockStr(domain):
    return "127.0.0.1" + ' ' + domain

def block(blockStr):
    with open(pathToHostsFile, 'a') as file:
        file.write('\n' + blockStr)

def unblock(blockStr):
    lines = []
    
    with open(pathToHostsFile, 'r') as file:
        for line in file:
            if blockStr not in line:
                lines.append(line)

    with open(pathToHostsFile, 'w') as file:
        file.write(''.join(lines))

chosenOption = -1
inputDomain = ""

# Path to real host-file on linux
pathToHostsFile = "/etc/hosts"

while (chosenOption != 0):
    chosenOption = int(input("""
    Please choose an option:
    1) block
    2) unblock
    0) exit
    """))
    
    match chosenOption:
        case 1:
            inputDomain = input("Please enter the domain you want to block: ")
            block(getBlockStr(inputDomain))
            print(inputDomain + " was blocked!")

        case 2:
            inputDomain = input("Please enter the domain you want to unblock: ")
            unblock(getBlockStr(inputDomain))
            print(inputDomain + " was unblocked!")

        case 0:
            print("Exiting!")
            
        case _:
            print("Wrong option, please choose again.")
