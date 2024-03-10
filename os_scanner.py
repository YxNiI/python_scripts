import os
import platform


# Output data about the operating-system.

outputs: list[str] = ["System-Information:\n", "Operating-System: %s" % platform.platform()]
architecture_tuple: tuple[str, str] = platform.architecture()
outputs.append("Architecture: %s %s" % (platform.machine(), architecture_tuple[0]))
outputs.append("Linkage: %s" % architecture_tuple[1])
outputs.append("Network-Name: %s" % platform.node())

outputs.append("\nEnvironment-Variables:")
enviroVars: list[str] = ["USERNAME", "HOME", "LOGNAME", "DESKTOP_SESSION", "SHELL"]
for key, value in os.environ.items():
    if key in enviroVars:
        outputs.append(key + ": " + value)

os.system('clear')
print('\n'.join(outputs))
