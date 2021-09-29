def mfile():
    from myfiles import inputc
    # Ask for name of up to 2 fits file
    file1 = inputc('BC/CB model in fits table file name (model 1)')
    n = 1
    if len(file1) > 0:
        n = n+1
    else:
        quit()
    file2 = inputc('      model in fits table file name (model 2)')
    if len(file2) > 0:
        n = n+1
        if (n == 2):
            file1 = file2
    return n,file1,file2

def gpl(a):

    import os
    from myfiles import head,fcheck
    from galaxev import fplot
    from galcomp import fplot2
    import mywidgets
    from mywidgets import select_file,namewidget
    import matplotlib.pyplot as plt

    # Header
    head()

    # Check if running from command line or Jupyter Notebook
    if str(a).find("Jupyter") < 0:
        # Running from command line
        jupy = False

        # Number of arguments in command line
        n = len(a)

        # Make sure correct files are in use
        if str(a).find("fits") < 0 and str(a).find("ised") < 0 and str(a).find("ased") < 0 and str(a).find("all") < 0:
            n=1
    
        if n==3:
            # Assumes name of 2 files has been entered in command line
            file1 = fcheck(a[1])
            file2 = fcheck(a[2])
        elif n==2:
            # Assumes name of 1 file has been entered in command line
            file1 = fcheck(a[1])
        else:
            # Ask for name of up to 2 file
            n,file1,file2 = mfile()
    else:
        # Running Jupyter Notebook
        jupy = True
        if os.path.isfile(os.getenv('PYTHON') + '/tmp/file1.tmp'):
            n = 2
            # select_file(1)
            of = open(os.getenv('PYTHON') + '/tmp/file1.tmp',"r")
            file1 = of.read()
            of.close()
            os.remove(os.getenv('PYTHON') + '/tmp/file1.tmp')
            # select_file(2)
            if os.path.isfile(os.getenv('PYTHON') + '/tmp/file2.tmp'):
                n = 3
                of = open(os.getenv('PYTHON') + '/tmp/file2.tmp',"r")
                file2 = of.read()
                of.close()
                os.remove(os.getenv('PYTHON') + '/tmp/file2.tmp')
        else:
            # Ask for name of up to 2 fits file
            n,file1,file2 = mfile()

    # Choose ith plot style
   #plt.style.use(fstyle(5))
   #plt.style.use(fstyle(1))

    # Turn interactive mode on
    plt.ion()

    # Read BC/CB models from fits table and call plotting functions
    while True:
        if n==3:
            # Plot selected options for two files
            n = fplot2(file1,file2,n)
        elif n==2:
            # Plot selected options for one file
            n = fplot(file1,n)
        elif n==0:
            # Ask for name of up to 2 fits file
            print()
            n,file1,file2 = mfile()
        elif n==1:
            if jupy:
               break
            else:
               quit()

def plmenu(k):
    # Print plot menu
    if k==0:
        # Fits file options:
        print()
        print('Plot:    s - SEDs')
        print('         n - SEDs (normalized)')
        print('         m - photometric magnitudes')
        print('         c - photometric colors')
        print('         i - line strength indices')
        print('         p - physical properties')
        print('         f - enter new fits files')
        print('         q - quit')
    else:
        # ised and ascii file options:
        print()
        print('Plot:    s - SEDs')
        print('         n - SEDs (normalized)')
        print('         f - enter new file name')
        print('         q - quit')
    o = input('choice = ')
    return o

def fplot(ifile,n):

    global qf
    from myfiles import read_bcfits, read_bcised, read_bcased, normwav 
    from myplots import fstyle

    # Choose correct file format
    if '.fits' in ifile:
        # Read fits table
        w,f,t,h,m,d,p,a = read_bcfits(ifile)
        k = 0
        qf = True
    elif '.ised' in ifile:
        # Read .ised file
        w,f,t,h = read_bcised(ifile)
        k = 1
        qf = False
    else:
        # Read .ased file or any ascii table (galaxevpl output)
        w,f,t,h = read_bcased(ifile)
        k = 1
        qf = True

    while True:
        # Select plot option
        o = plmenu(k)
        if o=='s' or o=='n':
            wn = normwav(o)
            fgpl(ifile,w,f,t,h,wn)
        elif o=='c':
            fcol(ifile,a,m)
        elif o=='m':
            fmag(ifile,a,m)
        elif o=='i':
            fidx(ifile,a,d)
        elif o=='p':
            fphy(ifile,a,p)
        elif o=='f':
            n=0
            return n
        elif o=='q':
            n=1
            return n
        else:
            print('Unknown option: ' + o)

def fgpl(ifile,w,f,t,h,wn):

    # Extracts model SED at age indicated in argument list (GBA, Dec. 2019)

    from myfiles import geta
    from myplots import plsed1

    # Detect if BC03 or CB20 model according to last time step
    e = round(t[len(t)-1]*1.E-9)	# Last time step rounded to nearest integer in Gyr
    if e > 16:
        bc = True                 # BC2003 models reach 20 Gyr
    else:
        bc = False                # CB2020 models reach 14 Gyr

    while True:
        # Ask for time steps to print
        print()
        a=geta()
        if len(a) <= 0:
            break
        a = a[a <= e]			# keep only requested ages <= maximum age

        # Plot sed's
        plsed1(w,f,t,h,a,bc,ifile,qf,wn)

def fcol(ifile,t,m):

    # Plot selected color sets

    import os
    from myplots import splt,nplt

    while True:
        # Ask for colors to plot
        print()
        print('Select colors to plot (press <Enter> to exit loop):')
        print('         1: UBVRIJKL - Johnson')
        print('         2: UBVRIJKL - Johnson-Cousins')
        print('         3:    ugriz - SDSS')
        print('         4: User selected colors')
        op = input( 'choice = ')

        # Plot colors
        if (op == '1'):
            lh = ['U_Johnson','B2_Johnson',  'B3_Johnson','V_Johnson',  'V_Johnson','R_Johnson',
                  'R_Johnson','I_Johnson',   'I_Johnson','J_Johnson',   'J_Johnson','K_Johnson',
                  'K_Johnson','L_Johnson',   'V_Johnson','J_Johnson',   'V_Johnson','K_Johnson']
            ly = ['U - B', 'B - V', 'V - R', 'R - I', 'I - J', 'J - K', 'K - L', 'V - J', 'V - K']
            splt(3,3,t,m,lh,ly,False)

        elif (op=='2'):
            lh = ['U_Johnson','B2_Johnson',  'B3_Johnson','V_Johnson',  'V_Johnson','R_Cousins',
                  'R_Cousins','I_Cousins',   'I_Cousins','J_Johnson',   'J_Johnson','K_Johnson',
                  'K_Johnson','L_Johnson',   'V_Johnson','J_Johnson',   'V_Johnson','K_Johnson']
            ly = ['U - B', 'B - V', 'V - R$_c$', 'R$_c$ - I$_c$', 'I$_c$ - J', 'J - K', 'K - L', 'V - J', 'V - K']
            splt(3,3,t,m,lh,ly,False)
         
        elif (op=='3'):
            lh = ['u_SDSS_AB','g_SDSS_AB',   'g_SDSS_AB','r_SDSS_AB',   'r_SDSS_AB','i_SDSS_AB',   'i_SDSS_AB','z_SDSS_AB']
            ly = ['u - g', 'g - r', 'r - i', 'i - z']
            splt(2,2,t,m,lh,ly,False)

        elif (op=='4'):
            n,f,l = ucol(m)
            if n < 0:
                break
            nplt(n,t,f,l,False)
        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',ifile.replace('fits','color') + op + ".png")

def fidx(ifile,t,m):

    # Plots selected line indices

    import os
    from myplots import yl,splt,nplt

    while True:
        # Ask for indices to plot
        print()
        print('Select indices to plot (press <Enter> to exit loop):')
        print('         1: Lick Indices  1:15')
        print('         2: Lick Indices 16:21 + WO + Marcillac et al. indices')
        print('         3: DTT + HK + B4000vn indices')
        print('         4: Fanelli et al. UV indices')
        print('         5: Fanelli et al. UV indices (cont.)')
        print('         6: User selected indices')
        op = input( 'choice = ')

        # Plot indices
        if (op == '1'):
            # Lick indices 1:15
            l = ['CN1:m', 'CN2:m', 'Ca4227', 'G4300', 'Fe4383', 'Ca4455', 'Fe4531', 'Fe4668', 'Hbeta', 'Fe5015', 'Mg1:m', 'Mg2:m', 'Mgb', 'Fe5270', 'Fe5335']
            lh,ly = yl(l)
            splt(5,3,t,m,lh,ly,False)

        elif (op == '2'):
            # Lick indices 16:21 + WO + Marcillac et al. indices
            l = ['Fe5406', 'Fe5709', 'Fe5782', 'NaD', 'TiO1:m', 'TiO2:m', 'HdeltaA', 'HgammaA', 'HdeltaF', 'HgammaF', '', '', 'H83889', 'H93835', 'H103798']
            lh,ly = yl(l)
            splt(5,3,t,m,lh,ly,False)

        elif (op=='3'):
            # DTT + HK + B4000 indices
            l = ['CaII8498', 'CaII8542', 'CaII8662', 'MgI8807', '', '', 'BHHK', '', '', 'B4000VN:n', '', '', '', '', '']
            lh,ly = yl(l)
            splt(5,3,t,m,lh,ly,False)

        elif (op=='4'):
            # Fanelli et al UV indices
            l = ['BL1302','SiIV','BL1425','Fe1453','CIV1548a','CIV1548c','CIV1548e','BL1617','BL1664','BL1719','BL1853','FeII2402','BL2538','FeII2609','MgII']
            lh,ly = yl(l)
            splt(5,3,t,m,lh,ly,False)

        elif (op=='5'):
            # Fanelli et al UV indices (cont.)
            l = ['MgI','Mgwide','FeI','BL3096','CIVabs','HeIIems','','','','','','','','','']
            lh,ly = yl(l)
            splt(5,3,t,m,lh,ly,False)

        elif (op=='6'):
            n,f,l = uidx(m)
            if n < 0:
                break
            nplt(n,t,f,l,False)

        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',ifile.replace('fits','lsindx') + op + ".png")

def fmag(ifile,t,m):

    # Plots selected photometric magnitudes
    
    import os
    from myplots import splt,nplt

    while True:
        # Ask for magnitudes to plot
        print()
        print('Select magnitudes to plot (press <Enter> to exit loop):')
        print('         1: UV to FIR')
        print('         2: NIR to FIR')
        print('         3: User selected bands')
        op = input( 'choice = ')

        # Plot magnitudes
        if (op == '1'):

            lh=['Mbol','FUV_GALEX_AB','NUV_GALEX_AB','U_Johnson','B3_Johnson','V_Johnson','R_Cousins','I_Cousins','u_SDSS_AB','g_SDSS_AB','r_SDSS_AB',
                'i_SDSS_AB','z_SDSS_AB','K_Palomar','I5p7_IRAC','M24_MIPS']
            ly = ['M$_{BOL}$', 'GALEX FUV', 'GALEX NUV', 'U', 'B', 'V', 'R', 'I', 'u', 'g', 'r', 'i', 'z', 'K', 'IRAC 5.7 $\mu$m', 'MIPS 24 $\mu$m']
            splt(4,4,t,m,lh,ly,True)
    
        elif (op == '2'):
 
            lh = ['J_2Mass', 'H_2Mass', 'Ks_2Mass', 'K_Palomar', 'L_Johnson', 'I3p6_IRAC', 'I4p5_IRAC', 'I5p7_IRAC', 'I7p9_IRAC', 'I12_IRAS', 'M24_MIPS',
                  'I25_IRAS', 'I60_IRAS', 'M70_MIPS', 'I100_IRAS', 'M160_MIPS' ]
            ly = ['2Mass J', '2Mass H', '2Mass Ks', 'K', 'L', 'IRAC 3.6 $\mu$m', 'IRAC 4.5 $\mu$m', 'IRAC 5.7 $\mu$m', 'IRAC 7.9 $\mu$m', 'IRAS 12 $\mu$m',
                  'MIPS 24 $\mu$m', 'IRAS 25 $\mu$m', 'IRAS 60 $\mu$m', 'MIPS 70 $\mu$m', 'IRAS 100 $\mu$m', 'MIPS 160 $\mu$m']
            splt(4,4,t,m,lh,ly,True)

        elif (op=='3'):
            n,f,l = umag(m)
            if n < 0:
                break
            nplt(n,t,f,l,True)
        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',ifile.replace('fits','mags') + op + ".png")
        
def fphy(ifile,t,m):

    # Plots selected physical properties
    
    import os
    from myplots import splt,nplt

    while True:
        # Ask for indices to plot
        print()
        print('Select quantities to plot (press <Enter> to exit loop):')
        print('         1: Mass related properties')
        print('         2: Ionizing photons and remnant production rate')
        print('         3: User selected property')
        op = input( 'choice = ')

        # Plot physical properties
        if (op == '1'):
            # Galaxy mass and M/L ratios
            lh = ['Mgalaxy', 'Mstars', 'Mremnants', 'Mretgas', 'Mtot', 'Mtot_Lb', 'Mtot_Lv', 'Mtot_Lk', 'SFR', 'Mliv_Lb', 'Mliv_Lv', 'Mliv_Lk', 'EvolutionaryFlux',
                  'SpecificEvolFlux', 'TurnoffMass', 'BPMS_BMS']
            ly = ['Mgal (M$_\odot$)', 'Mliv (M$_\odot$)', 'Mrem (M$_\odot$)', 'Mgas (M$_\odot$)', 'Mtot = Mliv + Mrem (M$_\odot$)', 'Mtot/L$_B$ (M$_\odot$/L$_\odot$)',
                  'Mtot/L$_V$ (M$_\odot$/L$_\odot$)', 'Mtot/L$_K$ (M$_\odot$/L$_\odot$)', 'SFR (M$_\odot$/yr)', 'Mliv/L$_B$ (M$_\odot$/L$_\odot$)', 'Mliv/L$_V$ (M$_\odot$/L$_\odot$)',
                  'Mliv/L$_K$ (M$_\odot$/L$_\odot$)', 'Evolutionary Flux (Nstars/yr)', 'Specific Evol. Flux (Nstars/yr/L$_\odot$)', 'MS Turnoff Mass (M$_\odot$)', 'Ratio PostMS/MS Bol. Flux']
            splt(4,4,t,m,lh,ly,False)

        elif (op == '2'):
            # Ionizing photons and other physical properties
            lh = ['logNLy', 'logNHeI', 'logNHeII', 'NBH', 'NNS', 'NWD', 'B912', 'SNR', 'PNBR']
            ly = ['log N(HI) (photons/M$_\odot$)', 'log N(HeI) (photons/M$_\odot$)', 'log N(HeII) (photons/M$_\odot$)', 'N(BH) (number/M$_\odot$)', 'N(NS) (number/M$_\odot$)',
                  'N(WD) (number/M$_\odot$)', 'Lyman Break Amplitude', 'SN rate (SN/yr/L$_\odot$/M$_\odot$)', 'PNBR (PN/yr/L$_\odot$/M$_\odot$)' ]
            splt(3,3,t,m,lh,ly,False)

        elif (op=='3'):
            n,f,l = uphy(m)
            if n < 0:
                break
            nplt(n,t,f,l,False)
        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',ifile.replace('fits','physp') + op + ".png")

def ucol(m):
    from mydata import bands
    # Plot user selected color
    b = bands()
    while True:
        # Ask for colors to plot, 1 model
        print()
        a = input('Select up to 5 bands to plot up to 4 colors: N1 N2 N3 N4 N5 = ')
        a = a.replace(",", " ")
        a = a.split()
        n = min(5,len(a))
        f = [""]*n
        for i in range(n):
            f[i] = b[int(a[i])]
        k = n-1
        if k <= 0:
            p=0.
            l=''
            n=-1
            return n,p,l
        # k colors to plot
        p = [0.]*k
        l = [""]*k
        for i in range (k):
            p[i] = m[f[i]]-m[f[i+1]]
            l[i] = f[i] + ' - ' + f[i+1]
            l[i] = l[i].replace("prime", "'")
            l[i] = l[i].replace("p", ".")
        return k,p,l

def umag(m):
    # Plot user selected magnitudes
    from mydata import bands
    b = bands()
    while True:
        # Ask for band to plot, 1 model
        print()
        a = input('Select up to 4 bands to plot (<Enter> exits) N1 N2 N3 N4 = ')
        a = a.replace(",", " ")
        a = a.split()
        n = min(4,len(a))
        f = [""]*n
        for i in range(n):
            f[i] = b[int(a[i])]
        if n <= 0:
            p=0.
            l=''
            n=-1
            return n,p,l
        # k bands to plot
        p = [0.]*n
        l = [""]*n
        for i in range (n):
            p[i] = m[f[i]]
            l[i] = f[i]
            l[i] = l[i].replace("prime", "'")
            l[i] = l[i].replace("p", ".")
        return n,p,l

def uidx(m):
    # Plot user selected indices
    from mydata import indices
    b,u= indices()
    while True:
        # Ask for indices to plot, 1 model
        print()
        a = input('Select up to 4 indices to plot (<Enter> exits) N1 N2 N3 N4 = ')
        a = a.replace(",", " ")
        a = a.split()
        n = min(4,len(a))
        f = [""]*n
        for i in range(n):
            f[i] = b[int(a[i])]
        if n <= 0:
            p=0.
            l=''
            n=-1
            return n,p,l
        # k bands to plot
        p = [0.]*n
        l = [""]*n
        for i in range (n):
            l[i] = f[i] + ' ' + u[int(a[i])]
            f[i] = f[i].replace("_", "")
            f[i] = f[i].replace("-", "")
            p[i] = m[f[i]]
        return n,p,l

def uphy(m):
    # Plot user selected properties
    from mydata import properties
    b,u= properties()
    while True:
        # Ask for properties to plot, 1 model
        print()
        a = input('Select up to 4 properties to plot (<Enter> exits) N1 N2 N3 N4 = ')
        a = a.replace(",", " ")
        a = a.split()
        n = min(4,len(a))
        f = [""]*n
        for i in range(n):
            f[i] = b[int(a[i])]
        if n <= 0:
            p=0.
            l=''
            n=-1
            return n,p,l
        # k bands to plot
        p = [0.]*n
        l = [""]*n
        for i in range (n):
            l[i] = f[i] + ' ' + u[int(a[i])]
            l[i] = l[i].replace("_", "/")
            p[i] = m[f[i]]
        return n,p,l
