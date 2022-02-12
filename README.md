# CSE-163-Final-Project-
There are quite a few libraries need to properly execute our project:
pandas
beautiful soup (bs4)
Scikit-Learn
requests
math
seaborn and matplotlib
eli5

How to run:
Our program is pretty simple, the only python module that actually contains a main
method is ml_analysis.py (Unless you count the test module, in which case there is two)

Running the ml_analysis.py module will use functions from the data_prep.py module to scrap
the data, and will all perform all of the model training, predicting, testing, and interpreting
(Result graphs are stored in graphs folder)

Data:
The vast majority of our data isn't explicitly stored becase we scrape it off of basketball-reference,
however in our data folder there is some that is stored: This was the data we
used as our training and test labels for the machine learning part of the project
That data can therefore be found in the data folder, or if you want to see if for
youself it was retrievd from the "Miscallneaous Stats" section of the basketball reference
web page we linked in our project report