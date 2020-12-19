
# In[1]:


# 텍스트 정제


# In[2]:


import re


# In[3]:


sentence = 'Sunil tweeted, "Witnessing 70th Republic Day of India from Rajpath,            New Delhi. Mesmerizing performance by Indian Army! Awesome airshow! @ india_official             @indian_army #India #70thRepublic_Day. For more photos ping me sunil@photoing.com :)"'


# In[4]:


# 텍스트에서 숫자, 알파벳 문자, 공백만 남기고 모든 문자를 제거
re.sub(r'([^\s\w]|_)+', ' ', sentence).split()   # \s : 공백을 의미, \w : 숫자+알파벳문자를 의미


# In[ ]:


# n-gram 추출


# In[6]:


def n_gram_extractor(sentence, n):
    tokens = re.sub(r'([^\s\w]|_)+', ' ', sentence).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])


# In[7]:


n_gram_extractor('The cute little boy is playing with the kitten.', 2)  # 2-gram


# In[8]:


n_gram_extractor('The cute little boy is playing with the kitten.', 3)  # 3-gram


# In[10]:


from nltk import ngrams
list(ngrams('The cute little boy is playing with the kitten.'.split(), 3))


# In[13]:


from textblob import TextBlob
blob = TextBlob('The cute little boy is playing with the kitten.')
blob.ngrams(n=3)


# In[ ]:


# 다른 패키지로 Tokenization


# In[14]:


# Keras로 tokenization
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence)


# In[15]:


# TextBlob으로 tokenization
from textblob import TextBlob
blob = TextBlob(sentence)
blob.words


# In[16]:


# 트윗 tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer = TweetTokenizer()
tweet_tokenizer.tokenize(sentence)


# In[23]:


# MWE(Multi-Word Expression) tokenizer
from nltk.tokenize import MWETokenizer
mwe_tokenizer = MWETokenizer()
mwe_tokenizer.add_mwe(('Republic', 'Day'))  # Multi-Word 추가 
mwe_tokenizer.add_mwe(('Indian', 'Army'))   # Multi-Word 추가 => 출력결과에 반영되지 않았음
mwe_tokenizer.tokenize(sentence.split())


# In[24]:


# Indian_Army 를 만들기 위해 작업
mwe_tokenizer.tokenize(sentence.replace('!', '').split()) # 'Army!'의 '!'를 제거 


# In[25]:


# 정규식 tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|\S+')
reg_tokenizer.tokenize(sentence)


# In[26]:


# 공백 tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer = WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence)


# In[28]:


# Word punct tokenizer
from nltk.tokenize import WordPunctTokenizer
wp_tokenizer = WordPunctTokenizer()
wp_tokenizer.tokenize(sentence)


# In[29]:


# 어간 추출


# In[30]:


# RegexpStemmer 사용
from nltk.stem import RegexpStemmer
sentence = "I love playing football"
regex_stemmer = RegexpStemmer('ing$', min=4)
' '.join([regex_stemmer.stem(wd) for wd in sentence.split()])


# In[31]:


# PorterStemmer 사용
from nltk.stem.porter import *
sentence = "Before eating, it would be nice to sanitize your hands with a sanitizer"
ps_stemmer = PorterStemmer()
' '.join([ps_stemmer.stem(wd) for wd in sentence.split()])


# In[36]:


# 표제어 추출


# In[34]:


import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
sentence = "The products produced by the process today are far better than what it produces generally."
' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(sentence)])


# In[37]:


# 단어의 단수화와 복수화


# In[38]:


from textblob import TextBlob
sentence = TextBlob("She sells seashells on the seashore")
sentence.words


# In[39]:


sentence.words[2].singularize()  # 3번째 단어 단수화


# In[40]:


sentence.words[5].pluralize()  # 6번째 단어 복수화


# In[41]:


# 스페인어 -> 영어 번역


# In[43]:


from textblob import TextBlob
en_blob = TextBlob(u'muy bien')
en_blob.translate(from_lang='es', to='en')


# In[44]:


# Feature 추출


# In[45]:


import pandas as pd
df = pd.DataFrame([
    ['The interim budget for 2019 will be announced on 1st February.'],
    ['Do you know how much expectation the middle-class working population is having from this budget?'],
    ['February is the shortest month in a year.'],
    ['This financial year will end on 31st March.']    
])  # DataFrame 생성
df.columns = ['text']
df


# In[46]:


from textblob import TextBlob
df['number_of_words'] = df['text'].apply(lambda x : len(TextBlob(str(x)).words))  # 각 문장의 단어 수 셈
df


# In[47]:


wh_words = set(['why', 'who', 'which', 'what', 'where', 'when', 'how'])
# 각 문장에서 'wh-' 단어 리스트에 속하는 단어가 있는지 확인
df['is_wh_words_present'] = df['text'].apply(lambda x : True if len(set(TextBlob(str(x)).words).intersection(wh_words))>0 else False)
df


# In[48]:


df['language'] = df['text'].apply(lambda x : TextBlob(str(x)).detect_language())
df


# In[49]:


# BoW(단어 모음) 구현


# In[50]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus = [ 'Data Science is an overlap between Arts and Science',
           'Generally, Arts graduates are right-brained and Science graduates are left-brained',
           'Excelling in both Arts and Science at a time becomes difficult', 
           'Natural Language Processing is a part of Data Science'
         ]


# In[51]:


bag_of_words_model = CountVectorizer()
print(bag_of_words_model.fit_transform(corpus).todense())
bag_of_word_df = pd.DataFrame(bag_of_words_model.fit_transform(corpus).todense())
bag_of_word_df.columns = sorted(bag_of_words_model.vocabulary_)
bag_of_word_df.head()


# In[53]:


bag_of_words_model_small = CountVectorizer(max_features=10)
bag_of_word_df_small = pd.DataFrame(bag_of_words_model_small.fit_transform(corpus).todense())
bag_of_word_df_small.columns = sorted(bag_of_words_model_small.vocabulary_)
bag_of_word_df_small.head()


# In[56]:


from pylab import *
import nltk
nltk.download('stopwords')
from sklearn.datasets import fetch_20newsgroups
from nltk import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import re
import string
from collections import Counter


# In[58]:


newsgroups_data_sample = fetch_20newsgroups(subset='train')
stop_words = stopwords.words('english')
stop_words = stop_words + list(string.printable)


# In[59]:


# newsgroups_data_sample['data']로부터 한 문장을 가져와, 해당 문장을 정규화하고 tokenizing한 다음, 각 token에 대해 불용어인지 확인하고 불용어가 아니면 tokenized_corpus에 저장
tokenized_corpus = [word.lower() for sentence in newsgroups_data_sample['data'] for word in word_tokenize(re.sub(r'([^\s\w]|_)+', ' ', sentence)) if word.lower() not in stop_words]


# In[60]:


token_count_di = Counter(tokenized_corpus)# 각 token의 빈도 수 계산
token_count_di.most_common(50) # 빈도 수가 높은 50개의 token 출력


# In[61]:


# TF-IDF 계산


# In[62]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'Data Science is an overlap between Arts and Sceience',
    'Generally, Arts graduates are right-brained and Science graduates are left-brained',
    'Excelling in both Arts and Science at a time becomes difficult',
    'Natural Language Processing is a part of Data Science'
]


# In[63]:


tfidf_model = TfidfVectorizer()
print(tfidf_model.fit_transform(corpus).todense())


# In[65]:


# TF-IDF 행렬을 DataFrame으로 생성
tfidf_df = pd.DataFrame(tfidf_model.fit_transform(corpus).todense())
tfidf_df.columns = sorted(tfidf_model.vocabulary_)
tfidf_df.head()


# In[66]:


# 가장 빈도수가 높은 10개 단어에 대해 TF-IDF 행렬을 DataFrame으로 생성
tfidf_model_small = TfidfVectorizer(max_features=10)
tfidf_df_small = pd.DataFrame(tfidf_model_small.fit_transform(corpus).todense())
tfidf_df_small.columns = sorted(tfidf_model_small.vocabulary_)
tfidf_df_small.head()


# In[67]:


# 코사인 유사도 계산


# In[70]:


from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[71]:


pair1 = ["What you do defines you", "Your deeds define you"]
pair2 = ["Once upon a time there lived a king.", "Who is your queen?"]
pair3 = ["He is desperate", "Is he not desperate?"]


# In[72]:


tfidf_model = TfidfVectorizer()
corpus = [pair1[0], pair1[1], pair2[0], pair2[1], pair3[0], pair3[1]]
tfidf_results = tfidf_model.fit_transform(corpus).todense()


# In[74]:


cosine_similarity(tfidf_results[0], tfidf_results[1]) # 첫번째, 두번째 텍스트 사이의 코사인 유사도 계산


# In[75]:


cosine_similarity(tfidf_results[2], tfidf_results[3]) # 세번째, 네번째 텍스트 사이의 코사인 유사도 계산


# In[76]:


cosine_similarity(tfidf_results[4], tfidf_results[5]) # 다섯번째, 여섯번째 텍스트 사이의 코사인 유사도 계산


# In[77]:


# 텍스트 시각화 방법


# In[96]:


# 단어 구름 이용
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from wordcloud import STOPWORDS
from wordcloud import WordCloud

newsgroups_data_sample = fetch_20newsgroups(subset='train')


# In[97]:


other_stopwords_to_remove = ['\\n', 'n', '\\', '>', 'nLines', 'nI', "n'"]
STOPWORDS = STOPWORDS.union(set(other_stopwords_to_remove))
stopwords = set(STOPWORDS)

text = str(newsgroups_data_sample['data'][:10])
wordcloud = WordCloud(width = 800, height = 800, 
                      background_color = 'white', 
                      max_words=200, 
                      stopwords=stopwords, 
                      min_font_size = 10).generate(text)  # 단어 구름 생성

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


