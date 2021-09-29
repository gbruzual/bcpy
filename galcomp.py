def fplot2(file1,file2,n):

    global qf1, qf2
    from galaxev import plmenu
    from myfiles import read_bcfits, read_bcised, read_bcased, normwav
    from myplots import fstyle

    # Choose correct file format for file 1
    if '.fits' in file1:
        # Read fits table
        w1,f1,t1,h1,m1,d1,p1,a1 = read_bcfits(file1)
        k1 = 0
        qf1 = True
    elif '.ised' in file1:
        # Read .ised file
        w1,f1,t1,h1 = read_bcised(file1)
        k1 = 1
        qf1 = False
    else:
        # Read .ased file or any ascii table (galaxevpl output)
        w1,f1,t1,h1 = read_bcased(file1)
        k1 = 1
        qf1 = True

    # Choose correct file format for file 2
    if '.fits' in file2:
        # Read fits table
        w2,f2,t2,h2,m2,d2,p2,a2 = read_bcfits(file2)
        k2 = 0
        qf2 = True
    elif '.ised' in file2:
        # Read .ised file
        w2,f2,t2,h2 = read_bcised(file2)
        k2 = 1
        qf2 = False
    else:
        # Read .ased file or any ascii table (galaxevpl output)
        w2,f2,t2,h2 = read_bcased(file2)
        k2 = 1
        qf2 = True

    # Select menu
    k = max(k1,k2)

    while True:
        # Select plot option
        o = plmenu(k)
        if o=='s' or o=='n':
            wn = normwav(o)
            fgpl2(w1,f1,t1,h1,file1,w2,f2,t2,h2,file2,wn)
        elif o=='c':
            fcol2(file1,a1,m1,file2,a2,m2)
        elif o=='m':
            fmag2(file1,a1,m1,file2,a2,m2)
        elif o=='i':
            fidx2(file1,a1,d1,file2,a2,d2)
        elif o=='p':
            fphy2(file1,a1,p1,file2,a2,p2)
        elif o=='f':
            n=0
            return n
        elif o=='q':
            n=1
            return n
        else:
            print('Unknown option: ' + o)

def fgpl2(w1,f1,t1,h1,file1,w2,f2,t2,h2,file2,wn):

    # Extracts model SED at age indicated in argument list (GBA, Dec. 2019)

    from myfiles import geta
    from myplots import plsed2
    while True:
        # Ask for time steps to plot
        print()
        a = geta()
        if len(a) <= 0:
            break
        e1 = round(t1[len(t1)-1]*1.E-9)        # Last time step rounded to nearest integer in Gyr
        a1 = a[a <= e1]
        e2 = round(t2[len(t2)-1]*1.E-9)        # Last time step rounded to nearest integer in Gyr
        a2 = a[a <= e2]
        # Detect if BC03 or CB20 model according to last time step
        if e1 > 16:
            b1 = True                 # BC2003 models reach 20 Gyr
        else:
            b1 = False                # CB2020 models reach 14 Gyr
        if e2 > 16:
            b2 = True                 # BC2003 models reach 20 Gyr
        else:
            b2 = False                # CB2020 models reach 14 Gyr

        # Plot sed's
        plsed2(w1,f1,t1,h1,a1,b1,file1,qf1,w2,f2,t2,h2,a2,b2,file2,qf2,wn)
   
def fcol2(file1,t1,m1,file2,t2,m2):

    # Plot selected color sets

    import os
    from myplots import splt2,nplt2

    while True:
        # Ask for colors to plot
        print()
        print('Select colors to plot (press <Enter> to exit loop)')
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
            splt2(3,3,t1,m1,t2,m2,lh,ly,False)

        elif (op=='2'):
            lh = ['U_Johnson','B2_Johnson',  'B3_Johnson','V_Johnson',  'V_Johnson','R_Cousins',
                  'R_Cousins','I_Cousins',   'I_Cousins','J_Johnson',   'J_Johnson','K_Johnson',
                  'K_Johnson','L_Johnson',   'V_Johnson','J_Johnson',   'V_Johnson','K_Johnson']
            ly = ['U - B', 'B - V', 'V - R$_c$', 'R$_c$ - I$_c$', 'I$_c$ - J', 'J - K', 'K - L', 'V - J', 'V - K']
            splt2(3,3,t1,m1,t2,m2,lh,ly,False)
         
        elif (op=='3'):
            lh = ['u_SDSS_AB','g_SDSS_AB',   'g_SDSS_AB','r_SDSS_AB',   'r_SDSS_AB','i_SDSS_AB',   'i_SDSS_AB','z_SDSS_AB']
            ly = ['u - g', 'g - r', 'r - i', 'i - z']
            splt2(2,2,t1,m1,t2,m2,lh,ly,False)

        elif (op=='4'):
            n,f1,f2,l = ucol2(m1,m2)
            if n < 0:
                break
            nplt2(n,t1,f1,t2,f2,l,False)

        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',file1.replace('fits','') + file2.replace('fits','color') + op + ".png")
        
def fidx2(file1,t1,m1,file2,t2,m2):

    # Plots selected line indices

    import os
    from myplots import yl,splt2,nplt2

    while True:
        # Ask for indices to plot
        print()
        print('Select indices to plot (press <Enter> to exit loop)')
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
            splt2(5,3,t1,m1,t2,m2,lh,ly,False)

        elif (op == '2'):
            # Lick indices 16:21 + WO + Marcillac et al. indices
            l = ['Fe5406', 'Fe5709', 'Fe5782', 'NaD', 'TiO1:m', 'TiO2:m', 'HdeltaA', 'HgammaA', 'HdeltaF', 'HgammaF', '', '', 'H83889', 'H93835', 'H103798']
            lh,ly = yl(l)
            splt2(5,3,t1,m1,t2,m2,lh,ly,False)

        elif (op=='3'):
            # DTT + HK + B4000 indices
            l = ['CaII8498', 'CaII8542', 'CaII8662', 'MgI8807', '', '', 'BHHK', '', '', 'B4000VN:n', '', '', '', '', '']
            lh,ly = yl(l)
            splt2(5,3,t1,m1,t2,m2,lh,ly,False)

        elif (op=='4'):
            # Fanelli et al UV indices
            l = ['BL1302','SiIV','BL1425','Fe1453','CIV1548a','CIV1548c','CIV1548e','BL1617','BL1664','BL1719','BL1853','FeII2402','BL2538','FeII2609','MgII']
            lh,ly = yl(l)
            splt2(5,3,t1,m1,t2,m2,lh,ly,False)

        elif (op=='5'):
            # Fanelli et al UV indices (cont.)
            l = ['MgI','Mgwide','FeI','BL3096','CIVabs','HeIIems','','','','','','','','','']
            lh,ly = yl(l)
            splt2(5,3,t1,m1,t2,m2,lh,ly,False)

        elif (op=='6'):
            n,f1,f2,l = uidx2(m1,m2)
            if n < 0:
                break
            nplt2(n,t1,f1,t2,f2,l,False)
        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',file1.replace('fits','') + file2.replace('fits','lsindx') + op + ".png")
                
def fmag2(file1,t1,m1,file2,t2,m2):

    # Plots selected photometric magnitudes
    
    import os
    from myplots import splt2,nplt2

    while True:
        # Ask for magnitudes to plot
        print()
        print('Select magnitudes to plot (press <Enter> to exit loop)')
        print('         1: UV to FIR')
        print('         2: NIR to FIR')
        print('         3: User selected bands')
        op = input( 'choice = ')

        # Plot magnitudes
        if (op == '1'):

            lh=['Mbol','FUV_GALEX_AB','NUV_GALEX_AB','U_Johnson','B3_Johnson','V_Johnson','R_Cousins','I_Cousins','u_SDSS_AB','g_SDSS_AB','r_SDSS_AB',
                'i_SDSS_AB','z_SDSS_AB','K_Palomar','I5p7_IRAC','M24_MIPS']
            ly = ['M$_{BOL}$', 'GALEX FUV', 'GALEX NUV', 'U', 'B', 'V', 'R', 'I', 'u', 'g', 'r', 'i', 'z', 'K', 'IRAC 5.7 $\mu$m', 'MIPS 24 $\mu$m']
            splt2(4,4,t1,m1,t2,m2,lh,ly,True)
    
        elif (op == '2'):
 
            lh = ['J_2Mass', 'H_2Mass', 'Ks_2Mass', 'K_Palomar', 'L_Johnson', 'I3p6_IRAC', 'I4p5_IRAC', 'I5p7_IRAC', 'I7p9_IRAC', 'I12_IRAS', 'M24_MIPS',
                  'I25_IRAS', 'I60_IRAS', 'M70_MIPS', 'I100_IRAS', 'M160_MIPS' ]
            ly = ['2Mass J', '2Mass H', '2Mass Ks', 'K', 'L', 'IRAC 3.6 $\mu$m', 'IRAC 4.5 $\mu$m', 'IRAC 5.7 $\mu$m', 'IRAC 7.9 $\mu$m', 'IRAS 12 $\mu$m',
                  'MIPS 24 $\mu$m', 'IRAS 25 $\mu$m', 'IRAS 60 $\mu$m', 'MIPS 70 $\mu$m', 'IRAS 100 $\mu$m', 'MIPS 160 $\mu$m']
            splt2(4,4,t1,m1,t2,m2,lh,ly,True)

        elif (op=='3'):
            n,f1,f2,l = umag2(m1,m2)
            if n < 0:
                break
            nplt2(n,t1,f1,t2,f2,l,True)

        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',file1.replace('fits','') + file2.replace('fits','mags') + op + ".png")
        
def fphy2(file1,t1,m1,file2,t2,m2):

    # Plots selected physical properties
    
    import os
    from myplots import splt2,nplt2

    while True:
        # Ask for indices to plot
        print()
        print('Select quantities to plot (press <Enter> to exit loop)')
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
            splt2(4,4,t1,m1,t2,m2,lh,ly,False)

        elif (op == '2'):
            # Ionizing photons and other physical properties
            lh = ['logNLy', 'logNHeI', 'logNHeII', 'NBH', 'NNS', 'NWD', 'B912', 'SNR', 'PNBR']
            ly = ['log N(HI) (photons/M$_\odot$)', 'log N(HeI) (photons/M$_\odot$)', 'log N(HeII) (photons/M$_\odot$)', 'N(BH) (number/M$_\odot$)', 'N(NS) (number/M$_\odot$)',
                  'N(WD) (number/M$_\odot$)', 'Lyman Break Amplitude', 'SN rate (SN/yr/L$_\odot$/M$_\odot$)', 'PNBR (PN/yr/L$_\odot$/M$_\odot$)' ]
            splt2(3,3,t1,m1,t2,m2,lh,ly,False)

        elif (op=='3'):
            n,f1,f2,l = uphy2(m1,m2)
            if n < 0:
                break
            nplt2(n,t1,f1,t2,f2,l,False)
        else:
            break

        # Rename saved file
        os.rename('tmpplot.png',file1.replace('fits','') + file2.replace('fits','physp') + op + ".png")

def ucol2(m1,m2):
    from mydata import bands
    # Plot user selected colors
    b = bands()
    while True:
        # Ask for colors to plot, 2 models
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
            p1=0.
            p2=0.
            l=''
            n=-1
            return n,p1,p2,l
        # k colors to plot
        p1 = [0.]*k
        p2 = [0.]*k
        l  = [""]*k
        for i in range (k):
            p1[i] = m1[f[i]]-m1[f[i+1]]
            p2[i] = m2[f[i]]-m2[f[i+1]]
            l[i]  = f[i] + ' - ' + f[i+1]
            l[i]  = l[i].replace("prime", "'")
            l[i]  = l[i].replace("p", ".")
        return k,p1,p2,l

def umag2(m1,m2):
    # Plot user selected magnitudes
    from mydata import bands
    b = bands()
    while True:
        # Ask for band to plot, 2 models
        print()
        a = input('Select up to 4 bands to plot (<Enter> exits) N1 N2 N3 N4 = ')
        a = a.replace(",", " ")
        a = a.split()
        n = min(4,len(a))
        f = [""]*n
        for i in range(n):
            f[i] = b[int(a[i])]
        if n <= 0:
            p1=0.
            p2=0.
            l=''
            n=-1
            return n,p1,p2,l
        # k bands to plot
        p1 = [0.]*n
        p2 = [0.]*n
        l  = [""]*n
        for i in range (n):
            p1[i] = m1[f[i]]
            p2[i] = m2[f[i]]
            l[i]  = f[i]
            l[i]  = l[i].replace("prime", "'")
            l[i]  = l[i].replace("p", ".")
        return n,p1,p2,l

def uidx2(m1,m2):
    # Plot user selected index
    from mydata import indices
    b,u= indices()
    while True:
        # Ask for index to plot, 2 models
        print()
        a = input('Select up to 4 indices to plot (<Enter> exits) N1 N2 N3 N4 = ')
        a = a.replace(",", " ")
        a = a.split()
        n = min(4,len(a))
        f = [""]*n
        for i in range(n):
            f[i] = b[int(a[i])]
        if n <= 0:
            p1=0.
            p2=0.
            l=''
            n=-1
            return n,p1,p2,l
        # k bands to plot
        p1 = [0.]*n
        p2 = [0.]*n
        l  = [""]*n
        for i in range (n):
            l[i]  = f[i] + ' ' + u[int(a[i])]
            f[i]  = f[i].replace("_", "")
            f[i]  = f[i].replace("-", "")
            p1[i] = m1[f[i]]
            p2[i] = m2[f[i]]
        return n,p1,p2,l

def uphy2(m1,m2):
    # Plot user selected properties
    from mydata import properties
    b,u= properties()
    while True:
        # Ask for properties to plot, 2 models
        print()
        a = input('Select up to 4 properties to plot (<Enter> exits) N1 N2 N3 N4 = ')
        a = a.replace(",", " ")
        a = a.split()
        n = min(4,len(a))
        f = [""]*n
        for i in range(n):
            f[i] = b[int(a[i])]
        if n <= 0:
            p1=0.
            p2=0.
            l=''
            n=-1
            return n,p1,p2,l
        # k bands to plot
        p1 = [0.]*n
        p2 = [0.]*n
        l  = [""]*n
        for i in range (n):
            l[i]  = f[i] + ' ' + u[int(a[i])]
            l[i]  = l[i].replace("_", "/")
            p1[i] = m1[f[i]]
            p2[i] = m2[f[i]]
        return n,p1,p2,l
