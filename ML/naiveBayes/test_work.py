l1 = ["eat","sleep","repeat","sleep","repeat","repeat"]
# obj1 = enumerate(l1)
# print (list(obj1))

count = 0
for words in l1:
    obj1 = enumerate(l1)

    for i, d in enumerate(l1):
        print("i: ", i)
        print("d: ", d)
        if d[0] == words:
            wordID = i
            print(wordID)

            # features_matrix[docID, wordID] = words.count(word)