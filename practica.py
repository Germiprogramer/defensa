def bitcoinToEuros(bitcoin_amount, bitcoin_value_euros):
    euros_value = bitcoin_amount * bitcoin_value_euros
    return euros_value

#quiero calcular el valor de tu Bitcoin en euros y realizar la correlación con los datos del csv air_traffic_data.csv


#4. Cálculo de la correlación entre el valor del Bitcoin y el número de pasajeros
#5. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos
#6. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales
#7. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos nacionales
#8. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales y nacionales
#9. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales y nacionales por aeropuerto


import dask.dataframe as dd
import dask.bag as db
import os
#lee el csv
df=dd.read_csv(os.path.join('air_traffic_data.csv')).compute()
#elimina los duplicados
def val_unicos(dato):
  a = df[dato].unique()
  print(dato, df[dato].unique())
  return a
ba =val_unicos('Boarding Area')
pcc = val_unicos('Price Category Code')
atc =val_unicos('Activity Type Code')
t = val_unicos('Terminal')
gs = val_unicos('GEO Summary')
aatc = val_unicos('Adjusted Activity Type Code')
m = val_unicos('Month')

#hago que las columnas sean de tipo numerico
def cambio(a, b, c, d, e, dato):
    if dato != 'Month':
        for i in range(len(df)):
            if df [dato][i] == a:
                df[dato][i] = 0	
            elif df [dato][i] == b:
                df[dato][i] = 1
            elif df [dato][i] == c:
                df[dato][i] = 2
            elif df [dato][i] == d:
                df[dato][i] = 3
            elif df [dato][i] == e:
                df[dato][i] = 4
    else:
        for i in range(len(df)):
                if df[dato][i]=='January':
                    df[dato][i]=1
                elif df[dato][i]=='February':
                    df[dato][i]=2
                elif df[dato][i]=='March':
                    df[dato][i]=3
                elif df[dato][i]=='April':
                    df[dato][i]=4
                elif df[dato][i]=='May':
                    df[dato][i]=5
                elif df[dato][i]=='June':
                    df[dato][i]=6
                elif df[dato][i]=='July':
                    df[dato][i]=7
                elif df[dato][i]=='August':
                    df[dato][i]=8
                elif df[dato][i]=='September':
                    df[dato][i]=9
                elif df[dato][i]=='October':
                    df[dato][i]=10
                elif df[dato][i]=='November':
                    df[dato][i]=11
                elif df[dato][i]=='December':
                    df[dato][i]=12
    df[dato]=df[dato].astype(int)
    cambio(pcc[0], pcc[1], None, None, None, 'Price Category Code')   
    cambio(gs[0], gs[1], None, None, None, 'GEO Summary')
    cambio(aatc[0], aatc[1], aatc[2], None, None, 'Adjusted Activity Type Code')
    cambio(t[0], t[1], t[2], t[3], t[4], 'Terminal')
    cambio(None, None, None, None, None, 'Terminal')  
#calcula la media de todas las columnas
df.mean()
#calcula la desviacion estandar de todas las columnas
df.std()
#ahora calculamos la correlacion entre el valor del Bitcoin y el número de pasajeros
df['bitcoin_value_euros']=bitcoinToEuros(df['bitcoin_value'],df['bitcoin_value_euros'])
df['bitcoin_value_euros'].corr(df['passenger_count'])
#ahora calculamos la correlacion entre el valor del Bitcoin y el número de vuelos
df['bitcoin_value_euros'].corr(df['flight_count'])
#ahora calculamos la correlacion entre el valor del Bitcoin y el número de vuelos internacionales
df['bitcoin_value_euros'].corr(df['international_flight_count'])
#ahora calculamos la correlacion entre el valor del Bitcoin y el número de vuelos nacionales
df['bitcoin_value_euros'].corr(df['domestic_flight_count'])
