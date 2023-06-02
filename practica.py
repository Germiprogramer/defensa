#4. Cálculo de la correlación entre el valor del Bitcoin y el número de pasajeros
#5. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos
#6. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales
#7. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos nacionales
#8. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales y nacionales
#9. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales y nacionales por aeropuerto

#ahora calculamos la correlacion entre el valor del Bitcoin y el número de pasajeros
df['bitcoin_value_euros']=bitcoinToEuros(df['bitcoin_value'],df['bitcoin_value_euros'])
df['bitcoin_value_euros'].corr(df['passenger_count'])
#ahora calculamos la correlacion entre el valor del Bitcoin y el número de vuelos
df['bitcoin_value_euros'].corr(df['flight_count'])
#ahora calculamos la correlacion entre el valor del Bitcoin y el número de vuelos internacionales
df['bitcoin_value_euros'].corr(df['international_flight_count'])
#ahora calculamos la correlacion entre el valor del Bitcoin y el número de vuelos nacionales
df['bitcoin_value_euros'].corr(df['domestic_flight_count'])

#agregamos una columna con el bitcoin_value_euros por aeropuerto
df['bitcoin_value_euros_aeropuerto']=df['bitcoin_value_euros']/df['airport_id']


# calcula la matriz de correlacion de todas las columnas
df.corr()

