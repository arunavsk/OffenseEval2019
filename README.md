# Identifying and Categorizing Offensive Language on Twitter

Offensive language, hate speech and cyberbullying have become increasing more pervasive in social media. Individuals frequently take advantage of the perceived anonymity on social media platforms, to engage in brash and disrespectful  behaviour  that  many  of  them  would not  consider  in  real  life. The  goal  of  this project  is  to  use  a  hierarchical  model  to  not only  identify  tweets/messages  with  offensive language but categorize the type and the target of offensive messages on social media.

# How To
- Create virutal env and install dependencies
```python
conda create -n [ENV] python=3.7
conda activate [ENV]
pip install -r requirements.txt
wget http://nlp.stanford.edu/data/glove.twitter.27B.zip
```

- Visit the following notebooks
	- [EDA](/notebooks/EDA.ipynb) : Exploratory analysis and visualizations
	- [Preprocessing](/notebooks/Preprocessing.ipynb): Data Cleaning, Feature Engineering and more
	- [NBSVM](/notebooks/NBSVM.ipynb): NBSVM classifier for all 3 sub-tasks
	- [LSTM](/notebooks/LSTM.ipynb): LSTM classifier for all 3 sub-tasks
	- [CNN Text (Simplified)](/notebooks/CNNv1.ipynb): Simplified version of CNN Text proposed by Kim with one single input channel
	- [CNN Text (OG)](/notebooks/CNNv2.ipynb): Original architecture of CNN Text by Kim with multichannel inputs

- Full report for implementation details, results, conclusion [here](/documents/Report.pdf)

# FAQ
Please reach out to arsaikia@iu.edu for feedback and suggestions

