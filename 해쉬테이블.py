# 해쉬 구조
# 키에 데이터를 저장하는 데이터 구조
# 파이썬에서는 딕셔너리 사용하면 됨 내부적으로 해쉬 테이블로 구현됨
# 키를 가지고 바로 value 데이터 꺼냄


# 알아둘 용어
"""
해쉬 - 임의 값을 고정 길이로 변환하는 것
해쉬 테이블 - 키 값의 연산에 의해 직접 접근이 가능한 데이터 구조
해싱 함수 - Key에 대해 산술 연산을 이용해 데이터 위치를 찾을 수 있는 함수
해쉬 값 또는 해쉬 주소 - Key를 해싱 함수로 연산해서 , 해쉬 값을 알아내고 이를 기반으로 해쉬 테이블에서
해당 Key에 대한 데이터 위치를 일관성 있게 찾을 수 있음
슬롯 - 한 개의 데이터를 저장할 수 있는 공간
저장할 데이터에 대해 Key를 추출할 수 있는 별도 함수도 존재할 수 있음
"""

# 간단한 해쉬 예
hash_table = list([0 for i in range(10)])

# 해쉬 함수


def hash_func(key):
    return key % 5


# 해쉬 테이블에 저장
data1 = "Andy"  # 65
data2 = "Dave"  # 68
data3 = "Trump"  # 84

# ord(): 문자의 ASCII 코드 리턴
#print(ord(data1[0]), ord(data2[0]), ord(data3[0]))
# print(hash_func(ord(data1[0])))
# print(hash_func(ord(data2[0])))
# print(hash_func(ord(data3[0])))

# 해쉬 테이블에 값 저장


def storage_data(data, value):
    key = ord(data[0])
    hash_address = hash_func(key)
    hash_table[hash_address] = value
    # print(hash_table)


storage_data("Andy", "01055553333")
storage_data("Dave", "01044443333")
storage_data("Trump", "01022223333")

# 실제 데이터를 저장하고 읽어보기


def get_data(data):
    key = ord(data[0])
    hash_address = hash_func(key)
    return hash_table[hash_address]


print(get_data("Andy"))

# 자료구조 해쉬 테이블의 장단점과 주요 용도
# 장점:
# - 데이터 저장/읽기 속도가 빠르다
# - 해쉬는 키에 대한 데이터가 있는지(중복) 확인이 쉬움

# 단점:
# - 일반적으로 저장공간이 더 많이 필요
# - 여러 키에 해당하는 주소가 동일할 경우 충돌을 해결하기 위한 별도 자료구조 필요

# 주요 용도
# - 검색이 많이 필요한 경우
# - 저장, 삭제, 읽기가 빈번한 경우
# - 캐쉬 구현시
