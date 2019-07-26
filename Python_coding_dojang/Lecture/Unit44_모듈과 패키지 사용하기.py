# 지금까지 파이썬 코드를 작성하면서 input, print 등의
# 내장 함수(built-in function)를 주로 사용했는데,
# 내장 함수만으로는 할 수 있는게 별로 없습니다.
#
# 그래서 좀 더 복잡한 프로그램을 만들려면 파이썬의 모듈과 패키지를 사용해야 합니다.
# 우리가 책 중간 중간에 사용했던 random, turtle, pickle 등이 바로 모듈과 패키지입니다.

# 모듈(module)은 각종 변수, 함수, 클래스를 담고 있는 파일이고,
# 패키지(package)는 여러 모듈을 묶은 것입니다.

# 파이썬을 설치할 때 다양한 모듈과 패키지가 기본으로 설치됩니다.
# 만약 기본 모듈과 패키지로 부족하다면 다른 사람이 만든 유명 모듈과 패키지를 설치해서 쓸 수도 있습니다.


# 참고 : 모듈, 패키지, 라이브러리

# 파이썬을 배우다 보면 모듈, 패키지, 파이썬 표준 라이브러리와 같은 용어를 접하게 되는데 서로 비슷한 개념이지만 약간의 차이가 있습니다.
# 모듈: 특정 기능을 .py 파일 단위로 작성한 것입니다.
# 패키지: 특정 기능과 관련된 여러 모듈을 묶은 것입니다.
#         패키지는 모듈에 네임스페이스(namespace, 이름공간)를 제공합니다.
# 파이썬 표준 라이브러리: 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를 묶어서
# 파이썬 표준 라이브러리(Python Standard Library, PSL)라 부릅니다.




# 44.1 import로 모듈 가져오기 -----------------------------------------------------------

# import 모듈
# import 모듈1, 모듈2
# 모듈.변수
# 모듈.함수()
# 모듈.클래스()

import math
print(math.pi)

math.sqrt(4.0)

from math import pi


# 44.1.1  import as로 모듈 이름 지정하기

# 모듈의 함수를 사용할 때 math.sqrt처럼 일일이 math를 입력하기 귀찮은 사람도 있겠죠?
# 이때는 import as를 사용하여 모듈의 이름을 지정할 수 있습니다.

# * import 모듈 as 이름
import math as m    # math 모듈을 가져오면서 이름을 m으로 지정
m.sqrt(4.0)



# 44.1.2  from import로 모듈의 일부만 가져오기

# import as로 모듈의 이름을 지정하는 방법보다 좀 더 편한 방법이 있습니다.
# 이번에는 from import로 원하는 변수만 가져와보겠습니다.

# * from 모듈 import 변수

# 다음은 math 모듈에서 변수 pi만 가져옵니다.

from math import pi  # math 모듈에서 변수 pi만 가져옴
print(pi)            # pi를 바로 사용하여 원주율 출력


# 모듈의 변수를 가져왔으니 이번에는 함수를 가져와보겠습니다
# (물론 클래스도 가져올 수 있습니다).

# * from 모듈 import 함수
# * from 모듈 import 클래스

# 다음은 math 모듈에서 sqrt 함수만 가져옵니다.

from math import sqrt  # math 모듈에서 sqrt 함수만 가져옴
sqrt(4.0)  # sqrt 함수를 바로 사용


# 지금까지 변수나 함수를 하나만 가져왔습니다.
# 하지만 math 모듈에서 가져올 변수와 함수가 여러 개일 수도 있겠죠?

# 이때는 import 뒤에 가져올 변수, 함수, 클래스를 콤마로 구분하여
# 여러 개를 지정해주면 됩니다.

# from 모듈 import 변수, 함수, 클래스

from math import pi, sqrt  # math 모듈에서 pi, sqrt를 가져옴

# from math import pi, sqrt와 같이 pi와 sqrt 두 개를 가져왔습니다.
# 하지만 변수, 함수, 클래스가 두세 개라면 괜찮지만 수십 개가 된다면 입력하기가 상당히 번거롭겠죠?
# from import는 모듈의 모든 변수, 함수, 클래스를 가져오는 기능도 있습니다.

# from 모듈 import *

# 다음은 math 모듈의 모든 변수, 함수, 클래스를 가져옵니다.

from math import *



# 44.1.3  from import로 모듈의 일부를 가져온 뒤 이름 지정하기

# 이번에는 from import로 변수, 함수, 클래스를 가져온 뒤 이름을 지정해보겠습니다.

# from 모듈 import 변수 as 이름
# from 모듈 import 함수 as 이름
# from 모듈 import 클래스 as 이름

# 다음은 math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정합니다.

from math import sqrt as s  # math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정

s(4.0)

# 그럼 여러 개를 가져왔을 때 각각 이름을 지정할 수는 없을까요?
# 이때는 각 변수, 함수, 클래스 등을 콤마로 구분하여 as를 여러 개 지정하면 됩니다.

# * from 모듈 import 변수 as 이름1, 함수 as 이름2, 클래스 as 이름3

from math import pi as p, sqrt as s



# 참고 : 가져온 모듈 해제하기, 다시 가져오기

# import로 가져온 모듈(변수, 함수, 클래스)은 del로 해제할 수 있습니다.

import math
del math

# 모듈을 다시 가져오려면 importlib.reload를 사용합니다.

import importlib
import math

importlib.reload(math)



