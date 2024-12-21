import numpy as np 
from utils.load_housing_data import load_housing_data

# cargar la data
housing = load_housing_data()

# Definir el tamaño del conjunto de prueba y la semilla
test_ratio = 0.2         # 20% de los datos para test
random_state_value = 42   # Semilla arbitraria para reproducibilidad


def split_train_test(data, test_ratio, random_state=None):

    if random_state is not None:
        np.random.seed(random_state)


    # Creates random permutation of indices
    shuffled_indices = np.random.permutation(len(data))
    
    # Calculates size of test set
    test_set_size = int(len(data) * test_ratio)
    
    # Splits indices into test and train sets
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    
    # Returns split datasets using iloc for indexing
    return data.iloc[train_indices], data.iloc[test_indices]

 # Dividir la data en entrenamiento y test
train_set, test_set = split_train_test(housing, 0.2,  random_state=random_state_value)



# Check the sizes
print(f"Total data size: {len(housing)}")
print(f"Training set size: {len(train_set)}")  # Should be ~80% of data
print(f"Test set size: {len(test_set)}")      # Should be ~20% of data

