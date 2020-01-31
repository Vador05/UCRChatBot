
Based on https://data-flair.training/blogs/python-chatbot-project/

##Installation Process:

 git clone https://github.com/Vador05/UCRChatBot
 pip3 install --upgrade tensorflow
 pip3 install keras
 pip3 install nltk
 sudo apt-get install python3-tk 

  From a Python 3 terminal
  >>> import nltk
  >>> nltk.download('punkt')
  >>> nltk.download('wordnet')

##Preparation
5 steps to create a chatbot in Python from scratch:

    1-Import and load the data file
	All the Q&A are stored in the JSON file
    2-Preprocess data
	The questions and answers will be splitted by words using the nltk tokenize function
    3-Create training and testing data
	The input id the pattern and the desired result is in which class the input pattern belongs to
    4-Build the model
	Using a neural network of 3 layers (128, 64, )neurons and after 200 epochs* store the trained data.
	*one epoch = one forward pass and one backward pass of all the training examples
    5-Predict the response
	Use the generated model to classify the answerclass and get one of the answers from the pool.
