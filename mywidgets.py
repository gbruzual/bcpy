import ipywidgets as widgets
from   ipywidgets import interact, Dropdown, interactive, fixed, interact_manual
import  mywidgets
import  myfiles   as myfiles

def get_user_selection(a): # A default arg is needed here
    # Function for the button to select user input and do work
    # Displays the current value of various dropdown menus
    print(dd1.value,dd2.value,dd3.value,dd4.value)

def namewidget(O,Model,Z,IMF,Mup,Library):
    # Builds file name according to dropdown menu selection
    # name = 'bc2020_z001_chab_lr_BaSeL_ssp.fits'
    # name = 'bc2020_z008_chab_MU300_hr_stelib_ssp.fits'
    import os

    filew = ''
    if Model == 'None':
        filew = 'None'
    elif Model == 'BC2003':
        filew = 'bc2003'
    elif Model == 'BC2019':
        filew = 'bc2019'
    elif Model == 'CB2019':
        filew = 'cb2019'
    elif Model == 'BC2020':
        filew = 'bc2020'
    elif Model == 'CB2020':
        filew = 'cb2020'
    
    if Z == '0':
        filew = filew + '_z0000_'
    elif Z == '0.0001':
        filew = filew + '_z0001_'
    elif Z == '0.0002':
        filew = filew + '_z0002_'
    elif Z == '0.0004':
        filew = filew + '_z0004_'
    elif Z == '0.0005':
        filew = filew + '_z0005_'
    elif Z == '0.001':
        filew = filew + '_z001_'
    elif Z == '0.002':
        filew = filew + '_z002_'
    elif Z == '0.004':
        filew = filew + '_z004_'
    elif Z == '0.006':
        filew = filew + '_z006_'
    elif Z == '0.008':
        filew = filew + '_z008_'
    elif Z == '0.010':
        filew = filew + '_z010_'
    elif Z == '0.014':
        filew = filew + '_z014_'
    elif Z == '0.017':
        filew = filew + '_z017_'
    elif Z == '0.019':
        filew = filew + '_z019_'
    elif Z == '0.020':
        filew = filew + '_z020_'
    elif Z == '0.030':
        filew = filew + '_z030_'
    elif Z == '0.040':
        filew = filew + '_z040_'
    elif Z == '0.050':
        filew = filew + '_z050_'
    elif Z == '0.060':
        filew = filew + '_z060_'
    elif Z == '0.100':
        filew = filew + '_z100_'
    
    if IMF == 'Chabrier':
        filew = filew + 'chab_'
    elif IMF == 'Kroupa':
        filew = filew + 'kroup_'
    elif IMF == 'Salpeter':
        filew = filew + 'salp_'

    if Mup == '300':
        filew = filew + 'MU300_'
    elif Mup == '600':
        filew = filew + 'MU600_'
  
    if Library == 'Miles':
        filew = filew + 'hr_xmilesi_ssp.fits'
    elif Library == 'IndoUS':
        filew = filew + 'hr_xindous_ssp.fits'
    elif Library == 'Stelib':
        filew = filew + 'hr_stelib_ssp.fits'
    elif Library == 'BaSeL':
        filew = filew + 'lr_BaSeL_ssp.fits'

    # return and global do not seem to work with interact widget.
    # temporary solution is to write filew to a file
    if O == 1:
        of = open(os.getenv('PYTHON') + '/tmp/file1.tmp',"w")
        of.write(filew)
        of.close()
    elif O == 2:
        if str(filew).find("None") < 0:
            of = open(os.getenv('PYTHON') + '/tmp/file2.tmp',"w")
            of.write(filew)
        else:
            if os.path.isfile(os.getenv('PYTHON') + '/tmp/file2.tmp'):
                os.remove(os.getenv('PYTHON') + '/tmp/file2.tmp')
    return filew

def select_file(O):
    import os
    from myfiles import inputc
    from galaxev import mfile

    # Ask for name of up to 2 fits file to plot
    if O == 0:
        # Get file names directly from the keyboard
        n,file1,file2 = mfile()
        if n==2:
            of = open(os.getenv('PYTHON') + '/tmp/file1.tmp',"w")
            of.write(file1)
            of.close()
        elif n==3:
            of = open(os.getenv('PYTHON') + '/tmp/file1.tmp',"w")
            of.write(file1)
            of.close()
            of = open(os.getenv('PYTHON') + '/tmp/file2.tmp',"w")
            of.write(file2)
            of.close()

    else:
        # Create dropdown widgtes to build BC/CB model file names
        # Use linked dropdown widgets to select type of model and Z
        if O == 1:
            bc = {'BC2003':['0.020','0.0001','0.0004','0.004','0.008','0.020','0.050'],
                  'BC2019':['0.017','0','0.0001','0.0002','0.0005','0.001','0.002','0.004','0.006','0.008','0.010','0.014','0.017','0.020','0.030','0.040','0.060'],
                  'CB2019':['0.017','0','0.0001','0.0002','0.0005','0.001','0.002','0.004','0.006','0.008','0.010','0.014','0.017','0.020','0.030','0.040','0.060'],
                  'BC2020':['0.014','0.0001','0.0005','0.001','0.002','0.006','0.008','0.014','0.020','0.040'],
                  'CB2020':['0.014','0.0001','0.0005','0.001','0.002','0.006','0.008','0.014','0.020','0.040']}
            mW = Dropdown(options = bc.keys(), description='Model', value='CB2019')

        elif O == 2:
            bc = {  'None':['0.020','0.0001','0.0004','0.004','0.008','0.020','0.050'],
                  'BC2003':['0.020','0.0001','0.0004','0.004','0.008','0.020','0.050'],
                  'BC2019':['0.017','0','0.0001','0.0002','0.0005','0.001','0.002','0.004','0.006','0.008','0.010','0.014','0.017','0.020','0.030','0.040','0.060'],
                  'CB2019':['0.017','0','0.0001','0.0002','0.0005','0.001','0.002','0.004','0.006','0.008','0.010','0.014','0.017','0.020','0.030','0.040','0.060'],
                  'BC2020':['0.014','0.0001','0.0005','0.001','0.002','0.006','0.008','0.014','0.020','0.040'],
                  'CB2020':['0.014','0.0001','0.0005','0.001','0.002','0.006','0.008','0.014','0.020','0.040']}
            mW = Dropdown(options = bc.keys(), description='Model', value='None')
        zW = Dropdown(description='Z')

        # Create dropdown widget to select IMF
        bf3 = ['Chabrier', 'Kroupa', 'Salpeter']
        dd3 = widgets.Dropdown(
            options=bf3, # Object to iterate over
            description='IMF', # User defined 
            value=bf3[0], # Default value selection
            rows=len(bf3), # The number of rows to display when showing the box
            interactive=True, # This makes the box interactive, true by default
        )

        # Create dropdown widget to select Mup
        bf4 = ['100', '300', '600']
        dd4 = widgets.Dropdown(
            options=bf4, # Object to iterate over
            description='Mup', # User defined 
            value=bf4[0], # Default value selection
            rows=len(bf4), # The number of rows to display when showing the box
            interactive=True, # This makes the box interactive, true by default
        )

        # Create dropdown widget to select Spectral Library
        bf5 = ['Miles', 'IndoUS', 'Stelib', 'BaSeL']
        dd5 = widgets.Dropdown(
            options=bf5, # Object to iterate over
            description='Library', # User defined 
            value=bf5[0], # Default value selection
            rows=len(bf5), # The number of rows to display when showing the box
            interactive=True, # This makes the box interactive, true by default
        )

        @interact(Model = mW, Z = zW, IMF = dd3, Mup = dd4, Library = dd5, __output_result=False)
        def filen(Model, Z, IMF, Mup, Library):
            zW.options = bc[Model] # Here is the trick, i.e. update zW.options based on model, namely modelW.value.
            filew = namewidget(O,Model,zW.value,IMF,Mup,Library)
            print('     File: ' + filew)
