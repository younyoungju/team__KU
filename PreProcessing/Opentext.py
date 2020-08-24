#!/usr/bin/env python
# coding: utf-8

# In[5]:


def get_EBS_entered(s, e):
    # 파일 이름 만들기 #################################################
    EBS_filenames = []
    for i in range(s, e+1):
        n = '{0:05d}'.format(i)
        EBS_fname = 'lec' + n + '_EBS_entered.txt'
        EBS_filenames.append(EBS_fname)
    print(EBS_filenames)
    ####################################################
    
    # 파일 불러오기 ###################################################
    EBS_integrated = ''
    try:
        for _ in EBS_filenames:
            with open('data/' + _, 'r', encoding = 'utf8') as f:
                if EBS_filenames.index(_) == 0:
                    EBS_integrated += f.read() 
                else:
                    EBS_integrated += ' '+f.read()
    except:
        for _ in EBS_filenames:
            with open('data/' + _, 'r') as f:
                if EBS_filenames.index(_) == 0:
                    EBS_integrated += f.read() 
                else:
                    EBS_integrated += ' '+f.read()
    ####################################################
    
    return EBS_integrated


# In[6]:


def get_STT1_Google_entered(s, e):
    # 파일 이름 만들기 #################################################
    STT_filenames = []
    for i in range(s, e+1):
        n = '{0:05d}'.format(i)
        STT_fname = 'lec' + n + '_STT1_Google_entered.txt'
        STT_filenames.append(STT_fname)
    print(STT_filenames)
    ####################################################
    
    # 파일 불러오기 ###################################################
    STT_integrated = ''
    
    try:
        for _ in STT_filenames:
            with open('data/' + _, 'r', encoding = 'utf8') as f:
                if STT_filenames.index(_) == 0:
                    STT_integrated += f.read() 
                else:
                    STT_integrated += ' '+f.read()
    except:
        for _ in STT_filenames:
            with open('data/' + _, 'r') as f:
                if STT_filenames.index(_) == 0:
                    STT_integrated += f.read() 
                else:
                    STT_integrated += ' '+f.read()   
    ####################################################
    
    return STT_integrated


# In[7]:


def get_STT1_Transcribe_entered(s, e):
    # 파일 이름 만들기 #################################################
    STT_filenames = []
    for i in range(s, e+1):
        n = '{0:05d}'.format(i)
        STT_fname = 'lec' + n + '_STT1_Transcribe_entered.txt'
        STT_filenames.append(STT_fname)
    print(STT_filenames)
    ####################################################
    
    # 파일 불러오기 ###################################################
    STT_integrated = ''
    
    try:
        for _ in STT_filenames:
            with open('data/' + _, 'r', encoding = 'utf8') as f:
                if STT_filenames.index(_) == 0:
                    STT_integrated += f.read() 
                else:
                    STT_integrated += ' '+f.read()
    except:
        for _ in STT_filenames:
            with open('data/' + _, 'r') as f:
                if STT_filenames.index(_) == 0:
                    STT_integrated += f.read() 
                else:
                    STT_integrated += ' '+f.read()
    ####################################################
    
    return STT_integrated


# In[1]:


def get_EBS(s, e):
    # 파일 이름 만들기 #################################################
    EBS_filenames = []
    for i in range(s, e+1):
        n = '{0:05d}'.format(i)
        EBS_fname = 'lec' + n + '_EBS.txt'
        EBS_filenames.append(EBS_fname)
    print(EBS_filenames)
    ####################################################
    
    # 파일 불러오기 ###################################################
    EBS_integrated = ''
    try:
        for _ in EBS_filenames:
            with open('data/' + _, 'r', encoding = 'utf8') as f:
                if EBS_filenames.index(_) == 0:
                    EBS_integrated += f.read() 
                else:
                    EBS_integrated += ' '+f.read()
    except:
        for _ in EBS_filenames:
            with open('data/' + _, 'r') as f:
                if EBS_filenames.index(_) == 0:
                    EBS_integrated += f.read() 
                else:
                    EBS_integrated += ' '+f.read()
    ####################################################
    
    return EBS_integrated


# In[1]:


def get_STT1_Google(s, e):
    # 파일 이름 만들기 #################################################
    STT_filenames = []
    for i in range(s, e+1):
        n = '{0:05d}'.format(i)
        STT_fname = 'lec' + n + '_STT1_Google.txt'
        STT_filenames.append(STT_fname)
    print(STT_filenames)
    ####################################################
    
    # 파일 불러오기 ###################################################
    STT_integrated = ''
    
    try:
        for _ in STT_filenames:
            with open('data/' + _, 'r', encoding = 'euc-kr') as f:
                if STT_filenames.index(_) == 0:
                    STT_integrated += f.read() 
                else:
                    STT_integrated += '\n'+f.read()
    except:
        for _ in STT_filenames:
            with open('data/' + _, 'r') as f:
                if STT_filenames.index(_) == 0:
                    STT_integrated += f.read() 
                else:
                    STT_integrated += '\n'+f.read()   
    ####################################################
    
    return STT_integrated


# In[ ]:




