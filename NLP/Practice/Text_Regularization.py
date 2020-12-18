

# In[84]:


sentence = 'The quick brown fox jumps over the lazy dog'


# In[86]:


# 파이썬 기초
'quick' in sentence
sentence.index('fox')
sentence.split().index('lazy')
sentence.split()[2]
sentence.split()[2][::-1] #역순으로 출력

words = sentence.split()
[words[i] for i in range(len(words)) if i%2==0]

revword = [word[::-1] for word in words]
print(' '.join(revword))  # 리스트의 각 값들을 띄어쓰기로 join하여 문장으로 만듦


# In[14]:


import nltk
from nltk import word_tokenize


# In[ ]:


# PoS tagging (품사 태깅)


# In[87]:


words = word_tokenize("I am reading NLP Fundamentals")
print(words)


# In[25]:


nltk.pos_tag(words)  


# In[ ]:


# 불용어 제거 과정
# 불용어 : 문장의 의미에 큰 영향을 미치지 않는 일반적인 단어로, 분석 시 제거한다


# In[26]:


nltk.download('stopwords')
from nltk.corpus import stopwords


# In[27]:


stop_words = stopwords.words('English')
print(stop_words) # 영어에서의 불용어 목록


# In[28]:


sentence = "I am learning Python. It is one of the most popular programming languages"
sentence_words = word_tokenize(sentence)
print(sentence_words)


# In[29]:


# 문장에서 불용어를 제거한 문장 생성
sentence_no_stops = ' '.join([word for word in sentence_words if word not in stop_words])
print(sentence_no_stops)


# In[30]:


# 텍스트 정규화 과정
# 텍스트 정규화 : 변형된 텍스트를 표준 형식으로 변환하는 것 (ex: does = doing = do)


# In[31]:


sentence = "I visited US from UK on 22-10-18"


# In[33]:


normalized_sentence = sentence.replace("US", "United States").replace("UK", "United Kingdom").replace("-18", "-2018")
print(normalized_sentence)


# In[46]:


# 철자 수정
from autocorrect import Speller
spell = Speller()


# In[47]:


spell('Natureal')


# In[48]:


sentence = word_tokenize("Ntural Luanguage Processin deals with the art of extracting insightes from Natural Languaes")
print(sentence)


# In[49]:


sentence_corrected = ' '.join([spell(word) for word in sentence])
print(sentence_corrected)


# In[50]:


# 어간 추출 (ex: production -> product, products -> product)
stemmer = nltk.stem.PorterStemmer()
stemmer.stem("production")


# In[51]:


stemmer.stem("coming")


# In[52]:


stemmer.stem("battling")


# In[53]:


# 표제어 추출 : 어간 추출 과정에서 부적절한 결과를 극복하기 위해, 추가적으로 사전을 통해 단어의 기본 형태를 추출하는 과정
# 시간이 오래 걸림
nltk.download('wordnet')
from nltk.stem.wordnet import WordNetLemmatizer


# In[55]:


lemmatizer = WordNetLemmatizer()
lemmatizer.lemmatize('products')


# In[56]:


lemmatizer.lemmatize('battling')


# In[57]:


# 개체명 취급
nltk.download('maxent_ne_chunker')
nltk.download('words')


# In[58]:


sentence = "We are reading a book published by Packt which is based out of Birmingham."


# In[62]:


i = nltk.ne_chunk(nltk.pos_tag(word_tokenize(sentence)), binary=True)
[a for a in i if len(a)==1]


# In[63]:


# 단어 중의성 해결
from nltk.wsd import lesk


# In[64]:


sentence1 = "Keep your savings in the bank"
sentence2 = "It's so risky to drive over the banks of the road"


# In[65]:


print(lesk(word_tokenize(sentence1), 'bank'))


# In[66]:


print(lesk(word_tokenize(sentence2), 'bank'))


# In[67]:


# 문장 경계 인식
from nltk.tokenize import sent_tokenize


# In[71]:


sent_tokenize("N.L.P is interesting. Isn't it?")


# In[72]:


# 실습1: 원시 텍스트 전처리
text_corpus = "In this book authored by Sohom Ghosh and Dwight Gunning, we shall learnning how to pracess Natueral Language and extract insights from it. The first four chapter will introduce you to the basics of NLP. Later chapters will describe how to deal with complex NLP prajects. If you want to get early access of it, you should book your order now."


# In[89]:


tokens = word_tokenize(text_corpus)
#print([tokens[i] for i in range(20)])
print(tokens)


# In[90]:


sentence_corrected = ' '.join([spell(token) for token in tokens])
print(sentence_corrected)
tokens_corrected = word_tokenize(sentence_corrected)
print([tokens_corrected[i] for i in range(20)])


# In[91]:


print([nltk.pos_tag(token) for token in tokens_corrected])


# In[93]:


stop_words = stopwords.words('English')
tokens_no_stopwords = [token for token in tokens_corrected if token not in stop_words]
print([tokens_no_stopwords[i] for i in range(20)])


# In[98]:


stemmer = nltk.stem.PorterStemmer()
stemmer.stem("production")
print([stemmer.stem(tokens_no_stopwords[i]) for i in range(20)])


# In[102]:


sentence_list = sent_tokenize(text_corpus)
print(sentence_list)
print(len(sentence_list))



