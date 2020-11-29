# -*- coding: utf-8 -*-
import pandas as pd

# Cambiar para que acepte ruta relativa
dirpath = 'E:\\utadeo\\utadeo-nosql-proyect\\data\\'
#dirpath = '\\Users\Lizeth_Blanco\Documents\Maestría\BasesdeDatos\Proyecto\data'

dforigin = pd.read_csv(dirpath + 'train.csv')

dfcustomer = dforigin[['id', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']]
dfvehicle = dforigin[['id', 'Vehicle_Age', 'Vehicle_Damage']]

dfcustomer_sd = dfcustomer.drop_duplicates(['Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License'])
dfvehicle_sd = dfvehicle.drop_duplicates(['Vehicle_Age', 'Vehicle_Damage'])

dfinsure = dforigin[['Annual_Premium', 'Policy_Sales_Channel', 'Response']]
dfinsure['_from'] = 'customers/' + dfcustomer['id'].astype(str)
dfinsure['_to'] = 'vehicles/' + dfvehicle['id'].astype(str)

dfcustomer_1 = dforigin[dforigin['Vehicle_Age'].str.match('> 2 Years') 
                        & dforigin['Vehicle_Damage'].str.match('Yes')]
dfcustomer_1['vehicle_id'] = 1

dfcustomer_2 = dforigin[dforigin['Vehicle_Age'].str.match('1-2 Year') 
                        & dforigin['Vehicle_Damage'].str.match('No')]
dfcustomer_2['vehicle_id'] = 2

dfcustomer_3 = dforigin[dforigin['Vehicle_Age'].str.match('< 1 Year') 
                        & dforigin['Vehicle_Damage'].str.match('No')]
dfcustomer_3['vehicle_id'] = 3

dfcustomer_4 = dforigin[dforigin['Vehicle_Age'].str.match('< 1 Year') 
                        & dforigin['Vehicle_Damage'].str.match('Yes')]
dfcustomer_4['vehicle_id'] = 4

dfcustomer_5 = dforigin[dforigin['Vehicle_Age'].str.match('1-2 Year') 
                        & dforigin['Vehicle_Damage'].str.match('Yes')]
dfcustomer_5['vehicle_id'] = 5

dfcustomer_6 = dforigin[dforigin['Vehicle_Age'].str.match('> 2 Years') 
                        & dforigin['Vehicle_Damage'].str.match('No')]
dfcustomer_6['vehicle_id'] = 6

dfcustomer_final = dfcustomer_1
dfcustomer_final = dfcustomer_final.append(dfcustomer_2)
dfcustomer_final = dfcustomer_final.append(dfcustomer_3)
dfcustomer_final = dfcustomer_final.append(dfcustomer_4)
dfcustomer_final = dfcustomer_final.append(dfcustomer_5)
dfcustomer_final = dfcustomer_final.append(dfcustomer_6)

dfcustomer_final.to_csv(dirpath + 'dfcusotmer_final.csv', index=False)


"""
dfcustomer.columns = ['_key', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']
dfcustomer.to_csv(dirpath + 'customers.csv', index=False)
#dfcustomer.to_json(dirpath + 'customers.json')

dfvehicle.columns = ['_key', 'Vehicle_Age', 'Vehicle_Damage']
dfvehicle.to_csv(dirpath + 'vehicles.csv', index=False)
#dfvehicle.to_json(dirpath + 'vehicles.json')

dfinsure.to_csv(dirpath + 'insure.csv', index=False)
#dfcustomer.to_json(dirpath + 'insure.json')

"""