"""
file reader for excel cross section data 
"""
import pandas as pd

class xs_data():
    def __init__(self):
        self.target_z = None
        self.target_A = None
        self.projectile = None
        self.reaction = None
        self.quantity = None
        self.MF = None
        self.MT = None
        self.data = None

def get_xs_path(nuclide, reaction, lib):
    """   """
    reaction = str(reaction)
    if len(reaction)== 1:
        reaction = "00" + reaction
    elif len(reaction)==2:
        reaction = "0" + reaction
    path = "Data/xs_data/" + lib +"/"    
    path = path + reaction + "/" + nuclide + "_" + reaction + ".xlsx" 

    return path

    
def clean_line(line):
    line = line.strip()
    line = " ".join(line.split())
    return line

    
def get_parameter(line):
    line = clean_line(line)
    line = line.split(":")
    return line[-1]    
        
        
def read_xs(path):
    lib_data = pd.read_excel(path)
    
    return lib_data
    