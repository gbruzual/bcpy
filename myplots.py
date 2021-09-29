def fstyle(i):
    # Defines style of plot according to variable i selected from following list
    # To obtain available styles do: print(plt.style.available)
    o = ('classic', 'seaborn-paper', '_classic_test', 'Solarize_Light2', 'bmh', 'dark_background', 'fast', 'fivethirtyeight',
         'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
         'seaborn-darkgrid', 'seaborn-deep', 'seaborn-notebook', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
         'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10')
    return o[i]

def yl(l):
    # Builds y-label for variables in l
    n  = len(l)
    y = [" "]*(n+1)
    for i in range(n):
        lh = l[i]
        if lh=='':
            y[i] = lh
        elif ":m" in lh:
            lh = lh.replace(":m","")
            l[i] = lh
            y[i] = lh + " (mag)"
        elif ":n" in lh:
            lh = lh.replace(":n","")
            l[i] = lh
            y[i] = lh
        else:
            y[i] = lh + " ($\AA$)"
    return l,y

def vw(ax,i,j,t,m,k,lh,ly,flip):
    # Plots in window (i,j)
    if lh[k] =='':
        ax[i,j].set_axis_off()
    else:
        ax[i,j].set_xscale('log')
        ax[i,j].set_xlabel("t (yr)")
        ax[i,j].set_ylabel(ly[k])
        if flip:
            ax[i,j].invert_yaxis()
        if len(lh) > len(ly):
            ax[i,j].plot(t,m[lh[2*k]]-m[lh[2*k+1]],'r',linestyle='solid')
        else:
            ax[i,j].plot(t,m[lh[k]], 'r', linestyle='solid')

def splt(i,j,t,m,lh,ly,flip):
    # Plot figure with ixj subplots
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(i,j,figsize=(10,8))
    k = -1
    for ii in range(i):
        for jj in range(j):
            ax[ii,jj].minorticks_on()
            k = k + 1
            vw(ax,ii,jj,t,m,k,lh,ly,flip)
    for jj in range(j):
        fig.align_ylabels(ax[:,jj])       # align ylabel for the jj ax column
    fig.tight_layout()
    plt.savefig('tmpplot.png')
    plt.show()

def vw2(ax,i,j,t1,m1,t2,m2,k,lh,ly,flip):
    # Plots in window (i,j)
    if lh[k] =='':
        ax[i,j].set_axis_off()
    else:
        ax[i,j].set_xscale('log')
        ax[i,j].set_xlabel("t (yr)")
        ax[i,j].set_ylabel(ly[k])
        if flip:
            ax[i,j].invert_yaxis()
        if len(lh) > len(ly):
            ax[i,j].plot(t1,m1[lh[2*k]]-m1[lh[2*k+1]],'b',linestyle='solid',label='1')
            ax[i,j].plot(t2,m2[lh[2*k]]-m2[lh[2*k+1]],'r',linestyle='solid',label='2')
        else:
            ax[i,j].plot(t1,m1[lh[k]],'b',linestyle='solid',label='1')
            ax[i,j].plot(t2,m2[lh[k]],'r',linestyle='solid',label='2')
    if i==0 and j==0:
        ax[i,j].legend(loc='best')
        #ax[i,j].legend(loc='best', title='Model:', frameon=True)

def splt2(i,j,t1,m1,t2,m2,lh,ly,flip):
    # Plot figure with ixj subplots
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(i,j,figsize=(10,8))
    k = -1
    for ii in range(i):
        for jj in range(j):
            ax[ii,jj].minorticks_on()
            k = k + 1
            vw2(ax,ii,jj,t1,m1,t2,m2,k,lh,ly,flip)
    for jj in range(j):
        fig.align_ylabels(ax[:,jj])       # align ylabel for the jj ax column
    # fig.suptitle("This Main Title is Nicely Formatted", fontsize=16)
    # fig.subplots_adjust(top=0.88)
    fig.tight_layout()
    plt.savefig('tmpplot.png')
    plt.show()

def nvw(ax,i,k,t,f,l,flip):
    # Plot in window ax[i]
    if k > 1:
        bx = ax[i]
    else:
        bx = ax
    bx.set_xscale('log')
    bx.set_xlabel("t (yr)")
    bx.set_ylabel(l)
    if flip:
        bx.invert_yaxis()
    bx.plot(t,f,'r',linestyle='solid')

def nplt(k,t,f,l,flip):
    # Plot figure with n subplots
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1,k,figsize=(5*k,5))
    for i in range (k):
        nvw(ax,i,k,t,f[i],l[i],flip)
    fig.tight_layout()
    plt.savefig('tmpplot.png')
    plt.show()

def nvw2(ax,i,k,t1,f1,t2,f2,l,flip):
    # Plot in window ax[i]
    if k > 1:
        bx = ax[i]
    else:
        bx = ax
    bx.set_xscale('log')
    bx.set_xlabel("t (yr)")
    bx.set_ylabel(l)
    if flip:
        bx.invert_yaxis()
    bx.plot(t1,f1,'b',linestyle='solid',label='1')
    bx.plot(t2,f2,'r',linestyle='solid',label='2')
    bx.legend(loc='best')

def nplt2(k,t1,f1,t2,f2,l,flip):
    # Plot figure with n subplots, 2 models
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1,k,figsize=(5*k,5))
    for i in range (k):
        nvw2(ax,i,k,t1,f1[i],t2,f2[i],l[i],flip)
    fig.tight_layout()
    plt.savefig('tmpplot.png')
    plt.show()

def newlimslbl(x1,x2,y1,y2,xl,yl,r):
    # Asks for new limits and/or labels for current plot
    
    print('  Current limits = ',x1, x2, y1, y2)
    limits = input('  New plot limits (Xmin Xmax Ymin Ymax) or new labels (Xlabel,Ylabel) = ')
    if len(limits) == 0:
        q=True
        xmin,xmax,ymin,ymax = x1,x2,y1,y2
        xlbl,ylbl = xl,yl
    else:
        q=False
        if ',' in limits:
            r=True
            xmin,xmax,ymin,ymax = x1,x2,y1,y2
            xlbl,ylbl = limits.split(',')
        else:
            xmin,xmax,ymin,ymax = limits.split()
            xmin,xmax,ymin,ymax = float(xmin), float(xmax), float(ymin), float(ymax)
            xlbl,ylbl = xl,yl
    return xmin,xmax,ymin,ymax,q,xlbl,ylbl,r

def newlimslogy(x1,x2,y1,y2):
    # Asks for new limits for current plot (expected log Y limits)
    
    limits = input('  New plot limits (Xmin Xmax logYmin logYmax) = ')
    if len(limits) == 0:
        q=False
        xmin,xmax,ymin,ymax = x1,x2,y1,y2
    else:
        q=True
        xmin,xmax,ymin,ymax = limits.split()
        xmin,xmax,ymin,ymax = float(xmin), float(xmax), 10.**float(ymin), 10.**float(ymax)
    return xmin,xmax,ymin,ymax,q

def newlimslogylbl(x1,x2,y1,y2,xl,yl,r):
    # Asks for new limits and/or labels for current plot (expected log Y limits)
    
    limits = input('  New plot limits (Xmin Xmax logYmin logYmax) or new labels (Xlabel,Ylabel) = ')
    if len(limits) == 0:
        q=True
        xmin,xmax,ymin,ymax = x1,x2,y1,y2
        xlbl,ylbl = xl,yl
    else:
        q=False
        if ',' in limits:
            r=True
            xmin,xmax,ymin,ymax = x1,x2,y1,y2
            xlbl,ylbl = limits.split(',')
        else:
            xmin,xmax,ymin,ymax = limits.split()
            xmin,xmax,ymin,ymax = float(xmin), float(xmax), 10.**float(ymin), 10.**float(ymax)
            xlbl,ylbl = xl,yl
    return xmin,xmax,ymin,ymax,q,xlbl,ylbl,r

def txtsed(ifile,w,f,h,a,k,p):
    # Open and writes text file with selected sed's
    import os

    # Ask for output file name
    print()
    ofile = input('  Name of file to save final plot and write SED''s = ')
    if len(ofile) > 0:
        # Rename temporary file
        os.rename('tmpsedplot.png',ofile + '.png') 
        if p:
            # Write sed's in text file if p = True
            of = open(ofile + '.txt',"w")
            # Output file header
            of.write('# Input file name  = ' + ifile + '\n')
            of.write('# Output file name = ' + ofile + '.txt\n')
            # Build output file header
            d1 = '# Column' + ' '.join( '%10i'     % v for v in range(2,k+2))
            d1 = d1.replace("n  ", "n")
            d2 = '# SED(Lo/A)'
            for j in range(k):
                d2 = d2 + '  at age   '
            d3 = '# Lambda_A ' + ' '.join('%10.4E' % v for v in a*1.E9)
            of.write(d1+'\n')
            of.write(d2+'\n')
            of.write(d3+'\n')
            u  = [0]*(k+1)
            for l in range(len(w)):
                for j in range(k+1):
                    u[j] = f[h[j]][l]
                s = ' '.join('%10.4E' % v for v in u) + "\n"
                of.write(s)
            of.close()
    else:
        # Remove temporary file
        os.remove('tmpsedplot.png')

def plsed1(w,f,t,h,a,bc,ifile,qf,wn):
    # Plots various sed's from the same model in a single panel

    import matplotlib.pyplot as plt
    from myfiles import geth

    # Get column header of sed's to plot (fits file)
    k,i,b = geth(a,t)

    if wn > 0.:
        # Normalize sed's, find position in array w of the normalization wavelength = wn
        n = True
        for l in range(len(w)):
            if w[l] <= wn:
                ln = l
    else:
        n = False

    q = False
    while True:
       #fig, ax = plt.subplots(1,1,figsize=(10,8))
        fig, ax = plt.subplots(1,1,figsize=(16,8))
        ax.minorticks_on()
        ax.set_title(ifile)
        ax.set_xlabel("Wavelength ($\AA$)")
        if n:
            ax.set_ylabel('L / L(' + str(int(wn)) + '$\AA$)')
        else:
            ax.set_ylabel("L (L$_\odot/\AA$)")
        plt.grid(True)
        if q:
            # Set plot limits entered by user
            if xmax > 1.E4:
                ax.set_xscale('log')
            ax.set_xlim(xmin,xmax)
            ax.set_ylim(ymin,ymax)
        else:
            # Plot sed's in full range of wavelength and flux
            ax.set_xscale('log')
        ax.set_yscale('log')
        for l in range(1,k+1):
            if n:
                # Normalize sed's
                if qf:
                    fn = f[ln][i[l]]
                else:
                    fn = f[i[l]][ln]
                yp = f[i[l]][:]/fn
            else:
                yp = f[i[l]][:]
            ax.plot(w,yp,linestyle='solid',label=b[l])
        ax.legend(loc='best', title='Age (Gyr)', frameon=True)
        # Save and show plot
        plt.savefig('tmpsedplot.png')
        plt.show()
        # Repeat plot with user selected limits
        xmin, xmax = ax.set_xlim()  # return the current xlim
        ymin, ymax = ax.set_ylim()  # return the current ylim
        xmin, xmax, ymin, ymax, q = newlimslogy(xmin,xmax,ymin,ymax)
        if not q:
            break
    # Rename file with final plot and write plotted SED's to text file
    txtsed(ifile,w,f,h,a,k,True)

def plsed2(w1,f1,t1,h1,a1,b1,file1,qf1,w2,f2,t2,h2,a2,b2,file2,qf2,wn):
    # Plots sed's of two models requested by user in different panels

    import numpy as np
    import matplotlib.pyplot as plt
    from myfiles import geth

    # Get column header of sed's to plot
    k1,i1,b1 = geth(a1,t1)
    k2,i2,b2 = geth(a2,t2)

    if wn > 0.:
        # Normalize sed's, find position in arrays w1,w2 of the normalization wavelength = wn
        n = True
        for l in range(len(w1)):
            if w1[l] <= wn:
                l1 = l
        for l in range(len(w2)):
            if w2[l] <= wn:
                l2 = l
    else:
        n = False

    q = False
    while True:

        if k1 > 1 and k2 > 1:

            # Multiple ages requested: plot sed's corresponding to each model in different frames

            # Find limits in common to both data groups
            fy1 = 1.E32 ; fy2 = -fy1
            for l in range(1,k1+1):
                if n:
                    # Normalize sed's
                    if qf1:
                        fn = f1[l1][i1[l]]
                    else:
                        fn = f1[i1[l]][l1]
                    yp = f1[i1[l]][:]/fn
                else:
                    yp = f1[i1[l]][:]
                fy1 = min(fy1,np.amin(yp))
                fy2 = max(fy2,np.amax(yp))
            for l in range(1,k2+1):
                if n:
                    # Normalize sed's
                    if qf2:
                        fn = f2[l2][i2[l]]
                    else:
                        fn = f2[i2[l]][l2]
                    yp = f2[i2[l]][:]/fn
                else:
                    yp = f2[i2[l]][:]
                fy1 = min(fy1,np.amin(yp))
                fy2 = max(fy2,np.amax(yp))
            fy1 = 0.9*max(fy1,1.e-25)
            fy2 = 1.5*fy2
            fx1 = 0.9*min(w1[0],w2[0])
            fx2 = 1.1*max(w1[len(w1)-1],w2[len(w2)-1])

            # Define plotting arrea
            fig, ax = plt.subplots(1,2,figsize=(20,8))

            # Plot first fits file on the LHS panel
            ax[0].minorticks_on()
            ax[0].set_xlabel('Wavelength ($\AA$)')
            if n:
                ax[0].set_ylabel('L / L(' + str(int(wn)) + '$\AA$)')
            else:
                ax[0].set_ylabel("L (L$_\odot/\AA$)")
            ax[0].set_title(file1)
            ax[0].set_yscale('log')
            if q:
                # Set plot limits entered by user
                if xmax > 1.E4:
                    ax[0].set_xscale('log')
                ax[0].set_xlim(xmin,xmax)
                ax[0].set_ylim(ymin,ymax)
            else:
                # Plot sed's in full range of wavelength and flux
                if fx2 > 1.E4:
                    ax[0].set_xscale('log')
                ax[0].set_xlim(fx1,fx2)
                ax[0].set_ylim(fy1,fy2)
            for l in range(1,k1+1):
                if n:
                    # Normalize sed's
                    if qf1:
                        fn = f1[l1][i1[l]]
                    else:
                        fn = f1[i1[l]][l1]
                    yp = f1[i1[l]][:]/fn
                else:
                    yp = f1[i1[l]][:]
                ax[0].plot(w1,yp,linestyle='solid',label=b1[l])
            ax[0].legend(loc='best', title='Age (Gyr)', frameon=True)
            xmin, xmax = ax[0].set_xlim()  # return the current xlim
            ymin, ymax = ax[0].set_ylim()  # return the current ylim
            ax[0].grid(True)

            # Plot second fits file on the RHS panel
            ax[1].minorticks_on()
            ax[1].set_xlabel('Wavelength ($\AA$)')
            if n:
                ax[1].set_ylabel('L / L(' + str(int(wn)) + '$\AA$)')
            else:
                ax[1].set_ylabel("L (L$_\odot/\AA$)")
            ax[1].set_title(file2)
            ax[1].set_xlim(xmin,xmax)
            ax[1].set_ylim(ymin,ymax)
            if xmax > 1.E4 or fx2 > 1.E4:
                ax[1].set_xscale('log')
            ax[1].set_yscale('log')
            for l in range(1,k2+1):
                if n:
                    # Normalize sed's
                    if qf2:
                        fn = f2[l2][i2[l]]
                    else:
                        fn = f2[i2[l]][l2]
                    yp = f2[i2[l]][:]/fn
                else:
                    yp = f2[i2[l]][:]
                ax[1].plot(w2,yp,linestyle='solid',label=b2[l])
            ax[1].legend(loc='best', title='Age (Gyr)', frameon=True)
            ax[1].grid(True)

        else:

            # A single age requested: plot sed's corresponding to both models in the same frame
            fig, ax = plt.subplots(1,1,figsize=(10,8))
            ax.minorticks_on()
            ax.set_title(file1 + '  vs.  ' + file2)
            ax.set_xlabel("Wavelength ($\AA$)")
            ax.set_ylabel("L (L$_\odot/\AA$)")
            plt.grid(True)
            if q:
                # Set plot limits entered by user
                if xmax > 1.E4:
                    ax.set_xscale('log')
                ax.set_xlim(xmin,xmax)
                ax.set_ylim(ymin,ymax)
            else:
                # Plot sed's in full range of wavelength and flux
                ax.set_xscale('log')
            ax.set_yscale('log')
            ax.plot(w1,f1[h1[i1[1]]],linestyle='solid',label=b1[1])
            ax.plot(w2,f2[h2[i2[1]]],linestyle='solid',label=b2[1])
            ax.legend(loc='best', title='Age (Gyr)', frameon=True)
            xmin, xmax = ax.set_xlim()  # return the current xlim
            ymin, ymax = ax.set_ylim()  # return the current ylim

        # Save and show plot
        plt.tight_layout()
        plt.savefig('tmpsedplot.png')
        plt.show()
        # Repeat plots with user selected limits
        xmin, xmax, ymin, ymax, q = newlimslogy(xmin,xmax,ymin,ymax)
        if not q:
            break

    # Rename file with final plot
   #txtsed(file1,w1,f1,h1,a1,k1,False)
    txtsed(file1,w1,f1,h1,a1,k1,True)
    return

def bfarrays(x,ys,yb):
    # Build arrays for Binary Fraction plots
    import numpy as np

    # Find position in array x of the normalization wavelength = 5500 A.
    for k in range(len(x)):
        if x[k] <= 5500:
            jn = k

    # Make a sequence of n values of bf (Binary Fraction) from 0 to 1 in steps of d
    m = 1001
    d =1./(m-1)
    n = np.arange(m)
    bf = [ k*d for k in n]

    # Compute flux yn at normalization wavelength for n seds
    yn = [ bf[k]*yb[jn] + (1-bf[k])*ys[jn] for k in n]

    # Build n seds combining the binary star sed yb (weight bf) and the single star sed ys (weight 1-bf)
    # Normalize each sed at the normalization wavelength according to yn computed above
    yp = [ bf[k]*yb/yn[k] + (1-bf[k])*ys/yn[k] for k in n]

    # Store in ym the normalized sed corresponding to bf = 0.5 (i.e., N1 = Ns, since BF = N1/(N1+Ns)
    ym = 0.5*yb + 0.5*ys
    yj = ym[jn]
    ym = ym/yj

    # Store in array z the values to map the auxiliary axis
    # Each sed will be plotted in the colour corresponding to its Binary fraction value
    z = np.arange(0., 1.001, 0.001, float)		# Same as bf values

    return yp,ym,z					# return arrays used in plots

def bfplot(fig,ax,x,ys,yb,id):

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from matplotlib.collections import LineCollection
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes
    import numpy as np

    # Build arrays to be plotted
    yp,ym,z = bfarrays(x,ys,yb)

    # Define labels and plot limits
    ax.set_xlabel('Wavelength ($\AA$)')
    ax.set_ylabel('F$_\lambda$/F$_\lambda$(5500 $\AA$)')
    ax.set_xscale('log')
    ax.set_yscale('log')
    #x.set_xlim(np.min(x), np.max(x))
    ax.set_xlim(90.,7000.)
    #x.set_ylim(np.min(yp), np.max(yp))
    #x.set_ylim(1.E-3,1.E2)
    ax.set_ylim(np.max(yp)/1.E4, np.max(yp)*1.1)
    ax.set_title(id)

    # Plot SED for BF = 0.50 as a black line
    ax.plot(x,ym, 'k', linestyle='solid')

    # Plot line_segments (SEDs) all at once following color code defined in array z
    line_segments = LineCollection([np.column_stack([x, y]) for y in yp], linestyles='solid', cmap=plt.cm.get_cmap('gist_rainbow'))
    line_segments.set_array(z)
    sc = ax.add_collection(line_segments)

    # Show colorbar at indicated position
    plt.tight_layout()
    position=fig.add_axes([0.80,0.15,0.02,0.35])  ## the parameters are the specified position set for the color box
    axcb = fig.colorbar(sc,cax=position)
    axcb.set_label('Binary Fraction')

def bfplot2(fig,ax,i,j,x,ys,yb,id):

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from matplotlib.collections import LineCollection
    import numpy as np

    # Build arrays to be plotted
    yp,ym,z = bfarrays(x,ys,yb)

    # Define labels and plot limits
    ax[i,j].set_xlabel('Wavelength ($\AA$)')
    ax[i,j].set_ylabel('F$_\lambda$/F$_\lambda$(5500 $\AA$)')
    ax[i,j].set_xscale('log')
    ax[i,j].set_yscale('log')
    ax[i,j].set_xlim(np.min(x), np.max(x))
    ax[i,j].set_xlim(90.,7000.)
    #x[i,j].set_ylim(np.min(yp), np.max(yp))
    #x[i,j].set_ylim(1.E-3,1.E2)
    ax[i,j].set_ylim(np.max(yp)/1.E4, np.max(yp)*1.1)
    ax[i,j].set_title(id)

    # Plot SED for BF = 0.50 as a black line
    ax[i,j].plot(x,ym, 'k', linestyle='solid')

    # Plot line_segments (SEDs) all at once following color code defined in array z
    line_segments = LineCollection([np.column_stack([x, y]) for y in yp], linestyles='solid', cmap=plt.cm.get_cmap('gist_rainbow'))
    line_segments.set_array(z)
    sc = ax[i,j].add_collection(line_segments)

    # Show colorbar at indicated position
    plt.tight_layout()
    position=fig.add_axes([0.85,0.58,0.015,0.20])  ## the parameters are the specified position set for the color box
    axcb = fig.colorbar(sc,cax=position)
    axcb.set_label('Binary Fraction')

def plseds(s):
    # Plot one record from one or more SED files (either .fits, .ised, .ased)
    import numpy as np
    import matplotlib.pyplot as plt
    from cycler import cycler
    from myfiles import read_sed,normwav,saveplot

    # Check for normalization
    wn = normwav('N')
    if wn > 0:
        m = True
    else:
        m = False

    # Get files to read and columns to plot
    k = 0
    n = len(s)
    f = ['']*n
    w = [0]*n
    h = [0]*n
    t = [0]*n
    jn= [0]*n
    a = ''
    for i in range(0,n):
        if len(s[i]) > 10:
            k = k+1
            f[k] = s[i]	     # Name of kth file
            w[k],h[k],t[k] = read_sed(f[k])
            if m:
                # Find position in array w[k] of the normalization wavelength = wn
                for j in range(len(w[k])):
                    if w[k][j] <= wn:
                        jn[k] = j
                    else:
                        break
        else:
             a = s[i]	     # Age of seds to plot
    if len(a) <= 0:
        a = '10'

    # Plot style
#   plt.rc('font', family='serif')
#   plt.style.use('seaborn-paper')
#   # plt.style.use('classic')
#   plt.rcParams['axes.prop_cycle'] = cycler(color='bgrcmyk')

    # Build plot
    q = True
    r = False
    xlbl,ylbl = '',''
    while True:
        while True:
            print()
            print('Plotting SED of age ' + a +' Gyr for')
            # fig, ax = plt.subplots(1,1,figsize=(8,8))
            fig, ax = plt.subplots()
            # Turn on minor ticks!!
            ax.minorticks_on()
            ax.set_title('Model SEDs at age ' + a + ' Gyr')
            if not q:
                # Set plot limits entered by user
                if xmax > 1.E4:
                    ax.set_xscale('log')
                ax.set_xlim(xmin,xmax)
                ax.set_ylim(ymin,ymax)
            else:
                # Plot sed's in full range of wavelength and flux
                ax.set_xscale('log')
            ax.set_yscale('log')
            if r:
                # Set axis labels entered by user
                ax.set_xlabel(xlbl)
                ax.set_ylabel(ylbl)
            else:
                # Set axis labels as column numbers
                ax.set_xlabel("Wavelength ($\AA$)")
                if m:
                    ax.set_ylabel('L / L(' + str(int(wn)) + '$\AA$)')
                else:
                    ax.set_ylabel("L (L$_\odot/\AA$)")
            plt.grid(True)
            for l in range(1,k+1):
                ii = np.abs(np.array(t[l]) - float(a)*1.E9).argmin()	# index of element of array t closest in value to age a
                fy = h[l][ii+1][:]
                if m:
#                    # Normalize sed's, find position in array w of the normalization wavelength = wn
#                    for j in range(len(w[l])):
#                        if w[l][j] <= wn:
#                            jn = j
                    # Normalize sed
                    fn = fy[jn[l]]
                    fy = fy/fn
                ax.plot(w[l],fy, linestyle='solid', linewidth=1, label=f[l])
                print('    File ' + str(l) + ': ' + f[l])
            ax.legend(loc='best', frameon=True)
            # Show plot
            #plt.ion()
            saveplot(fig)
            plt.show()
            xmin, xmax = ax.set_xlim()  # return the current xlim
            ymin, ymax = ax.set_ylim()  # return the current ylim
            xmin, xmax, ymin, ymax, q, xlbl, ylbl, r = newlimslogylbl(xmin,xmax,ymin,ymax,xlbl,ylbl,r)
            if q:
                break

        print()
        a = input('Plot SEDs at age (press <Enter> to exit) = ')
        if len(a) <= 0:
           break
        else:
            q = True
            q = False
            r = False

def pltext(s):
    # Plot one column from one or more text files

    import astropy.io.ascii as ascii
    import matplotlib.pyplot as plt
    from  cycler import cycler
    from  myfiles import saveplot
    
    # Number of arguments in command line
    n = len(s)

    # Get files to read and columns to plot
    f = ['']*100
    d = ['']*100
    c = [0]*100
    k = 0
    j = 0
    for i in range(0,n):
        if len(s[i]) > 2:
            k = k+1
            # Name of kth file:
            f[k] = s[i]
            # Read kth file (ascii)
            d[k] = ascii.read(f[k])
        else:
            j = j+1
            # Number of columns to plot
            c[j] = int(s[i])

    # Check columns to plot
    if j>=2:
        xc = c[1]
        yc = c[2]
    elif j==1:
        xc = 1
        yc = c[1]
    else:
        xc = 1
        yc = 2

    # Plot style
    # plt.rc('font', family='serif')
    # plt.style.use('seaborn-paper')
    # plt.style.use('classic')
    # plt.rcParams['axes.prop_cycle'] = cycler(color='bgrcmyk')

    # Build plot
    q = True
    r = False
    xlbl,ylbl = '',''
    while True:
        while True:
            print()
            print('Plotting Column ' + str(yc) + ' vs. Column ' + str(xc) + ' for')
            # fig, ax = plt.subplots(1,1,figsize=(8,8))
            fig, ax = plt.subplots()
            # Turn on minor ticks!!
            ax.minorticks_on()
            if not q:
                # Set plot limits entered by user
                ax.set_xlim(xmin,xmax)
                ax.set_ylim(ymin,ymax)
            if r:
                # Set axis labels entered by user
                ax.set_xlabel(xlbl)
                ax.set_ylabel(ylbl)
            else:
                # Set axis labels as column numbers
                ax.set_xlabel('Column ' + str(xc))
                ax.set_ylabel('Column ' + str(yc))
            #plt.grid(True)
            for i in range(1,k+1):
                # Plot data for the ith file
                ax.plot(d[i][xc-1][:],d[i][yc-1][:], linestyle='solid' , label=f[i])
                print('    File ' + str(i) + ': ' + f[i])
            ax.legend(loc='best')
            # Show plot
            # plt.ion()
            saveplot(fig)
            plt.show()
            xmin, xmax = ax.set_xlim()  # return the current xlim
            ymin, ymax = ax.set_ylim()  # return the current ylim
            xmin, xmax, ymin, ymax, q, xlbl, ylbl, r = newlimslbl(xmin,xmax,ymin,ymax,xlbl,ylbl,r)
            if q:
                break

        print()
        yc = input('Plot column (press <Enter> to exit) = ')
        if len(yc) <= 0:
           break
        else:
            yc = int(yc)
            q = True
            r = False

def sptext(s):
    # Scatter plot of one column from one or more text files

    import astropy.io.ascii as ascii
    import matplotlib.pyplot as plt
    from cycler import cycler

    # Number of arguments in command line
    n = len(s)

    # Get files to read and columns to plot
    f = ['']*100
    d = ['']*100
    c = [0]*100
    k = 0
    j = 0
    for i in range(1,n):
        if len(s[i]) > 2:
            k = k+1
            # Name of kth file:
            f[k] = s[i]
            # Read kth file (ascii)
            d[k] = ascii.read(f[k])
        else:
            j = j+1
            # Number of columns to plot
            c[j] = int(s[i])

    # Check columns to plot
    if j>=2:
        xc = c[1]
        yc = c[2]
    elif j==1:
        xc = 1
        yc = c[1]
    else:
        xc = 1
        yc = 2

    # Plot style
    #plt.rc('font', family='serif')
    #plt.style.use('seaborn-paper')
    # plt.style.use('classic')
    #plt.rcParams['axes.prop_cycle'] = cycler(color='bgrcmyk')

    # Build plot
    q = True
    r = False
    xlbl,ylbl = '',''
    while True:
        while True:
            print()
            print('Plotting Column ' + str(yc) + ' vs. Column ' + str(xc) + ' for')
            fig, ax = plt.subplots(1,1,figsize=(10,8))
            ax.minorticks_on()
            if not q:
                # Set plot limits entered by user
                ax.set_xlim(xmin,xmax)
                ax.set_ylim(ymin,ymax)
            if r:
                # Set axis labels entered by user
                ax.set_xlabel(xlbl)
                ax.set_ylabel(ylbl)
            else:
                # Set axis labels as column numbers
                ax.set_xlabel('Column ' + str(xc))
                ax.set_ylabel('Column ' + str(yc))
            plt.grid(True)
            for i in range(1,k+1):
                # Plot data for the ith file
                # ax.plot(d[i][xc-1][:],d[i][yc-1][:], linestyle='solid' , label=f[i])
                # ax.scatter(d[i][xc-1][:],d[i][yc-1][:], c='dodgerblue', marker='o', s=30, alpha=1.0, label=f[i])
                ax.scatter(d[i][xc-1][:],d[i][yc-1][:], c='dodgerblue', marker='o', s=1, alpha=1.0, label=f[i])
                # ax.scatter(d[i][xc-1][:],d[i][yc-1][:], marker='.', s=20, label=f[i])
                print('    File ' + str(i) + ': ' + f[i] + ',    ' + str(len(d[i])) + ' data points')
            ax.legend(loc='best')
            xmin, ymin, xend, yend = 0, 0, 0.005, 0.005
            ax.plot((xmin, xend), (ymin, yend), 'k')
            xmin, ymin, xend, yend = 0, 0, 0.005, 0.01
            ax.plot((xmin, xend), (ymin, yend), 'red')
            xmin, ymin, xend, yend = 0, 0, 0.005, 0.0025
            ax.plot((xmin, xend), (ymin, yend), 'red')
            # Show plot
            plt.ion()
            plt.show()
            xmin, xmax = ax.set_xlim()  # return the current xlim
            ymin, ymax = ax.set_ylim()  # return the current ylim
            xmin, xmax, ymin, ymax, q, xlbl, ylbl, r = newlimslbl(xmin,xmax,ymin,ymax,xlbl,ylbl,r)
            if q:
                break

        print()
        yc = input('Plot column (press <Enter> to exit) = ')
        if len(yc) <= 0:
           break
        else:
            yc = int(yc)
            q = True
            r = False
