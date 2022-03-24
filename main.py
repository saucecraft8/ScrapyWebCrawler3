import pandas as pd
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

data = pd.read_json('TestSpider/items.json')
dataFrame = pd.DataFrame(data)

parse = word_tokenize(dataFrame.iat[0,0][0][1:-1])

print(parse)
