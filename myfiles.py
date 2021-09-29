def head():
    print('Galaxy Spectral Evolution Library - GALAXEV')
    print('Python Version (C) 2020 - G. Bruzual and S. Charlot - All Rights Reserved')
    print()

def xarg(a):
    sed = False
    s = [""]*10
    s = a.split()
    for i in range(1,len(s)):
        if '.fits' in s[i] or '.ised' in s[i] or '.ased' in s[i]:
            sed = True
    return sed, s

def dtname():
    from datetime import datetime
    import os
    # datetime object containing current date and time
    now = 'FigG80_' + str(datetime.now()) 
    now=now.replace(':','')
    now=now.replace('-','')
    now=now.replace(' ','_')
    i=now.find('.')
    now=now[0:i+1] + 'png'
    # Home directory
    # home=os.path.expanduser('~')
    # now = home + '/python/g80/' + now
    return now

def saveplot(fig):
    s = input('Save plot to file (Y or [N]) ? ')
    if s == 'y' or s == 'Y':
        s = dtname()
        fig.savefig(s)
        print('Plot saved to file: ' + s)
                    
def geth(a,t):
    # Find number of records h[k] corresponding to age a[k] (in Gyr) selected by user
    import numpy as np
    n = len(a)				# Number of time steps requested
    i = [""]*(n+1)
    b = [""]*(n+1)
    k = 0
    for l in range(n):
        k = k+1
        b[k] = str(a[l])
        c = a[l]
        if c > 1.E3:
            c = c*1.E-9			# if age entered in yr transform to Gyr
        j = np.abs(t-c*1.E9).argmin()
        i[k] = int(j)+1
   #print(n,k,i,b)
    return k,i,b

def normwav(o):
    # Returns normalization wavelength
    wn = 0.
    if o=='n':
        wx = input('             Normalize SED''s at wavelength (A), press ENTER for no normalization = ')
    elif o=='N':
        wx = input('Normalize SED''s at wavelength (A), press ENTER for no normalization = ')
    else:
        wx=''
    if len(wx) > 0 and float(wx) > 0:
        wn = float(wx)
    return wn

def read_bcfits(ifile):
    # Reads fits table with BC models
    import warnings
    import os
    from   astropy.table import Table
    from   astropy.io import fits
    from   astropy.utils.exceptions import AstropyWarning
    
    # Read file in fits table format
   #with fits.open(os.getenv('GALAXEV') + '/fits/' + ifile) as hdul:
    with fits.open(ifile) as hdul:
        warnings.simplefilter('ignore', category=AstropyWarning)
        # Use Table to read the fits table
        f = Table.read(hdul,hdu=1)	# hdu = 1 => SED's (luminosity vs. wavelength)
        p = Table.read(hdul,hdu=2)	# hdu = 2 => galaxy physical properties
        m = Table.read(hdul,hdu=3)	# hdu = 3 => photometric magnitude in different bands
        d = Table.read(hdul,hdu=4)	# hdu = 4 => line spectral indices
        t = Table.read(hdul,hdu=5)	# hdu = 5 => time scale for spectral evolution (221 steps)
        t = t['age-yr']			# time scale without pre MS evolution (agrees with t for BC03 and C&B models)
        w = f['Wavelength']		# wavelength array
        a = 10.**m['logage']		# time scale without pre MS evolution (agrees with t for BC03 and C&B models)
        if a[0] < 10.:
            a[0]=0.			# change first time step to a = 0. It is written as 1 yr in the color files.
        h = hdul[1].header		# SED column header
        for i in range(len(t)+1):
            h[i] = h['TTYPE' + str(i+1)]
       #    print(i,h[i])
       #for i in range(len(t)+1):
       #    if i==0:
       #        s = 'Wavelength'
       #        u = 'A  (Wavelength)'
       #    else:
       #        c = t[i-1]
       #        if c < 10.E9:
       #            s = str('{:.5E}'.format(c))
       #        else:
       #            s = str('{:.4f}'.format(c*1.E-9)) + "E9"
       #        s = s.replace("E+0", "E")
       #        u = 'Lo/A  (SED at t = ' + s + ' yr)'
       #        s = s.replace(".", "p")
       #        s = 't' + s
       #    s = "sechdr['TTYPE" + str(i+1) + "']  = '" + s + "'"		# label for column i+1
       #    u = "sechdr['TUNIT" + str(i+1) + "']  = '" + u + "'"		# units for column i+1
       #    print (s)
       #    print (u)
       #print()
       #hdul.info()
       #print(hdul[0].header)
       #print(hdul[1].header)
       #print(hdul[2].header)
       #print(hdul[3].header)
       #print(hdul[4].header)
       #print(hdul[5].header)
       #sechdr = hdul[1].header
       #print(h['TTYPE1'])
       #print(h['TTYPE222'])
    print()
    print("In file " + ifile + " there are " + str('{:d}'.format(len(t))) + " galaxy SED's, from " + str('{:.1E}'.format(t[0])) +
          " to " + str('{:.1E}'.format(t[len(t)-1])) + " yr")
    print("Each SED covers the wavelength range from " + str('{:.1f}'.format(w[0])) + " to " + str('{:.1E}'.format(w[len(w)-1])) +
          " A in " + str('{:d}'.format(len(w))) + " steps")
    return w,f,t,h,m,d,p,a

def read_fits(ifile):
    # Reads SED from fits table (not necessarily a BC model)

    import warnings
    from   astropy.table import Table
    from   astropy.io import fits
    from   astropy.utils.exceptions import AstropyWarning
    
    # Read file in fits table format
    with fits.open(ifile) as hdul:
        warnings.simplefilter('ignore', category=AstropyWarning)
        # Use Table to read the fits table
        f = Table.read(hdul,hdu=1)      # hdu = 1 => SED's (luminosity vs. wavelength)
        h = Table.read(hdul,hdu=5)	# hdu = 5 => time scale for spectral evolution (221 steps)
        t = h['age-yr']			# time scale without pre MS evolution (agrees with t for BC03 and C&B models)
        w = f['Wavelength']             # wavelength array
    print()
    print("In file " + ifile + " there are " + str('{:d}'.format(len(t))) + " galaxy SED's, from " + str('{:.1E}'.format(t[0])) +
          " to " + str('{:.1E}'.format(t[len(t)-1])) + " yr")
    print("Each SED covers the wavelength range from " + str('{:.1f}'.format(w[0])) + " to " + str('{:.1E}'.format(w[len(w)-1])) +
          " A in " + str('{:d}'.format(len(w))) + " steps")
    return w,f,t

def bfits(ifile):
    # Reads SED from fits table (not necessarily a BC model)

    import warnings
    from   astropy.table import Table
    from   astropy.io import fits
    from   astropy.utils.exceptions import AstropyWarning
    
    # Read file in fits table format
    with fits.open(ifile) as hdul:
        warnings.simplefilter('ignore', category=AstropyWarning)
        # Use Table to read the fits table
        f = Table.read(hdul,hdu=1)         # hdu = 1 => SED's (luminosity vs. wavelength)
        p = Table.read(hdul,hdu=2)         # hdu = 2 => galaxy physical properties
        w = f['Wavelength']                # wavelength array
        t = p['Age']                       # time scale array
    print()
    print("In file " + ifile + " there are " + str('{:d}'.format(len(t))) + " galaxy SED's, from " + str('{:.1E}'.format(t[0])) +
          " to " + str('{:.1E}'.format(t[len(t)-1])) + " yr")
    print("Each SED covers the wavelength range from " + str('{:.1f}'.format(w[0])) + " to " + str('{:.1E}'.format(w[len(w)-1])) +
          " A in " + str('{:d}'.format(len(w))) + " steps")
    return w,f,t,p

def fcheck(file):
    # Checks if file exists in current directory
    import os
    while True:
       #if os.path.isfile(os.getenv('GALAXEV') + '/fits/' + file):
        if os.path.isfile(file):
            break
        else:
           file = input('File ' + file + ' does not exist. Enter new file name = ')
    return file

def inputc(a):
    # Ask for file name and check that file exists
    file = input(a + ' = ')
    if len(file) > 0:
        file = fcheck(file)
    return file

def geta():
    # Ask for time steps to plot
    import numpy as np
    input_string = input('Enter age of sed''s to plot (separated by space) = ')
    userList = input_string.split()
    a = np.array(userList, dtype=np.float32)
    for i in range(len(a)):         # if age entered in yr transform to Gyr
        if a[i] > 1.E3:
            a[i] = a[i]*1.E-9
    a = np.unique(a)                # unique sorts array a and suppresses duplicate entries (no need for a = np.sort(np.unique(a)))
    return a

def read_bcised(ifile):

    # Read *.ised binary file written by the galaxev fortran code
    import numpy as np
    from scipy.io import FortranFile

    # Comments by GBA 02.02.2020 (Madrid):
    #     The read_record function in FortranFile does not accept combining integer and float values in a single read
    #     A practical solution is to open the file once to read nt, nw, and ni as integer numbers, and then
    #     open the file again to read:
    #         t = time scale (nt steps)
    #         w = wavelength (nw points)
    #         f = sed fluxes (nw points, nt times)
    #         h = line index (ni points, nt times)
    #         p = phys prop  (nt points, 16 properties)

    # Open file to read 3 first records as integer
    with FortranFile(ifile) as file:
        # Read 1st record and get number nt of time steps
        d = file.read_record(dtype=np.int32)
        nt = d[0]
        # Read 2nd record and get number nw of wavelength points
        d = file.read_record(dtype=np.int32)
        nw = d[0]
        # Read 3rd record and get number ni of line index fluxes written after sed
        d = file.read_record(dtype=np.int32)
        ni = d[nw+1]
        # print(nt,' time steps')
        # print(nw,' wavelength points')
        # print(ni,' line index fluxes')

    # Open file again to read all record as float
    with FortranFile(ifile) as file:
        # Read 1st record with time scale
        d = file.read_record(dtype=np.float32)
        t = d[1:nt+1]
        h = []
        h.append(t[1:nt+1])			# flux
        p=[]
        p.append(t[1:nt+1])			# flux
        # Read 2nd record with wavelength scale
        d = file.read_record(dtype=np.float32)
        w = d[1:nw+1]
        f = []
        f.append(w[1:nw+1])			# flux
        # Read nt records with flux and line index evolution
        for i in range(nt):
            d = file.read_record(dtype=np.float32)
            f.append(d[1:nw+1])			# flux
            if nw != 56:
                h.append(d[nw+2:])		# line indices (not for ised files in JPAS filter system)
        # Read 16 records with physical properties for this model
        if nw != 56:
            for i in range(16):
                d = file.read_record(dtype=np.float32)
                p.append(d[1:])			# physical properties
        # Build array with number of time step
        a = []
        for i in range(len(t)+1):
            a.append(i)
    # Report file content
    print()
    print("In file " + ifile + " there are " + str('{:d}'.format(len(t))) + " galaxy SED's, from " + str('{:.1E}'.format(t[0])) +
          " to " + str('{:.1E}'.format(t[len(t)-1])) + " yr")
    print("Each SED covers the wavelength range from " + str('{:.1f}'.format(w[0])) + " to " + str('{:.1E}'.format(w[len(w)-1])) +
          " A in " + str('{:d}'.format(len(w))) + " steps")

    # Return arrays
    # return w,f,t,h,p		# uncomment if h and p are needed
    return w,f,t,a

def read_bcased(ifile):

    # Read *.ased ascii file written by the galaxevpl fortran code
    import numpy as np
    import astropy.io.ascii as ascii

    # Read time scale from header
    k = 0
    print()
    print('Reading text file: ' + ifile + ' will take a few seconds')
    with open(ifile, 'r') as f:
        for line in f:
            k = k+1
            h = line
            if k == 6:
                h = h.replace('# Lambda(A)',' 0.00E+00  ')
                h = h.split()
                h = np.array(h,dtype=np.float32)
                t = [0]
                t = h[1:]
                break

    # Read seds at all ages
    f = ascii.read(ifile)
    w = f[0][:]

    # Build array with number of time step
    a = []
    for i in range(len(t)+1):
        a.append(i)

    # Report file content
    print("In file " + ifile + " there are " + str('{:d}'.format(len(t))) + " galaxy SED's, from " + str('{:.1E}'.format(t[0])) +
          " to " + str('{:.1E}'.format(t[len(t)-1])) + " yr")
    print("Each SED covers the wavelength range from " + str('{:.1f}'.format(w[0])) + " to " + str('{:.1E}'.format(w[len(w)-1])) +
          " A in " + str('{:d}'.format(len(w))) + " steps")

    return w,f,t,a

def read_sed(ifile):

    # Reads various format of sed files
    import os
    from myfiles import read_fits, read_bcised, read_bcased

    # Choose correct file format
    if '.fits' in ifile:
        # Read .fits file
        w,f,t = read_fits(ifile)
    elif '.ised' in ifile:
        # Read .ised file
        w,f,t = read_bcised(ifile)
    #lif '.ased' in ifile:
    else:
        # Read .ased file or any ascii table (galaxevpl output)
        w,f,t = read_bcased(ifile)
    #lse:
    #   # Unknown file type
    #   print('Unknown file type ' + ifile)
    #   exit()
    return w,f,t
