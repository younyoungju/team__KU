#!/usr/bin/env python
# coding: utf-8

# In[1]:


# symbol dictionary
sd = {'½': '이분의일',
 '□': '사각형',
 '＞': '보다크다',
 '㈏': '나',
 '(': '',
 '×': '곱하기',
 ')': '',
 '①': '일',
 '+': '더하기',
 '˚': '도',
 '⑤': '오',
 '⅓': '삼분의일',
 '⅔': '삼분의이',
 '¼': '사분의일',
 '′': '',
 '＜': '보다작다',
 '-': '마이너스',
 '!': '',
 '④': '사',
 'π': '파이',
 '㎞': '킬로미터',
 '=': '는',
 ':': '대',
 '~': '',
 '…': '',
 '△': '삼각형',
 '²': '의제곱',
 '②': '이',
 '㈎': '가',
 '≤': '보다크거나같다',
 '㎝': '센치미터',
 '|': '절대값',
 '㈐': '다',
 '＝': '는',
 '÷': '나누기',
 '⑵': '이번',
 '㎠': '제곱센치미터',
 '¾': '사분의삼',
 '∠': '각',
 '%': '퍼센트',
 '－': '마이너스',
 "'": '',
 '③': '삼',
 '＋': '더하기',
 '⑴': '일번',
 '√': '루트',
 'cos': '코사인',
 'sin': '사인',
 'tan': '탄젠트', 
     'm' : '미터',
     'con' : '코사인', 
     'sim' : '사인', 
     'tna' : '탄젠트',
     '*' : '곱하기'}


# In[ ]:


ad = {
    'a':'에이',
    'b':'비',
    'c':'씨',
    'd':'디',
    'e':'이',
    'f':'에프',
    'g':'쥐',
    'h':'에이치',
    'i':'아이',
    'j':'제이',
    'k':'케이',
    'l':'엘',
    'm':'엠',
    'n':'엔',
    'o':'오',
    'p':'피',
    'q':'큐',
    'r':'알',
    's':'에스',
    't':'티',
    'u':'유',
    'v':'브이',
    'w':'더블유',
    'x':'엑스',
    'y':'와이',
    'z':'지',
    'A':'에이',
    'B':'비',
    'C':'씨',
    'D':'디',
    'E':'이',
    'F':'에프',
    'G':'쥐',
    'H':'에이치',
    'I':'아이',
    'J':'제이',
    'K':'케이',
    'L':'엘',
    'M':'엠',
    'N':'엔',
    'O':'오',
    'P':'피',
    'Q':'큐',
    'R':'알',
    'S':'에스',
    'T':'티',
    'U':'유',
    'V':'브이',
    'W':'더블유',
    'X':'엑스',
    'Y':'와이',
    'Z':'지'
}


# In[3]:


def get_korean_pronunciation_of_number(n):
    nbased = {0 : '', 1 : '일', 2 : '이', 3 : '삼', 4 : '사', 5 : '오', 6 : '육', 7 : '칠', 8 : '팔', 9 : '구' }
    nkopro = {}
    for _ in range(n+1):
        c = (_%100000000)//10000000
        b = (_%10000000)//1000000
        s = (_%1000000)//100000
        m = (_%100000)//10000
        t = (_%10000)//1000
        h = (_%1000)//100
        d = (_%100)//10
        o = _%10

        if _ == 0:
            nkopro[_] = '영'
        else:
            cc = '' if c == 0 else ('천' if c == 1 else nbased[c] + '천')
            bb = '' if b == 0 else ('백' if b == 1 else nbased[b] + '백')
            ss = '' if s == 0 else ('십' if s == 1 else nbased[s] + '십')
            if s == 0:
                mm = '' if m == 0 else ('만' if m == 1 else nbased[m] + '만')
            else:
                mm = '만' if m == 0 else ('일만' if m == 1 else nbased[m] + '만')
            tt = '' if t == 0 else ('천' if t == 1 else nbased[t] + '천')
            hh = '' if h == 0 else ('백' if h == 1 else nbased[h] + '백')
            dd = '' if d == 0 else ('십' if d == 1 else nbased[d] + '십')
            oo = '' if o == 0 else nbased[o]
            nkopro[_] = cc+bb+ss+mm+tt+hh+dd+oo
            
    return nkopro


# In[6]:


kopro = get_korean_pronunciation_of_number(9999999) #~99999


# In[11]:


kopro[1800178]


# In[54]:


kopro[999999]


# In[55]:


kopro[808214]


# In[56]:


kopro[818214]


# In[57]:


kopro[118214]


# In[58]:


kopro[108214]


# In[59]:


kopro[12548]


# In[60]:


kopro[118214]


# In[61]:


kopro[180000]


# In[62]:


kopro[118214]


# In[35]:


_ = 12548 #천오백십팔만
c = (_%100000000)//10000000
b = (_%10000000)//1000000
s = (_%1000000)//100000
m = (_%100000)//10000
t = (_%10000)//1000
h = (_%1000)//100
d = (_%100)//10
o = _%10
print(c)
print(b)
print(s)
print(m)
print(t)
print(h)
print(d)
print(o)


# In[ ]:




