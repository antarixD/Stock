#https://medium.com/machine-learning-101/chapter-2-svm-support-vector-machine-coding-edd8f1cf8f2d

import os
import numpy as np
from collections import Counter
from sklearn import svm
from sklearn.metrics import accuracy_score


train_loc = '/home/antarix/Desktop/naive bayes/test-mails (copy)'
#train_loc = '/home/antarix/Desktop/naive bayes/test-mails'
test_loc = '/home/antarix/Desktop/naive bayes/train-mails'

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
#below is the training model of the email
features_matrix, labels = extract_features(train_loc)
# below is the testing model of the email
test_feature_matrix, test_labels = extract_features(test_loc)


'''
model = svm.SVC()

print ("Training model.")
#train model
model.fit(features_matrix, labels)
predicted_labels = model.predict(test_feature_matrix)
print ("FINISHED classifying. accuracy score : ")
print ('accuracy_score : ', accuracy_score(test_labels, predicted_labels))


comparison = test_labels == predicted_labels
equal_arrays = comparison.all()
print(comparison)
print(equal_arrays)
'''

#This is very basic implementation. It assumes
# default values of tuning parameters (kernel = linear, C = 1 and gamma = 1)


# decrease the training time
#---------------------------
# One way to decrease the training time is by reducing the training set
# the below snop of the code used 10 percent of the training set

'''
ten_features_matrix = features_matrix[:int(len(features_matrix)/10)]
ten_labels = labels[:int(len(labels)/10)]

model.fit(ten_features_matrix, ten_labels)
predicted_labels = model.predict(test_feature_matrix)
print ("FINISHED classifying. accuracy score : ")
#percent score is 51.28
print ('accuracy_score 10 percent: ', accuracy_score(test_labels, predicted_labels))
'''

#lets tune parameters to get better accuracy score
#lets chnage kernal to rbf
model = svm.SVC(kernel="rbf", C = 100000000, gamma = 0.000000000001)

model.fit(features_matrix, labels)
predicted_labels = model.predict(test_feature_matrix)

ten_features_matrix = features_matrix[:int(len(features_matrix)/10)]
ten_labels = labels[:int(len(labels)/10)]

model.fit(ten_features_matrix, ten_labels)
predicted_labels = model.predict(test_feature_matrix)
print ("FINISHED classifying. accuracy score : ")
#percent score is 51.28
print ('accuracy_score 10 percent: ', accuracy_score(test_labels, predicted_labels))