import csv
with open('input1.csv', mode ='r') as file:
   
  # reading the CSV file and split the ',' 
  data = file.read()
  data = data.split(",")
  
  #Remove the '\n' from the last element in the file 
  for i in range(len(data)):
    if data[i] == 'boy\n':
      data[i] = 'boy'

  #Define the count to find frequency of each word
  def count(elements):
    if elements in dictionary:
        dictionary[elements] += 1
    else:
        dictionary.update({elements: 1})

  #Declare a dictionary
  dictionary = {}
  for elements in data:
    count(elements)
 
  # print the corresponding values.
  for i in dictionary:
    print (i, end = " ")
    print ("-", end = " ")
    print (dictionary[i], end = " ")
    print()
  
