# miniinfo
import platform
import getpass
from datetime import datetime

print("=" * 30)
print("      MINIINFO TOOL")
print("=" * 30)

print("Operating System:", platform.system())
print("System Name:", platform.node())
print("Username:", getpass.getuser())
print("Date and Time:", datetime.now())

print("=" * 30)
print("Tool finished successfully!")
