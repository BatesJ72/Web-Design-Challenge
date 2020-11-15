import pandas as pd
import os

path = os.path.join("..", "Resources", "cities.csv")
data = pd.read_csv(path)

df = pd.DataFrame(data)

df.to_html("file_data.html")