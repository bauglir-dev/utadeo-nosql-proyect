# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

# Cambiar para que acepte ruta relativa
dirpath = 'E:\\utadeo\\utadeo-nosql-proyect\\data\\'

dforigin = pd.read_csv(dirpath + 'train.csv')

dfcustomer = dforigin[['id', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']]
dfvehicle = dforigin[['id', 'Vehicle_Age', 'Vehicle_Damage']]

dfinsure = dforigin[['Annual_Premium', 'Policy_Sales_Channel', 'Response']]
dfinsure['_from'] = 'customers/' + dfcustomer['id'].astype(str)
dfinsure['_to'] = 'vehicles/' + dfvehicle['id'].astype(str)

dfcustomer.columns = ['_key', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']
dfcustomer.to_csv(dirpath + 'customers.csv', index=False)
#dfcustomer.to_json(dirpath + 'customers.json')

dfvehicle.columns = ['_key', 'Vehicle_Age', 'Vehicle_Damage']
dfvehicle.to_csv(dirpath + 'vehicles.csv', index=False)
#dfvehicle.to_json(dirpath + 'vehicles.json')

dfinsure.to_csv(dirpath + 'insure.csv', index=False)
#dfcustomer.to_json(dirpath + 'insure.json')



