
from sklearn.datasets import load_boston
from sklearn.linear_model import *
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import numpy as np  #pacchetto che permette di fare calcoli vettoriali e algebrici
#np.random.seed(2)   #questo comando forza numpy ad usare sempre lo stesso nucleo per creare numeri casuali


dataset = load_boston()         #carico un set di dati di abitazioni in 'dataset'

# print(dataset['DESCR'])       #visualizzo le feature
# print(dataset['data'][0])     #visualizzo i valori delle feature del primo lotto di terra
# print(dataset['target'][0])   #visualizzo il prezzo del primo lotto di terra (24.0 sono 24000$)

input_data = dataset['data']         #i solo i dati delle feature, ovvero dei dati delle abitazioni
value_expected = dataset['target']   #dalle predizioni, target


input_data_for_train, input_data_for_test, value_expected_for_train, value_expected_for_test = train_test_split(input_data, value_expected, test_size=0.25)

linear_model = LinearRegression()              #creo il modello lineare da addestrare
passive_aggro_model = RandomForestRegressor()    #creo il modello da confrontare

linear_model.fit(input_data_for_train, value_expected_for_train)   #addestro il modello lineare
passive_aggro_model.fit(input_data_for_train, value_expected_for_train)


value_predicted_on_linear_test = linear_model.predict(input_data_for_test)
value_predicted_on_linear_train = linear_model.predict(input_data_for_train)

value_predicted_on_passive_aggressive_test = passive_aggro_model.predict(input_data_for_test)
value_predicted_on_passive_aggressive_train = passive_aggro_model.predict(input_data_for_train)


print('--- MODELLO LINEARE ---\n\r')
error_committed_on_linear_train = mean_absolute_error(value_expected_for_train, value_predicted_on_linear_train)
print('ERRORE NELLA PREDIZIONE DEI DATI DI TRAIN CON MODELLO LINEARE', error_committed_on_linear_train)
error_committed_on_linear_test = mean_absolute_error(value_expected_for_test, value_predicted_on_linear_test)
print('ERRORE NELLA PREDIZIONE DEI DATI DI TEST CON MODELLO LINEARE', error_committed_on_linear_test)

print('DIFFERENZA', error_committed_on_linear_train-error_committed_on_linear_test)

print('--- MODELLO PASSIVO AGGRESSIVO ---\n\r')
error_committed_on_passive_aggressive_train = mean_absolute_error(value_expected_for_train, value_predicted_on_passive_aggressive_train)
print('ERRORE NELLA PREDIZIONE DEI DATI DI TRAIN CON MODELLO IN COMPETIZIONE', error_committed_on_passive_aggressive_train)
error_committed_on_passive_aggressive_test = mean_absolute_error(value_expected_for_test, value_predicted_on_passive_aggressive_test)
print('ERRORE NELLA PREDIZIONE DEI DATI DI TEST CON MODELLO IN COMPETIZIONE', error_committed_on_passive_aggressive_test)

print('DIFFERENZA', error_committed_on_linear_train-error_committed_on_passive_aggressive_test)

print('--- MODELLI A CONFRONTO ---\n\r')
print('DIFFERENZA', error_committed_on_linear_test-error_committed_on_passive_aggressive_test)
