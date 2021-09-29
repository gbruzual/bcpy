import matplotlib.pyplot as plt
import astropy.io.ascii as ascii
import numpy as np
import os
from   myfiles import xarg
from   myplots import plseds,pltext

def readdata(file):
    # Check if file exists in current directory
    if os.path.isfile(file):
        # If yes, open file and read it
        data = ascii.read(file)
        nl = len(data[0][:])
        nc = len(data[:][0])
        print('  ' + str(nl) + ' lines x ' + str(nc) + ' columns in table: ' + file)
        return data
    else:
        print("File '" + file + "' does not exist in this directory.")

def getcol(i):
    # Return values in ith-column
    global data
    if len(i) <= 0:
        n = 0
    else:
        n = int(i)-1
    x = data[n][:]
    return x

def getstr(s,p):
    # Return string entered as argument
    if len(s) < 0:
        print('Please enter ' + p + 'label')
    else:
        return s

# def showplot():
#    # fig.savefig("plot.pdf")
#    plt.show()
#    input('Continue?')
#    plt.close()

def points(filename):
    global x,y,xlabel,ylabel,title,ax
    fig, ax = plt.subplots(figsize=(8,8))
    #ax.set_xlim(xmin,xmax)
    #ax.set_ylim(ymin,ymax)
    ax.scatter(x,y,marker='.', s=5)	# , label=label)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # Turn on minor ticks!!
    ax.minorticks_on()
    plt.savefig('plot.png')
    plt.show()

def connect(a):
    global x,y,xlabel,ylabel,title,ax
    fig, ax = plt.subplots(figsize=(8,8))
    #fig, ax = plt.subplots()
    #xmin, xmax, ymin, ymax = -1, 15, 0, 1.10
    #ax.set_xlim(xmin,xmax)
    #ax.set_ylim(ymin,ymax)
    ax.plot(x, y,'black', linestyle='solid' , linewidth=3 , label='Label 1')
    # ax.plot(s,yI,'red',   linestyle='solid' , linewidth=3 , label='Label 2')
    # ax.plot(s,yR,'green', linestyle='solid' , linewidth=3 , label='Label 2')
    # ax.grid(True)
    ax.legend(loc='best')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # Turn on minor ticks!!
    ax.minorticks_on()
    plt.savefig('plot.png')
    plt.show()

def histogram(a):
    global x,y,xlabel,ylabel,title,ax
    fig, ax = plt.subplots(figsize=(8,8))
    ax.hist(x, color='red', histtype='bar', edgecolor='black', label='Label 1')
    ax.legend(loc='best')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    # Turn on minor ticks!!
    ax.minorticks_on()
    plt.savefig('plot.png')
    plt.show()

def readcols(a):
    a = a.replace('(','')
    a = a.replace(')','')
    a = a.replace('{','')
    a = a.replace('}','')
    a = a.replace('<','')
    a = a.replace('>','')
    print(a)
    # Define columns: {s 1 y 2 yI 3 yR 4 }
    # s  = d['col1'][:] y  = d['col2'][:] yI = d['col3'][:] yR = d['col4'][:]
    # file = 'N0_5_f_0.15.dat'
    # Define columns: read {s 1 y 2 yI 3 yR 4 }

def bcplot(argument):
    # Check for fits files
    sed, a = xarg(argument)
    # Draw plot
    if sed:
        plseds(a)
    else:
        pltext(a)

def command(a):
    # Decode command written in sm style
    global data,x,y,xlabel,ylabel,title
    i = a.find(' ')
    if i < 0:
        command  = a
        argument = ''
    else:
        command  = a[:i]
        argument = a[i+1:]

    if   command == 'dat' or command == 'data':
        data = readdata(argument)

    elif command == 'xc' or command == 'xcol' or command == 'xcolumn':
        x = getcol(argument)

    elif command == 'yc' or command == 'ycol' or command == 'ycolumn':
        y = getcol(argument)

    elif command == 'read':
        readcols(argument)

    elif command == 'bc' or command == 'bcplot' or command == 'mplot' or command == 'mp':
        bcplot(argument)

    elif command == 'xl' or command== 'xlab' or command == 'xlabel':
        xlabel = getstr(argument,'x')

    elif command == 'yl' or command== 'ylab' or command == 'ylabel':
        ylabel = getstr(argument,'y')

    elif command == 'title':
        title = getstr(argument,'')

    elif command == 'conn' or command == 'connect':
        connect(argument)

    elif command == 'histo' or command == 'histogram':
        histogram(argument)

    elif command == 'points':
        points(argument)

    elif command == 'show' or command == 'plot':
        showplot()

    elif command == 'default':
        xlabel = 'Xlabel'
        ylabel = 'Ylabel'
        title  = 'Title'

    else:
        # print('Unknown command: ' + command)
        data = readdata(command)
