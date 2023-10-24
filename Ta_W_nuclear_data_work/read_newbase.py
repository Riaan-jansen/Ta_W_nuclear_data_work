"""
file reader for newbase cross section data 
"""
import glob
import os
import pandas as pd

class xs_exp_data():
    def __init__(self):
        self.target_z = None
        self.target_A = None
        self.projectile = None
        self.reaction = None
        self.quantity = None
        self.MF = None
        self.MT = None
        self.author = None
        self.year = None
        self.data = None

def get_exps_paths(nuclide, reaction):
    """   """
    reaction = str(reaction)
    if len(reaction)== 1:
        reaction = "00" + reaction
    elif len(reaction)==2:
        reaction = "0" + reaction
    path = "Data/xs_data/old_exp/" 
    path = path + nuclide + "/xs/" + reaction + "/"
    
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    exp_paths = []
    for file in onlyfiles:
        exp_paths.append(path + file)
    
    return exp_paths

    
def clean_line(line):
    line = line.strip()
    line = " ".join(line.split())
    return line

    
def get_parameter(line):
    line = clean_line(line)
    line = line.split(":")
    return line[-1]    
        
        
def read_newbase_xs(path):
    with open(path) as f:
        lines = f.read().splitlines()
    f.close()
    
    exp_data = xs_exp_data()
    exp_data.target_z = get_parameter(lines[0])
    exp_data.target_A = get_parameter(lines[1])
    exp_data.projectile = get_parameter(lines[3])
    exp_data.reaction = get_parameter(lines[4])
    exp_data.quantity = get_parameter(lines[6])
    exp_data.MF = get_parameter(lines[8])
    exp_data.MT = get_parameter(lines[9])
    exp_data.author = get_parameter(lines[12])
    exp_data.year = get_parameter(lines[13])
    
    data = []
    for line in lines:
        if line[0] != "#":
            line = clean_line(line)
            line = list(map(float, line.split()))
            if len(line) == 4:
                line.append(0)
                line.append(0)
                line.append(0)
                line.append(0)
            data.append(line)
    heading = ("Energy", "xs", "dxs", "dE", "eval", "C/E", "chi2", "delta")
    df = pd.DataFrame(data, columns = heading)
    exp_data.data = df
    
    return exp_data
    