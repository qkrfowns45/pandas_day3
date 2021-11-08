# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 21:47:49 2021

@author: qkrfo
"""
import pandas as pd
import numpy as np
import seaborn as sns

student1 = pd.Series({'국어' : 100, '영어' : 80, '수학' : 90})
print(student1)
print('\n')

#전체 변수들이 나눠진다.
percentage = student1/200

print(percentage)
print('\n')
print(type(percentage))

student2 = pd.Series({'수학' : 80, '국어' : 90, '영어' : 80})
print(student1)
print('\n')
print(student2)
print('\n')

#각 index를 찾아서 사직연산을 할 수 있다.
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1/student2
print(type(division))
print('\n')

result = pd.DataFrame([addition,subtraction,multiplication,division], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)
print('\n')

student3 = pd.Series({'국어' : np.nan, '영어' : 80,'수학' : 90})
student4 = pd.Series({'수학' : 80 ,'국어' : 90})

print(student3)
print('\n')
print(student4)
print('\n')

#사칙연산이 불가능한것은(데이터가 없는경우) nan으로 나온다.
addition = student3 + student4
subtraction = student3 - student4
multiplication = student3 * student4
division = student3/student4
print(type(division))
print('\n')

result = pd.DataFrame([addition,subtraction,multiplication,division], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

#시리즈 연산
sr_add = student3.add(student4,fill_value = 0)
sr_sub = student3.sub(student4,fill_value = 0)
sr_mul = student3.mul(student4,fill_value = 0)
sr_div = student3.div(student4,fill_value = 0)

result = pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)
print('\n')

#데이터프레임 더하기 타이타닉은 seaborn라이브러리에서 제공하는 데이터셋
titanic = sns.load_dataset('titanic')
df = titanic.loc[:,['age','fare']]
print(df.head())
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.head())
print('\n')
print(type(addition))

print(df.tail())
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))

subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))














