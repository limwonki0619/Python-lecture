
# 03.1 **데이터프레임 인덱싱 정리**

데이터프레임(Data-Frame) 클래스는 2차원 행렬 데이터에 인덱스를 붙인 것과 비슷하다. 2차원이므로 각각의 행 데이터의 이름이 되는 **행방향 인덱스(row index)** 뿐 아니라 각각의 열 데이터의 이름이 되는 **열방향 인덱스(column index)**도 붙일 수 있다.

# **기본 인덱싱 방법**

## **데이터프레임 생성**

데이터프레임을 만드는 방법은 다양하다. 가장 간단한 방법은 다음과 같다.

1. 우선 하나의 열이 되는 데이터를 리스트나 일차원 배열을 준비한다.  
2. 이 각각의 열에 대한 이름(라벨)을 키로 가지는 딕셔너리를 만든다.  
3. 이 데이터를 DataFrame 클래스 생성자에 넣는다. 동시에 열방향 인덱스는 columns 인수로, 행방향 인덱스는 index 인수로 지정한다.


```python
import numpy as np
import pandas as pd

data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
columns = ["지역", "2015", "2010", "2005", "2000", "2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df = pd.DataFrame(data, index=index, columns=columns)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>0.0283</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>0.0163</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>0.0982</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2431774</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>0.0141</td>
    </tr>
  </tbody>
</table>
</div>



앞에서 데이터프레임은 2차원 배열 데이터를 기반으로 한다고 했지만 사실은 공통 인덱스를 가지는 열 시리즈(column series)를 딕셔너리로 묶어놓은 것이라고 보는 것이 더 정확하다. 2차원 배열 데이터는 모든 원소가 같은 자료형을 가져야 하지만 데이터프레임은 각 열(column)마다 자료형이 다를 수 있기 때문이다. 위 예제에서도 지역과 인구와 증가율은 각각 문자열, 정수, 부동소수점 실수이다.


```python
# 데이터에 접근하기 

df.values
```




    array([['수도권', 9904312, 9631482, 9762546, 9853972, 0.0283],
           ['경상권', 3448737, 3393191, 3512547, 3655437, 0.0163],
           ['수도권', 2890451, 2632035, 2517680, 2466338, 0.0982],
           ['경상권', 2466052, 2431774, 2456016, 2473990, 0.0141]], dtype=object)




```python
# 열 인덱스 접근하기

df.columns
```




    Index(['지역', '2015', '2010', '2005', '2000', '2010-2015 증가율'], dtype='object')




```python
# 행 인덱스 접근하기

df.index
```




    Index(['서울', '부산', '인천', '대구'], dtype='object')



## **열 데이터의 갱신, 추가, 삭제**

데이터프레임은 열 시리즈의 딕셔너리으로 볼 수 있으므로 열 단위로 데이터를 갱신하거나 추가, 삭제할 수 있다.


```python
# 열 데이터 갱신

df["2010-2015 증가율"] = df['2010-2015 증가율'] * 100 
df 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>2830000.0</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>1630000.0</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>9820000.0</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2431774</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>1410000.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 열 데이터 추가 

df["2005-2010 증가율"] = ((df["2010"] - df["2005"]) / df["2005"] * 100).round(2)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2010-2015 증가율</th>
      <th>2005-2010 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>2830000.0</td>
      <td>-1.34</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>1630000.0</td>
      <td>-3.40</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>9820000.0</td>
      <td>4.54</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2431774</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>1410000.0</td>
      <td>-0.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 열 데이터 삭제 

# 방법 1. del 활용

del df["2010-2015 증가율"]
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2010 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>-1.34</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-3.40</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>4.54</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2431774</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>-0.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 방법 2. drop 활용

df.drop('2005-2010 증가율', axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2431774</td>
      <td>2456016</td>
      <td>2473990</td>
    </tr>
  </tbody>
</table>
</div>



## **열 인덱싱**

데이터프레임은 열 시리즈의 딕셔너리와 비슷하다고 하였다. 따라서 데이터프레임을 인덱싱을 할 때도 열 라벨(column label)을 키값으로 생각하여 인덱싱을 할 수 있다.   
인덱스로 라벨 값을 **하나만 넣으면 시리즈 객체가 반환**되고, 라벨의 배열 또는 리스트를 넣으면 **부분적인 데이터프레임이 반환**된다.

- df[ '열 라벨' ] : 시리즈 객체 반환, 하나의 열을 선택 
- df[ [ '열 라벨들' ] ]  : 부분적인 데이터프레임 반환, 여러개의 열을 선택


```python
df['지역']  # '지역' 컬럼을 시리즈 객체로 반환 
```




    서울    수도권
    부산    경상권
    인천    수도권
    대구    경상권
    Name: 지역, dtype: object




```python
df[['2010', '2015']]  # '2010' 열과, '2015'열을 데이터프레임으로 반환 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2010</th>
      <th>2015</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>9631482</td>
      <td>9904312</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>3393191</td>
      <td>3448737</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>2632035</td>
      <td>2890451</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>2431774</td>
      <td>2466052</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[['2010']]  # 하나의 열만 선택하되, 데이터프레임으로 반환 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2010</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>9631482</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>3393191</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>2632035</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>2431774</td>
    </tr>
  </tbody>
</table>
</div>



데이터프레임의 **열 인덱스가 문자열 라벨을 가지고 있는 경우**에는 순서를 나타내는 **정수 인덱스를 열 인덱싱에 사용할 수 없다.** 정수 인덱싱의 슬라이스는 뒤에서 설명하겠지만 행(row)을 인덱싱할 때 사용하므로 열을 인덱싱할 때는 쓸 수 없다. 정수 인덱스를 넣으면 KeyError 오류가 발생하는 것을 볼 수 있다.

- 열 인덱스가 '문자'일 경우, 숫자로 열 인덱싱을 할 수 없다.
- 숫자 인덱싱은 행 인덱싱에 사용되기 때문이다.
- 다만, 열 인덱스가 원래부터 숫자인 경우, 인덱스 값으로 숫자를 사용할 수 있다. 예를 들면 아래와 같다.


```python
df2 = pd.DataFrame(np.arange(12).reshape(3, 4))  # 열 인덱스가 숫자로 이루어져 있다.
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2[2]  # 열 인덱스가 2인 데이터를 반환, 열 인덱스가 원래부터 숫자이므로 숫자 인덱싱을 사용할 수 있다.
```




    0     2
    1     6
    2    10
    Name: 2, dtype: int32




```python
df2[[1, 2]] # 1, 2열 반환 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



## **행 인덱싱**

만약 행 단위로 인덱싱을 하고자 하면 항상 **슬라이싱(slicing)을 해야 한다.** 인덱스의 값이 문자 라벨이면 라벨 슬라이싱도 가능하다.

- 행 인덱싱에는 슬라이싱이 사용된다. 


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2010 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>-1.34</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-3.40</td>
    </tr>
    <tr>
      <th>인천</th>
      <td>수도권</td>
      <td>2890451</td>
      <td>2632035</td>
      <td>2517680</td>
      <td>2466338</td>
      <td>4.54</td>
    </tr>
    <tr>
      <th>대구</th>
      <td>경상권</td>
      <td>2466052</td>
      <td>2431774</td>
      <td>2456016</td>
      <td>2473990</td>
      <td>-0.99</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[:1]  # 1번째 행 반환 (슬라이싱)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2010 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>-1.34</td>
    </tr>
  </tbody>
</table>
</div>




```python
df[1:2]  # 2번째 행 반환 (슬라이싱)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2010 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-3.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['서울':'부산']  # 행 인덱스가 문자열이므로 문자열을 이용한 슬라이싱도 가능하다. 

# 다만 이떄 사용하는 슬라이싱은 뒤쪽 인덱스까지 포함되는 행을 반환한다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>지역</th>
      <th>2015</th>
      <th>2010</th>
      <th>2005</th>
      <th>2000</th>
      <th>2005-2010 증가율</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>서울</th>
      <td>수도권</td>
      <td>9904312</td>
      <td>9631482</td>
      <td>9762546</td>
      <td>9853972</td>
      <td>-1.34</td>
    </tr>
    <tr>
      <th>부산</th>
      <td>경상권</td>
      <td>3448737</td>
      <td>3393191</td>
      <td>3512547</td>
      <td>3655437</td>
      <td>-3.40</td>
    </tr>
  </tbody>
</table>
</div>



## **개별 데이터 인덱싱**

데이터프레임에서 열 라벨로 시리즈를 인덱싱하면 시리즈가 된다. 이 시리즈를 다시 행 라벨로 인덱싱하면 개별 데이터가 나온다.


```python
df['2015']['서울']  # df[열][행]
```




    9904312



# **고급 인덱싱 방법**

데이터프레임에서 **특정한 데이터만 골라내는 것을 인덱싱(indexing)이라고 한다.** 앞 절에서는 라벨, 라벨 리스트, 인덱스데이터(정수) 슬라이스의 3가지 인덱싱 값을 사용하여 인덱싱을 하는 방법을 공부하였다. 그런데 Pandas는 numpy행렬과 같이 **쉼표를 사용한 (행 인덱스, 열 인덱스) 형식의 2차원 인덱싱을 지원**하기 위해 다음과 같은 특별한 인덱서(indexer) 속성도 제공한다.

- `loc` : 라벨값 기반의 2차원 인덱싱, 기본 인덱싱 방법과 행, 열 선택이 반대다. 
- `iloc` : 순서를 나타내는 정수 기반의 2차원 인덱싱
- `at`: 라벨값 기반의 2차원 인덱싱 (한개의 스칼라 값만 찾는다)
- `iat` : 순서를 나타내는 정수 기반의 2차원 인덱싱 (한개의 스칼라 값만 찾는다)

## **`loc` 인덱서**

`loc` 인덱서는 다음처럼 사용한다.

- `df.loc[행]`
- `df.loc[행, 열]`

이 때 행과 열에 들어가는 값은 다음 중 하나이다.

- **열** 인덱싱 값은 `라벨 문자열이다`
- **행** 인덱싱 값은 `정수`또는 `행 인덱스데이터`이다.

### **인덱싱값을 하나만 받는 경우** : [행]

`loc` 인덱서를 사용하면서 인덱스를 하나만 사용하면, **행(row)**을 선택한다.   
인덱스데이터가 'a'인 데이터를 선택하면, 해당하는 행이 시리즈로 출력된다.


```python
df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index=["a", "b", "c"],
                  columns=["A", "B", "C", "D"])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>b</th>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>c</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['a']  # 'a' 행을 반환한다.
```




    A    10
    B    11
    C    12
    D    13
    Name: a, dtype: int32




```python
df.loc['a':'c']  # 'a' 행부터 'c' 행 까지 반환한다. 이는 df['a':'c']와 같은 출력값이다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>b</th>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>c</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[['b']]  # 하나의 'b'행을 출력했지만, 시리즈로 받지 않고 데이터프레임으로 받았다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[['a', 'c']]  # 'a'와 'c'행을 리스트를 이용해 반환받았다. loc 인덱서에서만 행 인덱싱에서 콤마를 사용할 수 있다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>c</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df[['b','c']]  # loc 인덱서가 없는 경우, KeyError가 발생한다.
```


```python
df['a':'c']  # loc를 사용하지 않는 기본 인덱싱으로 각각의 행을 반환받을 수 없다. 항상 슬라이싱만 사용가능하다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>b</th>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>c</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



따라서 'a'행과 'c' 행을 기본 인덱싱으로 출력받고자한다면 아래와 같은 슬라이싱 방법이 필요하다.


```python
df['a'::2]  # 'a'행 부터, 한 행씩 건너뛴 행을 반환받는다. 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>c</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df.loc['A']  # loc 인덱서는 하나의 인덱스 값을 받을 경우 '행'으로 들어가기 떄문에, 하나의 입력값으로는 열을 선택할 수 없다.
```


```python
df.loc[:,'A']  # 따라서 loc인덱서는 [행, 열]로 인덱스 값을 받으므로, 전체 행에 해당하는 ':'가 필요하다.
```




    a    10
    b    14
    c    18
    Name: A, dtype: int32



### **인덱싱값을 행과 열 모두 받는 경우** : [행, 열]

인덱싱값을 행과 열 모두 받으려면 `df.loc[행 인덱스, 열 인덱스]`와 같은 형태로 사용한다. 행 인덱스 라벨값이 a, 열 인덱스 라벨값이 A인 위치의 값을 구하는 것은 다음과 같다.


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>b</th>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>c</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['a', 'A']  # 'a'행 'A'열 
```




    10




```python
df.loc['b':,'A'] # 'b'행부터 끝까지, 'A'열 
```




    b    14
    c    18
    Name: A, dtype: int32




```python
df.loc['a',:]  # 'a'행과 모든 열 
```




    A    10
    B    11
    C    12
    D    13
    Name: a, dtype: int32




```python
df.loc[['a','c'], ['B','D']]  # 'a', 'c'행과 'B', 'D'열 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>11</td>
      <td>13</td>
    </tr>
    <tr>
      <th>c</th>
      <td>19</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc['a'::2, 'B':'C']  # 행, 열 인덱스에 슬라이싱도 가능하다
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>c</th>
      <td>19</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.loc[df.A > 10, ['C','D']]  # 'A'열에서 10이상인 행과 'C', 'D'열
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>b</th>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>c</th>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>



## **`iloc` 인덱서**

iloc 인덱서는 loc 인덱서와 반대로 라벨이 아니라 순서를 나타내는 **정수(integer) 인덱스만** 받는다. 다른 사항은 loc 인덱서와 같다.


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>10</td>
      <td>11</td>
      <td>12</td>
      <td>13</td>
    </tr>
    <tr>
      <th>b</th>
      <td>14</td>
      <td>15</td>
      <td>16</td>
      <td>17</td>
    </tr>
    <tr>
      <th>c</th>
      <td>18</td>
      <td>19</td>
      <td>20</td>
      <td>21</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[0, 1]  # '0'행과, '1'열의 데이터
```




    11




```python
df.iloc[:2, 2]  # 2행 까지와, '3'열 
```




    a    12
    b    16
    Name: C, dtype: int32




```python
df.iloc[2:3, 1:3]  # '2'행과 '1, 2'열
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>c</th>
      <td>19</td>
      <td>20</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.iloc[-1]  # 마지막 행, loc 인덱서와 마찬가지로 인덱스가 하나만 들어가면 '행'을 선택한다.
```




    A    18
    B    19
    C    20
    D    21
    Name: c, dtype: int32



<hr>

# **기본 인덱싱 정리**

### **열 인덱싱**

- `df ['하나의 문자열 인덱스']` : 하나의 열을 **시리즈**로 반환 
- `df [['둘 이상의 문자열 인덱스']]` : 둘 이상의 열을 **데이터프레임**으로 반환
- `df [['하나의 문자열 인덱스']]` : 하나의 열을 **데이터프레임**으로 반환 
- `df [숫자 인덱스]` : 열 인덱스가 **원래 숫자**인 경우여야 가능하며, **시리즈**로 반환
- `df [[숫자인덱스1, 숫자인덱스2]]` : 열 인덱스가 **원래 숫자**인 경우여야 가능하며, **데이터프레임**으로 반환 

### **행 인덱싱**

행 인덱싱은 항상 **슬라이싱**으로 사용한다. 또한 행 인덱스 값이 **문자 라벨**인 경우, **라벨 슬라이싱**도 가능하다.

- `df[:1]` : 첫번쨰 행 반환 
- `df[1:2]` : 두번째 행 반환
- `df[1:3]` : 두 세번째 행 반환
- `df['문자 라벨1', '문자 라벨2']` : 라벨1부터 라벨2까지 포함하는 행 반환 

### **개별 인덱싱**

기본적인 데이터프레임 인덱싱은 
`df[열][행]` 으로 이루어진다. 결과값은 스칼라 값으로 출력된다.

# **고급 인덱싱 정리**

### **`loc` 인덱서** 

- 인덱스 값으로 `문자 라벨`을 받는다.
- `df.loc[행]`
- `df.loc[행, 열]`

인덱싱 값으로 사용가능한 것은 다음과 같다.

- 인덱스데이터
- 인덱스데이터 슬라이스
- 인덱스데이터 리스트
- 같은 행 인덱스를 가지는 불리언 시리즈 (행 인덱싱의 경우)
- 또는 위의 값들을 반환하는 함수


### **`iloc` 인덱서**

- 인덱스 값으로 `정수(숫자)`을 받는다.
- 나머지는 `loc`인덱서와 동일하다.

# **기본 인덱싱 vs 고급 인덱싱**

### **기본 인덱싱의 경우**

`df[열]` : 인덱스 값이 하나만 입력되는 경우 **열**을 반환한다.  

`df[열][행]`으로 인덱싱이 이뤄진다.  

 `행` 을 인덱싱 하고자 할 경우 항상 **슬라이싱**을 사용해야 한다. 

### **고급 인덱싱의 경우**

`df.loc[행]` : 인덱스 값이 하나만 입력되는 경우 **행**을 반환한다.   

`df.loc[행, 열]`로 인덱싱이 이뤄진다.

`열`을 인덱싱 하고자 할 경우 `:` 등을 행 인덱스 자리에 입력 한 후 원하는 열을 인덱싱 한다.
