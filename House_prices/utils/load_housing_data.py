import pandas as pd
import os

def load_housing_data(housing_path="utils/datasets/housing"):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)  

# Cargamos los datos
housing = load_housing_data()


 # Información de las columnas
# print(housing.info())

# Mostrar las filas
# print(housing.head())


# Analizar categorías de ocean_proximity
# print("\nCategorías de ocean_proximity:")
# print(housing["ocean_proximity"].value_counts())

# Descripción de los datos
print(housing.describe())