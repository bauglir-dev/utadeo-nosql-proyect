# -*- coding: utf-8 -*-
import pandas as pd

# Cambiar para que acepte ruta relativa
dirpath = 'E:\\utadeo\\utadeo-nosql-proyect\\data\\'
#dirpath = ''
#dirpath = '\\Users\Lizeth_Blanco\Documents\Maestría\BasesdeDatos\Proyecto\data'

dforigin = pd.read_csv(dirpath + 'train.csv')

#dfcustomer_sd = dfcustomer.drop_duplicates(['Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License'])
#dfvehicle_sd = dfvehicle.drop_duplicates(['Vehicle_Age', 'Vehicle_Damage'])

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


dforigin_final = dfcustomer_1
dforigin_final = dforigin_final.append(dfcustomer_2)
dforigin_final = dforigin_final.append(dfcustomer_3)
dforigin_final = dforigin_final.append(dfcustomer_4)
dforigin_final = dforigin_final.append(dfcustomer_5)
dforigin_final = dforigin_final.append(dfcustomer_6)

dfcustomer = dforigin_final[['id', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']]
dfvehicle = dforigin_final[['vehicle_id', 'Vehicle_Age', 'Vehicle_Damage']]

dfinsure = dforigin[['Annual_Premium', 'Policy_Sales_Channel', 'Response']]
dfinsure['_from'] = 'customers/' + dfcustomer['id'].astype(str)
dfinsure['_to'] = 'vehicles/' + dfvehicle['vehicle_id'].astype(str)

dforigin_final.to_csv(dirpath + 'dforigin_final.csv', index=False)

#dfcustomer_sd = dfcustomer.drop_duplicates(['Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License'])
dfvehicle_sd = dfvehicle.drop_duplicates(['Vehicle_Age', 'Vehicle_Damage'])

dfinsure = dforigin_final[['Annual_Premium', 'Policy_Sales_Channel', 'Response']]
dfinsure['_from'] = 'customers/' + dfcustomer['id'].astype(str)
dfinsure['_to'] = 'vehicles/' + dfvehicle['vehicle_id'].astype(str)

dfcustomer.columns = ['_key', 'Gender', 'Age', 'Region_Code', 'Vintage', 'Driving_License']
dfcustomer.to_csv(dirpath + 'customers.csv', index=False)
#dfcustomer.to_json(dirpath + 'customers.json')

dfvehicle_sd.columns = ['_key', 'Vehicle_Age', 'Vehicle_Damage']
dfvehicle_sd.to_csv(dirpath + 'vehicles.csv', index=False)
#dfvehicle.to_json(dirpath + 'vehicles.json')

dfinsure.to_csv(dirpath + 'insure.csv', index=False)
#dfcustomer.to_json(dirpath + 'insure.json')