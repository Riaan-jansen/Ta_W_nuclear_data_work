"""
basic data class
"""
import os
import pandas as pd

class basic_data():
    def __init__(self):
        self.density_data = self.read_density_data()
        self.hl_data = self.read_hl_data()
        
    def read_density_data(self):
        path = "Data\densities.xlsx"
        df = pd.read_excel(path)
        return df
    
    def get_density_value(self, mat):
        df = self.density_data
        return df.loc[df['Element'] == mat, 'Density'].item()    
        
    def read_hl_data(self):
        path = "Data\HL.xlsx"
        df = pd.read_excel(path)
        return df
        
    def get_hl_value(self, nuc):
        df = self.hl_data
        return df.loc[df['Name'] == nuc, 'HL_S'].item()
    