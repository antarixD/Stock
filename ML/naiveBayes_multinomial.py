#https://medium.com/machine-learning-101/chapter-1-supervised-learning-and-naive-bayes-classification-part-2-coding-5966f25f1475


import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


train_loc = '/home/antarix/Desktop/naive bayes/test-mails (copy)'
#train_loc = '/home/antarix/Desktop/naive bayes/test-mails'
test_loc = '/home/antarix/Desktop/naive bayes/train-mails'

#step 1: data cleaning: removing of unwanted words from the corpus
#step 2: count od words into key value

#-----------------------------------Step : 1-------------------------------------#
#input list of emails
#return is dictionary with first 3000 commanly used words in all the mails

def make_Dictionary(root_dir):
   all_words = []
   emails = [os.path.join(root_dir,file) for file in os.listdir(root_dir)]
   for mail in emails:
        with open(mail) as m:
            for line in m:
                words = line.split()
                all_words += words

   #the below dictionary has the (work: count) key value pair in the training set emails
   dictionary = Counter(all_words)
   #creating the list of the keys from the directory. To remove unwanted words
   list_to_remove = list(dictionary)

   #using the list to delete the keys from the directory
   for item in list_to_remove:
       # remove if numerical.
       if item.isalpha() == False:
           del dictionary[item]
       # deletion of characters with lenght = 1
       elif len(item) == 1:
           del dictionary[item]

    # consider only most 3000 common words in dictionary.
   dictionary = dictionary.most_common(3000)
   return dictionary

#-----------------------------------Step : 2-------------------------------------#
#input list of emails
#return is dictionary with first 3000 commanly used words in all the mails
def extract_features(mail_dir):
  files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]

  #creating the metrix of 3000 items. And all items are Zero '0'.
  #NOTE: 1 for each word in dictionary
  features_matrix = np.zeros((len(files),3000))

  #creating the metrix with iteams equal to number of files in the input directory(training and test directory)
  train_labels = np.zeros(len(files))

  count = 0;
  docID = 0;
  for file in files:

    with open(file) as fi:
      for i,line in enumerate(fi):
        #if line number is 3 i.e. index = 2 in file
        if i == 2:
          words = line.split()
          for word in words:
              wordID = 0
              for i,d in enumerate(out_dir):
                  if d[0] == word:
                      wordID = i
                      features_matrix[docID,wordID] = words.count(word)

      train_labels[docID] = 0;
      #spliting the file name to get the last token after '/', i.e. get file name
      #ex : /home/antarix/Desktop/naive bayes/test-mails/5-1339msg1.txt to get '5-1339msg1.txt'
      filepathTokens = file.split('/')

      lastToken = filepathTokens[len(filepathTokens) - 1]
      if lastToken.startswith("spmsg"):
          train_labels[docID] = 1;

          count = count + 1
      docID = docID + 1

  return features_matrix, train_labels




#______________________________Main________________________________________#
out_dir = make_Dictionary(train_loc)



print ("reading and processing emails from file.")
features_matrix, labels = extract_features(train_loc)
test_feature_matrix, test_labels = extract_features(test_loc)


#print('test_labels: ', test_labels)
# print(features_matrix, labels)
# print("test_feature_matrix, test_labels: ", test_feature_matrix, test_labels)


model = MultinomialNB()

print ("Training model.")
#train model
model.fit(features_matrix, labels)

predicted_labels = model.predict(test_feature_matrix)

print('predicted_labels')
print(predicted_labels)

print ("FINISHED classifying. accuracy score : ")
print (accuracy_score(test_labels, predicted_labels))

comparison = test_labels == predicted_labels
equal_arrays = comparison.all()
print(comparison)
print(equal_arrays)