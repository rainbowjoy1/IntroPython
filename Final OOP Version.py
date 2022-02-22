
class Document:
    def __init__(self, filename, string):
        self.filename=filename
        self.string=string
        Document.convert(string)

    def comparison(self,comp_file):
        
        
      for x in comp_file (make sure this is the dictionary):
        use dictionary keys to search and find matches
        #compare self to other--for loop not here
        #should only compare one file and use the for loop from the main code and not in the document object
      in a for loop compare the compfile with each file in the corpus list
        compfile should have two vectors. One of all ones for each word and one of all the frequencies
        compare the words and create a 2 vectors with a 1 or 0 if it matches. record the frecquency in the second list
      Divide the frequency matching vectors (if greater than one return 1). Dot product the word vector with the new frequency vector. 
      Dot product the final vector and the comp_file word vector

    def clean(self, text):
        text.lower()
        text.translate(str.maketrans('', '','!"#$%&()*+,-\'./:;<=>?@[\]^_`{|}~'))
        return self

    def convert(self, text):
        dictionary{}
        for word in text:
          ## remove the punctuation here and lower case here to save on memory ###todd thinks we should keep apostrophes
            if word not in dictionary:
                dictionary[word] = 0 
            dictionary[word] += 1
            return dictionary


for all files create new Document:
    add document to list
    
for all documents in list do:
    compare document1 to document2
    
    


File1=Files("Strings are sequences of letters and numbers, or in other words, chunks of text. They are surrounded by two quotes for protection: for example in Lesson 0 the part \"Hello, World!\" of the first program was a string. If a pound sign # appears in a string, then it does not get treated as a comment:")
