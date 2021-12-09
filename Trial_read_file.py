from PorterStemmer import PorterStemmer

word="Fascinating"
p=PorterStemmer()
output=p.stem(word,0,len(word)-1)
print(output)