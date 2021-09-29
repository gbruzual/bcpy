def bands():
    # Print photometric bands available in fits file

    # '         Mbol', '    U_Johnson', '   B2_Johnson', '   B3_Johnson', '    V_Johnson', '    R_Johnson', '    I_Johnson', '    J_Johnson', '    K_Johnson', '    L_Johnson',
    # '    R_Cousins', '    I_Cousins', '    J_Palomar', '    H_Palomar', '    K_Palomar', '      J_2Mass', '      H_2Mass', '     Ks_2Mass', ' Kprime_Cowie', '    I3p6_IRAC',
    # '    I4p5_IRAC', '    I5p7_IRAC', '    I7p9_IRAC', '     I12_IRAS', '     I25_IRAS', '     I60_IRAS', '    I100_IRAS', '     M24_MIPS', '     M70_MIPS', '    M160_MIPS',
    # '       u_SDSS_AB', '       g_SDSS_AB', '       r_SDSS_AB', '       i_SDSS_AB', '       z_SDSS_AB', '   u1_CFHT_MC_AB', '   u3_CFHT_MC_AB', '   g1_CFHT_MC_AB', '   g3_CFHT_MC_AB', '   r1_CFHT_MC_AB',
    # '   r3_CFHT_MC_AB', '   i2_CFHT_MC_AB', '   i3_CFHT_MC_AB', '   z1_CFHT_MC_AB', '   z3_CFHT_MC_AB', '      H_2MASS_AB', '   Ks_CFHT_WC_AB', '    FUV_GALEX_AB', '    NUV_GALEX_AB',
    # '   WFC3_F225W_AB', '   WFC3_F336W_AB', '  WFC3_FR388N_AB', '   WFC3_F438W_AB', '   WFC3_F555W_AB', '   WFC3_F814W_AB', '   WFC3_F110W_AB', '   WFC3_F125W_AB', '   WFC3_F160W_AB',
    # '  UVIS1_f225w_AB', '  UVIS1_f275w_AB', '  UVIS1_f336w_AB', '  UVIS1_f438w_AB', '  UVIS1_f555w_AB', '  UVIS1_f547m_AB', '  UVIS1_f606w_AB', '  UVIS1_f625w_AB', '  UVIS1_f656n_AB',
    # '  UVIS1_f657n_AB', '  UVIS1_f658n_AB', '  UVIS1_f814w_AB', ' ACSWFC_F220w_AB', ' ACSWFC_F250w_AB', ' ACSWFC_F330w_AB', ' ACSWFC_F410w_AB', ' ACSWFC_F435w_AB', ' ACSWFC_F475w_AB',
    # ' ACSWFC_F555w_AB', ' ACSWFC_F606w_AB', ' ACSWFC_F625w_AB', ' ACSWFC_F775w_AB', ' ACSWFC_F814w_AB',
    b = ['Mbol','U_Johnson','B2_Johnson','B3_Johnson','V_Johnson','R_Johnson','I_Johnson','J_Johnson','K_Johnson','L_Johnson','R_Cousins','I_Cousins','J_Palomar','H_Palomar','K_Palomar',
         'J_2Mass','H_2Mass','Ks_2Mass','Kprime_Cowie','I3p6_IRAC','I4p5_IRAC','I5p7_IRAC','I7p9_IRAC','I12_IRAS','I25_IRAS','I60_IRAS','I100_IRAS','M24_MIPS','M70_MIPS','M160_MIPS',
         'u_SDSS_AB','g_SDSS_AB','r_SDSS_AB','i_SDSS_AB','z_SDSS_AB','u1_CFHT_MC_AB','u3_CFHT_MC_AB','g1_CFHT_MC_AB','g3_CFHT_MC_AB','r1_CFHT_MC_AB','r3_CFHT_MC_AB','i2_CFHT_MC_AB',
         'i3_CFHT_MC_AB','z1_CFHT_MC_AB','z3_CFHT_MC_AB','H_2MASS_AB','Ks_CFHT_WC_AB','FUV_GALEX_AB','NUV_GALEX_AB','WFC3_F225W_AB','WFC3_F336W_AB','WFC3_FR388N_AB','WFC3_F438W_AB',
         'WFC3_F555W_AB','WFC3_F814W_AB','WFC3_F110W_AB','WFC3_F125W_AB','WFC3_F160W_AB','UVIS1_f225w_AB','UVIS1_f275w_AB','UVIS1_f336w_AB','UVIS1_f438w_AB','UVIS1_f555w_AB','UVIS1_f547m_AB',
         'UVIS1_f606w_AB','UVIS1_f625w_AB','UVIS1_f656n_AB','UVIS1_f657n_AB','UVIS1_f658n_AB','UVIS1_f814w_AB','ACSWFC_F220w_AB','ACSWFC_F250w_AB','ACSWFC_F330w_AB','ACSWFC_F410w_AB',
         'ACSWFC_F435w_AB','ACSWFC_F475w_AB','ACSWFC_F555w_AB','ACSWFC_F606w_AB','ACSWFC_F625w_AB','ACSWFC_F775w_AB','ACSWFC_F814w_AB']
    print()
    print("Photometric bands available in this fits file:")
    print()
    print("  N        Band      N       Band      N           Band      N            Band      N             Band")
    print("  -------------     -------------     -----------------     ------------------     -------------------")
    print("  0:       Mbol     15:   J_2Mass     30:     u_SDSS_AB     49:  WFC3_F225W_AB     70: ACSWFC_F220w_AB")
    print("                    16:   H_2Mass     31:     g_SDSS_AB     50:  WFC3_F336W_AB     71: ACSWFC_F250w_AB")
    print("  1:  U_Johnson     17:  Ks_2Mass     32:     r_SDSS_AB     51: WFC3_FR388N_AB     72: ACSWFC_F330w_AB")
    print("  2: B2_Johnson                       33:     i_SDSS_AB     52:  WFC3_F438W_AB     73: ACSWFC_F410w_AB")
    print("  3: B3_Johnson     18:  K'_Cowie     34:     z_SDSS_AB     53:  WFC3_F555W_AB     74: ACSWFC_F435w_AB")
    print("  4:  V_Johnson                                             54:  WFC3_F814W_AB     75: ACSWFC_F475w_AB")
    print("  5:  R_Johnson     19: I3.6_IRAC     35: u1_CFHT_MC_AB     55:  WFC3_F110W_AB     76: ACSWFC_F555w_AB")
    print("  6:  I_Johnson     20: I4.5_IRAC     36: u3_CFHT_MC_AB     56:  WFC3_F125W_AB     77: ACSWFC_F606w_AB")
    print("  7:  J_Johnson     21: I5.7_IRAC     37: g1_CFHT_MC_AB     57:  WFC3_F160W_AB     78: ACSWFC_F625w_AB")
    print("  8:  K_Johnson     22: I7.9_IRAC     38: g3_CFHT_MC_AB                            79: ACSWFC_F775w_AB")
    print("  9:  L_Johnson                       39: r1_CFHT_MC_AB     58: UVIS1_f225w_AB     80: ACSWFC_F814w_AB")
    print("                    23:  I12_IRAS     40: r3_CFHT_MC_AB     59: UVIS1_f275w_AB")
    print(" 10:  R_Cousins     24:  I25_IRAS     41: i2_CFHT_MC_AB     60: UVIS1_f336w_AB")
    print(" 11:  I_Cousins     25:  I60_IRAS     42: i3_CFHT_MC_AB     61: UVIS1_f438w_AB")
    print("                    26: I100_IRAS     43: z1_CFHT_MC_AB     62: UVIS1_f555w_AB")
    print(" 12:  J_Palomar                       44: z3_CFHT_MC_AB     63: UVIS1_f547m_AB")
    print(" 13:  H_Palomar     27:  M24_MIPS     45:    H_2MASS_AB     64: UVIS1_f606w_AB")
    print(" 14:  K_Palomar     28:  M70_MIPS     46: Ks_CFHT_WC_AB     65: UVIS1_f625w_AB")
    print("                    29: M160_MIPS                           66: UVIS1_f656n_AB")
    print("                                      47:  FUV_GALEX_AB     67: UVIS1_f657n_AB")
    print("                                      48:  NUV_GALEX_AB     68: UVIS1_f658n_AB")
    print("                                                            69: UVIS1_f814w_AB")
    return b

def indices():
    # Print line strength indices available in fits file

    # 'logage'   , 'CN_1     ', 'CN_2     ', 'Ca4227   ', 'G4300    ', 'Fe4383   ', 'Ca4455   ', 'Fe4531   ', 'Fe4668   ', 'Hbeta    ', 'Fe5015   ', 'Mg_1     ', 'Mg_2     ', 'Mg-b     ', 'Fe5270   ',
    # 'Fe5335   ', 'Fe5406   ', 'Fe5709   ', 'Fe5782   ', 'Na-D     ', 'TiO_1    ', 'TiO_2    ', 'HdeltaA  ', 'HgammaA  ', 'HdeltaF  ', 'HgammaF  ', 'D4000    ', 'B4000_VN ', 'CaII8498 ',
    # 'CaII8542 ', 'CaII8662 ', 'MgI8807  ', 'H8_3889  ', 'H9_3835  ', 'H10_3798 ', 'BH-HK    ', 'BL1302   ', 'SiIV     ', 'BL1425   ', 'Fe1453   ', 'CIV1548a ', 'CIV1548c ', 'CIV1548e ',
    # 'BL1617   ', 'BL1664   ', 'BL1719   ', 'BL1853   ', 'FeII2402 ', 'BL2538   ', 'FeII2609 ', 'MgII     ', 'MgI      ', 'Mgwide   ', 'FeI      ', 'BL3096   ', 'CIVabs   ', 'HeIIems  '
    b = ['logage','CN_1','CN_2','Ca4227','G4300','Fe4383','Ca4455','Fe4531','Fe4668','Hbeta','Fe5015','Mg_1','Mg_2','Mg-b','Fe5270',
         'Fe5335','Fe5406','Fe5709','Fe5782','Na-D','TiO_1','TiO_2','HdeltaA','HgammaA','HdeltaF','HgammaF','D4000','B4000_VN','CaII8498',
         'CaII8542','CaII8662','MgI8807','H8-3889','H9-3835','H10-3798','BH-HK','BL1302','SiIV','BL1425','Fe1453','CIV1548a','CIV1548c','CIV1548e',
         'BL1617','BL1664','BL1719','BL1853','FeII2402','BL2538','FeII2609','MgII','MgI','Mgwide','FeI','BL3096','CIVabs','HeIIems']
    u = ['yr','(mag)','(mag)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(mag)','(mag)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(mag)','(mag)','(A)','(A)','(A)','(A)','','','(A)','(A)','(A)',
         '(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)','(A)']
    print()
    print("Line strength indices available in this fits file:")
    print()
    print("  <----- Lick Indices ----->      <-- W&O -->      <--- DTT -->      <- Fanelli et al. UV Indices ->")
    print("  N  Index         N  Index        N  Index         N  Index          N  Index           N  Index")
    print("  --------------------------      -----------      ------------      -------------------------------")
    print("  1: CN_1         11: Mg_1        22: HdeltaA      28: CaII8498      36: BL1302         47: FeII2402")
    print("  2: CN_2         12: Mg_2        23: HgammaA      29: CaII8542      37: SiIV           48: BL2538")
    print("  3: Ca4227       13: Mg-b        24: HdeltaF      30: CaII8662      38: BL1425         49: FeII2609")
    print("  4: G4300        14: Fe5270      25: HgammaF      31: MgI8807       39: Fe1453         50: MgII")
    print("  5: Fe4383       15: Fe5335                                         40: CIV1548a       51: MgI")
    print("  6: Ca4455       16: Fe5406      <- 4000A ->      <Marcillac>       41: CIV1548c       52: Mgwide")
    print("  7: Fe4531       17: Fe5709      ----------       -----------       42: CIV1548e       53: FeI")
    print("  8: Fe4668       18: Fe5782      26: D(4000)      32: H8-3889       43: BL1617         54: BL3096")
    print("  9: Hbeta        19: Na-D        27: B4000_VN     33: H9-3835       44: BL1664         55: CIVabs")
    print(" 10: Fe5015       20: TiO_1                        34: H10-3798      45: BL1719         56: HeIIems")
    print("                  21: TiO_2                        35: BH-HK         46: BL1853")
    return b,u

def properties():
    # Print physical properties available in fits file
    b = ['logage', 'logNLy', 'logNHeI', 'logNHeII', 'logNHeII-logNLy', 'B912', 'B4000VN', 'B4000SDSS', 'B4000', 'Mbol', 'BolFlux', 'SNR', 'NBH', 'NNS', 'PNBR', 'NWD', 
         'Mstars', 'Mremnants', 'Mretgas', 'Mgalaxy', 'SFR', 'Mtot', 'Mtot_Lb', 'Mtot_Lv', 'Mtot_Lk', 'Mliv_Lb', 'Mliv_Lv', 'Mliv_Lk', 
         'EvolutionaryFlux', 'SpecificEvolFlux', 'TurnoffMass', 'BPMS_BMS', 'TotalMassLossRate', 'DustProductionRate']
    u = ['(yr)','(photons/Mo)','(photons/Mo)','(photons/Mo)','','','','','','(Vegamag)','(Lo)','(SN/yr/Lo/Mo)','(number/Mo)','(number/Mo)','(PN/yr/Lo/Mo)','(number/Mo)','(Mo)','(Mo)',
         '(Mo)','(Mo)','(Mo/yr)','(Mo)','(Mo/Lo)','(Mo/Lo)','(Mo/Lo)','(Mo/Lo)','(Mo/Lo)','(Mo/Lo)','(Nstars/yr)','(Nstars/yr/Lo)','(Mo)','','(M/Mo/yr)','(M/Mo/yr)']
    print()
    print("Physical properties available in this fits file:")
    print()
    print("  N  Property                             N  Property                              N  Property")
    print("  ---------------------------------      -----------------------------------      ------------------------------")
    print("  1: HI ionizing photons                 11: Supernova rate                       21: Mtot = Mliv + Mrem")
    print("  2: HeI ionizing photons                12: Number of black holes                22: Mtot/L(B)")
    print("  3: HeII ionizing photons               13: Number of neutron stars              23: Mtot/L(V)")
    print("  4: Ratio HeII/HI ionizing photons      14: Planetary nebula birth rate          24: Mtot/L(K)")
    print("                                         15: Number of white dwarfs               25: Mliv/L(B)")
    print("  5:  912 A break amplitude                                                       26: Mliv/L(V)")
    print("  6: 4000 A break amplitude (VN)         16: Mliv = Mass in living stars          27: Mliv/L(K)")
    print("  7: 4000 A break amplitude (SDSS)       17: Mrem = Mass in stellar remnants")
    print("  8: 4000 A break amplitude              18: Mgas = Mass in processed gas         28: Evolutionary flux")
    print("                                         19: Mgal = Mass of galaxy                29: Specific evolutionary flux")
    print("  9: Bolometric magnitude                         = Mliv+ Mrem + Mgas             30: Turnoff mass")
    print(" 10: Bolometric flux                     20: Star formation rate                  31: Bol flux PMS / Bol flux MS")
    print("                                                                                  32: Total mass loss rate")
    print("                                                                                  33: Dust production rate")
    return b,u
