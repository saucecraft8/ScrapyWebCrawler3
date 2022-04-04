import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
data = pd.read_json('TestSpider/items.json')
dataFrame = pd.DataFrame(data)

parse_string = dataFrame.iat[0,0][1][1:-1]
parse_string = lemmatizer.lemmatize(parse_string)

parse_tokenize = word_tokenize(parse_string)

while ',' in parse_tokenize:
  parse_tokenize.remove(',')
while '.' in parse_tokenize:
  parse_tokenize.remove('.')

print(parse_tokenize)
print(nltk.pos_tag(parse_tokenize))
