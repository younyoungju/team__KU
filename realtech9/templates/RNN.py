#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !pip install gensim --user


# In[1]:


#전처리
import re
import pickle
from string import punctuation
from jamo import h2j, j2hcj, j2h
from soynlp.hangle import levenshtein, jamo_levenshtein
from PreProcessing.find_common_part import find_common_part
from PreProcessing.Dictionary import sd, ad, kopro
from PreProcessing.Opentext import get_EBS, get_EBS_entered, get_STT1_Google_entered, get_STT1_Google, get_STT1_Transcribe_entered


# In[3]:


#젠심
from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile


# In[4]:


#LSTM
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, SimpleRNN
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical


# In[5]:


#토크나이저, 형태소분석기
import nltk
from nltk import Text
from nltk.tag import pos_tag
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize, word_tokenize, TweetTokenizer, regexp_tokenize
from nltk.help import upenn_tagset
from konlpy.corpus import kolaw, kobill
from konlpy.tag import Kkma, Mecab, Okt, Komoran, Hannanum
from collections import defaultdict


# In[6]:


EBS = get_EBS(1, 26)


# In[7]:


GOOGLE = get_STT1_Google(1, 26)


# In[10]:


GOOGLE[2500:3000]


# In[11]:


GOOGLE[2500:3000]
# GOOGLE


# In[12]:


##전처리 전체코드

def decimalnumber_to_korean(m):
    answer = ''
    for _ in m.group(1):
        answer += kopro[int(_)]
    answer += '점'
    for _ in m.group(3):
        answer += kopro[int(_)]
    return answer

def number_to_korean(s):
    #소수점 한국어로
    s = re.sub(r'(\d+)(\.)(\d+)', decimalnumber_to_korean, s)
    
    #정수 한국어로
    fl = re.findall(r'\d+', s)
    fl = set(fl)
    fl = [int(_) for _ in fl]
    fl.sort(reverse=True)
    fl = [str(_) for _ in fl]
    for n in fl:
        s = s.replace(n, kopro[int(n)])
    return s

def mathsymbol_to_korean(s):
    for ms in sd.keys():
        if ms in s:
            s = s.replace(ms, sd[ms])
    return s

def alphabet_to_korean(s):
    for a in ad.keys():
        if a in s:
            s = s.replace(a, ad[a])
    return s

def remove_newlines(s):
    
    return re.sub(r'[\n]+', ' ', s)

def remove_puncuations(s):
    
    return re.sub(r'[\.?,‘’]+', ' ', s)

def insert_dot(text, dot):
    pattern1 = re.compile(r'\S(ㄷㅏ)$')   #다
#     pattern2 = re.compile(r'(.ㅔ|ㅏ|ㅓ|ㅐ|ㅗ|ㅜ)(ㅇㅛ)$') # ㅔ요, ㅏ요, ㅓ요
#     pattern3 = re.compile(r'(ㅆ)(ㅈ|ㅊ)(ㅛ)$') 
#     pattern4 = re.compile(r'(ㅂ|ㅣ)(ㄴㅣㄲㅏ)$')  #ㅂ니까
#     pattern5 = re.compile(r'(ㄴㄷㅔ)$')
    text_list = []
    _1 = 0
    _2 = 0
    _3 = 0
    _4 = 0
    _5 = 0
    _6 = 0
    for _ in text.split(' '):         
        new_ = j2hcj(h2j(_))
        if pattern1.findall(new_):
            text_list.append(_.replace(_, _+dot))
            _1 += 1
#         elif pattern2.findall(new_):
#             text_list.append(_.replace(_, _+dot))
#             _2 += 1
#             list2.append(_)
#         elif pattern3.findall(new_):
#             text_list.append(_.replace(_, _+dot))
#             _3 += 1
#             list3.append(_)
#         elif pattern4.findall(new_):
#             text_list.append(_.replace(_, _+dot))
#             _4 += 1
#         elif pattern5.findall(new_):
#             text_list.append(_.replace(_,_+dot))
#             _5 += 1
        else:
            text_list.append(_)
            _6 += 1
#     print('pattern1 = {}, pattern2= {}, pattern3 = {}, pattern5 = {}, pattern6 = {}'.format(_1,_2,_3,_4,_5,_6)) 
    #print('pattern2 = ',list2)#'\n','list5 = ',list5)
    return text_list    

# EBS 전처리
def EBS_preprocessing(EBS):
    
#     수학기호 한국어로 변환(EBS)
    ebs_math_conversion = mathsymbol_to_korean(EBS)
        
#     숫자 한국어로 변환(EBS)
    ebs_number_conversion = number_to_korean(ebs_math_conversion)
        
#     알파벳 한국어로 변환(EBS)
    ebs_alphabet_conversion = alphabet_to_korean(ebs_number_conversion)
    
#     특수문자 제거
    ebs_punc_removed = remove_puncuations(ebs_alphabet_conversion)
    
#     점 집어넣기
#     ebs_dot_inserted = ' '.join(insert_dot(ebs_punc_removed,'.'))

#     띄어쓰기 제거
#     ebs_whitespace_removed = re.sub('[\s]+', '', ebs_punc_removed)

    return ebs_punc_removed

# GOOGLE 전처리
def GOOGLE_preprocessing(GOOGLE):
        
#     개행 삭제
    google_newline_removed = remove_newlines(GOOGLE)
    
#     수학기호 한국어로 변환
    google_math_conversion = mathsymbol_to_korean(google_newline_removed)
    
#     숫자 한국어로 변환(GOOGLE)
    google_number_conversion = number_to_korean(google_math_conversion)
        
#     알파벳 한국어로 변환(GOOGLE)
    google_alphabet_conversion = alphabet_to_korean(google_number_conversion)
    
#     특수문자 제거
    google_punc_removed = remove_puncuations(google_alphabet_conversion)
    
#     점 집어넣기
#     google_dot_inserted = ' '.join(insert_dot(google_punc_removed,'.'))
    
#     띄어쓰기 제거
#     google_whitespace_removed = re.sub('[\s]+', '', google_punc_removed)

    return google_punc_removed


# In[13]:


ko_pre_EBS = EBS_preprocessing(EBS) #한글로 치환
ko_pre_GOOGLE = GOOGLE_preprocessing(GOOGLE) #한글로 치환
dot_inserted_EBS = ' '.join(insert_dot(ko_pre_EBS,'.')).split('.')
dot_inserted_GOOGLE = ' '.join(insert_dot(ko_pre_GOOGLE,'.')).split('.')


# In[14]:


print(len(dot_inserted_EBS))
print(len(dot_inserted_GOOGLE))


# In[658]:


ws_removed_EBS = [''.join(_.split()) for _ in dot_inserted_EBS]
ws_removed_GOOGLE = [''.join(_.split()) for _ in dot_inserted_GOOGLE]


# In[ ]:


# with open('ws_removed_EBS.txt', 'wb') as f:
#     pickle.dump(ws_removed_EBS, f)
    
# with open('most_similar_GOOGLE.txt', 'wb') as f:
#     pickle.dump(most_similar_GOOGLE, f)

# with open('ws_removed_GOOGLE.txt', 'wb') as f:
#     pickle.dump(ws_removed_GOOGLE, f)


# In[17]:


# 불러올때
with open('data/ws_removed_EBS.txt', 'rb') as f:
    ws_removed_EBS = pickle.load(f)
    
with open('data/most_similar_GOOGLE.txt', 'rb') as f:
    most_similar_GOOGLE = pickle.load(f)
    
with open('data/ws_removed_GOOGLE.txt', 'rb') as f:
    ws_removed_GOOGLE = pickle.load(f)


# In[712]:


# most_similar_GOOGLE 리스트생성

# most_similar_GOOGLE = []
# for eidx, ebs_stnc in enumerate(ws_removed_EBS):
#     MIN = 150
#     for google_stnc in ws_removed_GOOGLE[eidx-200 if eidx-200 > 0 else 0:eidx+200 if eidx+200 < len(ws_removed_GOOGLE)-1 else len(ws_removed_GOOGLE)-1]:
#         current = levenshtein(ebs_stnc, google_stnc)
#         if current < MIN:
#             MIN = current
#             MIN_stnc = google_stnc
#     most_similar_GOOGLE.append(MIN_stnc)
# #     if MIN/(len(ebs_stnc)+len(google_stnc)) > 0.7:
# #         print('!!!!!!!!!!!!!!!!!!!!!!??!????????????????')
#     print(MIN, '         ', MIN/(len(ebs_stnc)+len(google_stnc)))
#     print()
#     print('ebs : ',ebs_stnc)
#     print()
#     print('google : ',MIN_stnc)
#     print()
#     print('*******'*10)


# # 유사 문장 확인

# In[18]:


for e, g in zip(ws_removed_EBS, most_similar_GOOGLE):
    nor_num = levenshtein(e, g)/((len(e)+len(g))/2)
    print('*********'*10)
    if nor_num < 0.1:
        print(levenshtein(e, g), '       ', nor_num, '     GOOD')
    elif nor_num > 0.5:
        print(levenshtein(e, g), '       ', nor_num, '     BAAD')
    else:
        print(levenshtein(e, g), '       ', nor_num)  
    print()
    print('index : ', ws_removed_EBS.index(e),  ' ',ws_removed_GOOGLE.index(g))
    print()
    print('ebs : ', e)
    print()
    print('google : ', g)
    print()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[638]:


for i, _ in enumerate(ws_removed_EBS[:200]):
    for j, google in enumerate(ws_removed_GOOGLE[i:i+3]):
        print(['EBS'])
        print(_)
        print()
        print(['GOOGLE'])
        print(google, j)
        print(levenshtein(_, google))
        print('*****************************************************************************')
        print()
        


# In[616]:


for e, g in zip(dot_inserted_EBS[:200], dot_inserted_GOOGLE[:200]):
    print(['EBS'])
    print(e)
    print()
    
    print(['GOOGLE'])
    print(g)
    print('*****************************************************************************')
    print()
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[511]:


ko_pre_EBS[5000:5500] # ~다.에만 점을 찍었음, 전체는 str


# In[513]:


ko_pre_GOOGLE[5000:5500] # ~다.에만 점을 찍었음, 전체는 str


# # 전처리끝

# # 형태소분석기 시작
# 
# #### 아래들만 남기기
# 
# - 'NNG' : 보통명사,
# - 'NNP': 고유명사,
# - 'NNB': 일반의존명사,
# - 'NR': 수사,
# - 'NP': 대명사, 
# - 'VV': 동사,
# - 'VA': 형용사,
# - 'XR': 어근
# - 'SF': 마침표

# In[391]:


kkma = Kkma()


# In[392]:


ebs_pos = kkma.pos(ko_pre_EBS) #ebs_pos : 리스트


# In[393]:


google_pos = kkma.pos(ko_pre_GOOGLE) #google_pos : 리스트


# In[394]:


def selected_pos(pos_text):
    alist = []
    for _ in pos_text:
        if _[1] in ['NNG','NNP','NNB','NR','NP', 'VV','VA','XR', 'SF']:
            alist.append(_[0])
            continue
    return alist


# In[395]:


list_ebs_pos = selected_pos(ebs_pos)


# In[396]:


list_google_pos = selected_pos(google_pos)


# In[555]:


integrated_into_W2V = [list_ebs_pos + list_google_pos]


# In[574]:


from collections import Counter
c = Counter()


# In[579]:


c = Counter(list_ebs_pos)
c.most_common(20) #EBS 형태소 최빈


# In[580]:


c = Counter(list_google_pos)
c.most_common(20) #GOOGLE 형태소 최빈


# # Skip-gram_W2V

# In[595]:


model = Word2Vec(
    integrated_into_W2V, 
    size = 100, #임베딩 차원
    min_count=1, #1번 이상 나온 단어들만
    sg = 1 # skip-gram
)
words = list(model.wv.vocab)
print(len(words))
words[3000:3020]


# In[534]:


print(model['출력']) #'출력'의 100차원 임베딩 벡터


# ### 벡터 유사도 확인

# In[535]:


model.wv.similar_by_word('콜사인',topn=20)


# In[536]:


model.wv.similar_by_word('데이트',topn=20) #대입


# In[538]:


model.wv.similar_by_word('직각',topn=20)


# In[582]:


model.wv.similar_by_word('양면',topn=20) #양변


# In[540]:


model.wv.similar_by_word('양배추',topn=20)


# In[541]:


model.wv.similar_by_word('쓰레기',topn=20) #직'선의기'울기


# In[543]:


model.wv.similar_by_word('싸이',topn=20) # sin


# In[544]:


model.wv.similar_by_word('임진각',topn=20) #끼인각


# In[565]:


model.wv.similar_by_word('교대',topn=20) #교재


# In[566]:


model.wv.similar_by_word('유기적',topn=20) # 6이죠 [육이죠]


# In[567]:


model.wv.similar_by_word('사인',topn=20)


# In[568]:


model.wv.similar_by_word('코사인',topn=20)


# In[569]:


model.wv.similar_by_word('탄젠트',topn=20)


# # 아래는 LSTM wikidocs

# ### https://wikidocs.net/45101 

# In[583]:


ebs_before_split = ' '.join(list_ebs_pos).replace(' .', '.')
ebs_morphs_sentence_list = ebs_before_split.split('.')

google_before_split = ' '.join(list_google_pos).replace(' .', '.')
google_morphs_sentence_list = google_before_split.split('.')

intg_mor_sen_list = ebs_morphs_sentence_list + google_morphs_sentence_list

print(len(intg_mor_sen_list))
intg_mor_sen_list[:20]


# In[584]:


text = intg_mor_sen_list
t = Tokenizer()
t.fit_on_texts(text)
vocab_size = len(t.word_index) + 1
print('단어 집합의 크기 : %d' % vocab_size)


# In[585]:


sequences = list()

for line in text: # 1,214 개의 샘플에 대해서 샘플을 1개씩 가져온다.
    encoded = t.texts_to_sequences([line])[0] # 각 샘플에 대한 정수 인코딩
    for i in range(1, len(encoded)):
        sequence = encoded[:i+1]
        sequences.append(sequence)

sequences[:20] # 11개의 샘플 출력


# In[592]:


# t.word_index : 단어 인덱싱
i = 0
for k, v in t.word_index.items():
    print(k, v)
    i+=1
    if i > 30:
        break


# In[494]:


index_to_word={}
for key, value in t.word_index.items(): # 인덱스를 단어로 바꾸기 위해 index_to_word를 생성
    index_to_word[value] = key

print('빈도수 상위 582번 단어 : {}'.format(index_to_word[582]))


# In[495]:


max_len=max(len(l) for l in sequences)
print('샘플의 최대 길이 : {}'.format(max_len))


# In[496]:


sequences = pad_sequences(sequences, maxlen=max_len, padding='pre')
print(sequences[:3])


# In[497]:


sequences = np.array(sequences)
X = sequences[:,:-1]
y = sequences[:,-1]


# In[498]:


print(X[:3])


# In[499]:


print(y[:3]) # 레이블


# In[500]:


vocab_size


# In[501]:


y = to_categorical(y, num_classes=vocab_size)


# In[502]:


y


# In[506]:


model = Sequential()
model.add(Embedding(vocab_size, 100, input_length=max_len-1))
# y데이터를 분리하였으므로 이제 X데이터의 길이는 기존 데이터의 길이 - 1
model.add(LSTM(10))
model.add(Dense(vocab_size, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=5, verbose=2)


# In[ ]:


def sentence_generation(model, t, current_word, n): # 모델, 토크나이저, 현재 단어, 반복할 횟수
    init_word = current_word # 처음 들어온 단어도 마지막에 같이 출력하기위해 저장
    sentence = ''
    for _ in range(n): # n번 반복
        encoded = t.texts_to_sequences([current_word])[0] # 현재 단어에 대한 정수 인코딩
        encoded = pad_sequences([encoded], maxlen=23, padding='pre') # 데이터에 대한 패딩
        result = model.predict_classes(encoded, verbose=0)
    # 입력한 X(현재 단어)에 대해서 y를 예측하고 y(예측한 단어)를 result에 저장.
        for word, index in t.word_index.items(): 
            if index == result: # 만약 예측한 단어와 인덱스와 동일한 단어가 있다면
                break # 해당 단어가 예측 단어이므로 break
        current_word = current_word + ' '  + word # 현재 단어 + ' ' + 예측 단어를 현재 단어로 변경
        sentence = sentence + ' ' + word # 예측 단어를 문장에 저장
    # for문이므로 이 행동을 다시 반복
    sentence = init_word + sentence
    return sentence


# In[ ]:


sentence_generation(model, t, '이 병 분에 높이', 5)


# In[ ]:




