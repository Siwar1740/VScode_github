import streamlit as st 
import nltk
import string
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
with open(r"C:\Users\hp\Downloads\text.txt", "r", encoding="utf8") as file:
    data = file.read().replace("\n", " ")

sentencies = sent_tokenize(data)


def preprocess(sentence):
    word = word_tokenize(sentence)
    stopword = set(stopwords.words("english"))
    word = [i for i in word if i not in stopword and i not in string.punctuation]
    limitizer = WordNetLemmatizer()
    word = [limitizer.lemmatize(i) for i in word]
    return word


lst = [preprocess(i) for i in sentencies]


def get_most_relevent_sentence(query):
    query_list = preprocess(query)
    maxsimilarity = 0

    releventsentece = ""

    for i in lst:
        intersection = set(query_list).intersection(set(i))
        union = set(query_list).union(set(i))
        similarity = len(intersection) / len(union)
        if similarity > maxsimilarity:
            maxsimilarity = similarity
            releventsentece = " ".join(i)
    return releventsentece
def chatbot (question) : 
    response = get_most_relevent_sentence (question) 
    return response 
def main(): 
    st.title("chatbot") 
    query = st.text_input("you") 
    if st.button("submit") :
        response = chatbot(query) 
        st.success(response) 
if __name__=="__main__":
    main()  

