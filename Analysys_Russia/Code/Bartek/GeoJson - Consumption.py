from Analysys_Russia.Code.Bartek.Main import consumptuon_data, geojson, pd, np, sns, plt,gpd

temp_data = consumptuon_data.copy()

temp_data = temp_data.loc[temp_data['Year'] == 2022]


temp_data = temp_data[['Region','Total alcohol consumption (in liters of pure alcohol per capita)']]

print(geojson.columns)

### i gave up. Names of regions is in Russian :////
