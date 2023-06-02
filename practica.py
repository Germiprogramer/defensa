#4. Cálculo de la correlación entre el valor del Bitcoin y el número de pasajeros
#5. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos
#6. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales
#7. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos nacionales
#8. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales y nacionales
#9. Cálculo de la correlación entre el valor del Bitcoin y el número de vuelos internacionales y nacionales por aeropuerto

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
