import matplotlib.pyplot as plt
import getpass
from   splib import command

# Get user name
username = getpass.getuser()

# Turn interactive mode on
plt.ion()

# sm command emulator
print('Hello ' + username + ', please give me a command')
command('default')
while True:
    a = input(': ')
    if a == 'q' or a == 'quit':
        break
    command(a)
