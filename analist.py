import numpy as np
import pandas as pd

precios = pd.DataFrame({"Azul": [8, 7.8, 8.9, 7, 9, 7.8, 9.5, 8.8, 8.2],
                        "Naranja": [10.55, 11, 11.85, 9.5, 10.5, 11.5, 11.4, 11.56, 12]
                        })

# todo menos el primero
print(precios.iloc[1:])
