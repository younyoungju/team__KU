#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 한 문장 2음절 경우의 수 구하기
# input : sentence
# output : 모든 길이의 단어 리스트
def get_words_of_two_length(s):
    answer = []
    MIN_LEN = 2
    MAX_LEN =2
    for l in range(MIN_LEN, MAX_LEN+1):
        for i in range(len(s)-l+1):
            answer.append(s[i:i+l])
    
    return answer    


# In[2]:


# input = (띄어쓰기없는 s1, 띄어쓰기없는 s2)
def find_common_part(s1, s2):
    answer = []
    s1 = ''.join(s1.split())
    s2 = ''.join(s2.split())
    
    s1_token_in_s2 = [_ for _ in get_words_of_two_length(s1) if _ in s2]
    
    for i, _ in enumerate(s1_token_in_s2):
        if i == 0:
            answer.append(_)
        else:
            if answer[-1][1:] in _ or answer[-1][-1] in _:
                answer.append(answer.pop()+_[-1])
            elif _ in answer[-1]:
                continue
            else:
                answer.append(_)
                
    return answer    

