from difflib import get_close_matches
import json

a=['ABCD','dsd','aB']
print(get_close_matches('abcd',a,cutoff=0.8))
data=json.load(open('data.json'))
print(data[''])


