# -*- coding: utf-8 -*-
import pandas as pd

# Cambiar para que acepte ruta relativa
dirpath = '\\Users\Lizeth_Blanco\Documents\Maestría\BasesdeDatos\Proyecto\data'

dforigin = pd.read_csv(dirpath + 'train.csv')

dfcustomer = dforigin[['id', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']]
dfvehicle = dforigin[['id', 'Vehicle_Age', 'Vehicle_Damage']]

dfinsure = dforigin[['Annual_Premium', 'Policy_Sales_Channel', 'Response']]
dfinsure['_from'] = 'customers/' + dfcustomer['id'].astype(str)
dfinsure['_to'] = 'vehicles/' + dfvehicle['id'].astype(str)

dfcustomer.columns = ['_key', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']
dfcustomer.to_csv(dirpath + 'customers.csv')

dfvehicle.columns = ['_key', 'Vehicle_Age', 'Vehicle_Damage']
dfvehicle.to_csv(dirpath + 'vehicles.csv')

dfinsure.to_csv(dirpath + 'insure.csv')

