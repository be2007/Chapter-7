"""
Gas properties
"""

# Number of bromine atoms
br_atoms = {
    'CCl4': 0,
    'CFC11': 0,
    'CFC113': 0,
    'CFC114': 0,
    'CFC115': 0,
    'CFC12': 0,
    'CH2Cl2': 0,
    'CH3Br': 1,
    'CH3CCl3': 0,
    'CH3Cl': 0,
    'CHCl3': 0,
    'HCFC141b': 0,
    'HCFC142b': 0,
    'HCFC22': 0,
    'Halon1211': 1,
    'Halon1301': 1,
    'Halon2402': 2,
}

# Number of chlorine atoms
cl_atoms = {
    'CCl4': 4,
    'CFC11': 3,
    'CFC113': 3,
    'CFC114': 2,
    'CFC115': 1,
    'CFC12': 2,
    'CH2Cl2': 2,
    'CH3Br': 0,
    'CH3CCl3': 3,
    'CH3Cl': 1,
    'CHCl3': 3,
    'HCFC141b': 2,
    'HCFC142b': 1,
    'HCFC22': 1,
    'Halon1211': 0,
    'Halon1301': 0,
    'Halon2402': 0,
}

# Fractional release (for ozone depletion)
# References:
# Daniel, J. and Velders, G.: A focus on information and options for 
#   policymakers, in: Scientific Assessment of Ozone Depletion, WMO, 2011
# Newman et al., 2007: A new formulation of equivalent effective stratospheric
#   chlorine (EESC)
fracrel = {
    'CCl4': 0.56,
    'CFC11': 0.47,
    'CFC113': 0.29,
    'CFC114': 0.12,
    'CFC115': 0.04,
    'CFC12': 0.23,
    'CH2Cl2': 0, # no literature value available
    'CH3Br': 0.60,
    'CH3CCl3': 0.67,
    'CH3Cl': 0.44,
    'CHCl3': 0, # no literature value available
    'HCFC141b': 0.34,
    'HCFC142b': 0.17,
    'HCFC22': 0.13,
    'Halon1211': 0.62,
    'Halon1301': 0.28,
    'Halon2402': 0.65,
}

# Conversion between GHG names in GHG spreadsheet and RCMIP.
ghg_to_rcmip_names={
    'HFC-125':      'HFC125',
    'HFC-134a':     'HFC134a',
    'HFC-143a':     'HFC143a',
    'HFC-152a':     'HFC152a',
    'HFC-227ea':    'HFC227ea',
    'HFC-23':       'HFC23',
    'HFC-236fa':    'HFC236fa',
    'HFC-245fa':    'HFC245fa',
    'HFC-32':       'HFC32',
    'HFC-365mfc':   'HFC365mfc',
    'HFC-43-10mee': 'HFC4310mee',
    'NF3':          'NF3',
    'C2F6':         'C2F6',
    'C3F8':         'C3F8',
    'n-C4F10':      'C4F10',
    'n-C5F12':      'C5F12',
    'n-C6F14':      'C6F14',
    'i-C6F14':      None,
    'C7F16':        'C7F16',
    'C8F18':        'C8F18',
    'CF4':          'CF4',
    'c-C4F8':       'cC4F8',
    'SF6':          'SF6',
    'SO2F2':        'SO2F2',
    'CCl4':         'CCl4',
    'CFC-11':       'CFC11',
    'CFC-112':      'CFC112',  
    'CFC-112a':     None,  
    'CFC-113':      'CFC113',
    'CFC-113a':     None,  
    'CFC-114':      'CFC114',
    'CFC-114a':     None, 
    'CFC-115':      'CFC115',
    'CFC-12':       'CFC12',
    'CFC-13':       None,
    'CH2Cl2':       'CH2Cl2',
    'CH3Br':        'CH3Br',
    'CH3CCl3':      'CH3CCl3',
    'CH3Cl':        'CH3Cl',
    'CHCl3':        'CHCl3',
    'HCFC-124':     None,
    'HCFC-133a':    None,
    'HCFC-141b':    'HCFC141b',
    'HCFC-142b':    'HCFC142b',
    'HCFC-22':      'HCFC22',
    'HCFC-31':      None,
    'Halon-1211':   'Halon1211',
    'Halon-1301':   'Halon1301',
    'Halon-2402':   'Halon2402',
}

# Hodnebrog et al., 2020: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019RG000691
lifetimes = {
    'HFC-125':      30,
    'HFC-134a':     14,
    'HFC-143a':     51,
    'HFC-152a':     1.6,
    'HFC-227ea':    36,
    'HFC-23':       228,
    'HFC-236fa':    213,
    'HFC-245fa':    7.9,
    'HFC-32':       5.4,
    'HFC-365mfc':   8.9,
    'HFC-43-10mee': 17,
    'NF3':          569,
    'C2F6':         10000,
    'C3F8':         2600,
    'n-C4F10':      2600,
    'n-C5F12':      4100,
    'n-C6F14':      3100,
    'i-C6F14':      3100,  # assumed
    'C7F16':        3000,
    'C8F18':        3000,
    'CF4':          50000,
    'c-C4F8':       3200,
    'SF6':          3200,
    'SO2F2':        36,
    'CCl4':         32,
    'CFC-11':       52,
    'CFC-112':      63.6,
    'CFC-112a':     52,
    'CFC-113':      93,
    'CFC-113a':     55,
    'CFC-114':      189,
    'CFC-114a':     105,
    'CFC-115':      540,
    'CFC-12':       102,
    'CFC-13':       640,
    'CH2Cl2':       0.4932,
    'CH3Br':        0.8,
    'CH3CCl3':      5,
    'CH3Cl':        0.9,
    'CHCl3':        0.5014,
    'HCFC-124':     5.9,
    'HCFC-133a':    4.6,
    'HCFC-141b':    9.4,
    'HCFC-142b':    18,
    'HCFC-22':      11.9,
    'HCFC-31':      1.2,
    'Halon-1211':   16,
    'Halon-1301':   72,
    'Halon-2402':   28,
}

# Ozone depleting substances
ods_species = [
    'CCl4',
    'CFC11',
    'CFC113',
    'CFC114',
    'CFC115',
    'CFC12',
    'CH2Cl2',
    'CH3Br',
    'CH3CCl3',
    'CH3Cl',
    'CHCl3',
    'HCFC141b',
    'HCFC142b',
    'HCFC22',
    'Halon1211',
    'Halon1301',
    'Halon2402',
]

# radiative efficiencies
# source: Hodnebrog et al 2020 https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2019RG000691
radeff = {
    'HFC-125':      0.23378,
    'HFC-134a':     0.16714,
    'HFC-143a':     0.168,
    'HFC-152a':     0.10174,
    'HFC-227ea':    0.27325,
    'HFC-23':       0.19111,
    'HFC-236fa':    0.25069,
    'HFC-245fa':    0.24498,
    'HFC-32':       0.11144,
    'HFC-365mfc':   0.22813,
    'HFC-43-10mee': 0.35731,
    'NF3':          0.20448,
    'C2F6':         0.26105,
    'C3F8':         0.26999,
    'n-C4F10':      0.36874,
    'n-C5F12':      0.4076,
    'n-C6F14':      0.44888,
    'i-C6F14':      0.44888,
    'C7F16':        0.50312,
    'C8F18':        0.55787,
    'CF4':          0.09859,
    'c-C4F8':       0.31392,
    'SF6':          0.56657,
    'SO2F2':        0.21074,
    'CCl4':         0.16616,
    'CFC-11':       0.25941,
    'CFC-112':      0.28192,
    'CFC-112a':     0.24564,
    'CFC-113':      0.30142,
    'CFC-113a':     0.24094, 
    'CFC-114':      0.31433,
    'CFC-114a':     0.29747,
    'CFC-115':      0.24625,
    'CFC-12':       0.31998,
    'CFC-13':       0.27752,
    'CH2Cl2':       0.02882,
    'CH3Br':        0.00432,
    'CH3CCl3':      0.06454,
    'CH3Cl':        0.00466,
    'CHCl3':        0.07357,
    'HCFC-124':     0.20721,
    'HCFC-133a':    0.14995,
    'HCFC-141b':    0.16065,
    'HCFC-142b':    0.19329,
    'HCFC-22':      0.21385,
    'HCFC-31':      0.068,
    'Halon-1211':   0.30014,
    'Halon-1301':   0.29943,
    'Halon-2402':   0.31169,
}

rcmip_to_ghg_names = {v: k for k, v in ghg_to_rcmip_names.items()}

