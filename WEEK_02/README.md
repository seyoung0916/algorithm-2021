## 백준 4101 (크냐?)  
:pushpin: 유형
* 기본 문법

:question: 문제  
* 두 수를 입력받아 앞이 크면 Yes, 아니면 No 출력
* 0 0을 입력하면 종료

:heavy_check_mark: 해결
* 단순 분기로 처리
  
---  

## 백준 10156 (과자)
:pushpin: 유형
* 연산

:question: 문제
* K : 과자 가격, N : 사려는 과자 개수, M : 현재 가진 돈
* 과자를 사려할 때 부모님께 받아야 하는 돈 계산(부족할 때)

:heavy_check_mark: 해결
* N*K : 과자를 살 때 필요한 돈
* N*K > M일 때 부모님께 받아야함, <= M 인 경우 안 받아도 됨

---  

## 백준 3009 (네 번째 점)
:pushpin: 유형
* 연산

:question: 문제
* 세 점이 주어졌을 때 사각형의 마지막 점 출력

:heavy_check_mark: 해결  
* 입력을 받아 딕셔너리 자료형에 해당 숫자의 출현 횟수를 저장(xcheck, ycheck) <br>
  -> 기존에 있던 숫자면 +1, 아니면 1로 저장
* xcheck, ycheck를 확인하면서 value값이 1이면 그게 x, y가 됨

---  

## 백준 2476 (주사위 게임)
:pushpin: 유형
* 연산

:question: 문제
* N명의 참여자, 주사위 3개 입력
* 같은 눈 3개, 2개, 모두 다를 때마다 상금이 다름
* N명의 참가자 중 가장 많은 상금을 받는 사람의 상금 출력

:heavy_check_mark: 해결  
* 세 값이 같은 경우 상금이 클 때 값을 갱신
* 두 값이 같은 경우 -> 두 가지 케이스로 나뉨
  1) a==b, a==c -> a로 상금 계산
  2) b==c -> b로 상금 계산
* 세 값이 모두 다른 경우, 최댓값으로 상금 계산해 크면 갱신

---  

## 백준 2754 (학점계산)
:pushpin: 유형
* 단순 분기

:question: 문제
* 학점을 입력받아 평균 출력

:heavy_check_mark: 해결  
* if, elif, else 사용

---  

## 백준 2884 (알람시계)
:pushpin: 유형
* 연산, 분기

:question: 문제
* 입력받은 두 숫자(시간, 분)에서 45분을 뺀 시간을 구하기

:heavy_check_mark: 해결  
* 분 - 45 계산 -> 음수면 60(한시간)을 더해 양수로 만들기
* 분에서 음수였을 경우에 1을 빼주기 -> 음수이면 24(하루) 더해주기

---  

## 백준 7567 (그릇)
:pushpin: 유형
* 배열 인덱스

:question: 문제
* 그릇 하나의 높이 : 10cm
* 같은 방향으로 포개질 경우 : 5cm 증가, 다른 방향 : 10cm 증가

:heavy_check_mark: 해결  
* 입력값을 순서대로 확인하면서 이전 것과 같은지 다른지에 따라 높이 증가

---

## 백준 5063 (TGN)
:pushpin: 유형
* 연산

:question: 문제
* r : 광고X 수익, e : 광고O 수익, c : 광고 비용
* 광고 할지 말지를 출력

:heavy_check_mark: 해결  
* r > e-c 이면 광고X, = 이면 상관X, <이면 광고

---

## 백준 10102 (개표)
:pushpin: 유형
* 배열

:question: 문제
* N명의 심사위원이 투표하여 누가 뽑혔는지를 출력
* 표 수가 같은 경우는 'Tie' 출력

:heavy_check_mark: 해결  
* N만큼 입력받아 count를 사용해 A, B 개수 비교

---

## 백준 10886 (0 = not cute / 1 = cute)
:pushpin: 유형
* 배열

:question: 문제
* N명 설문조사, 0이 귀엽지 않다, 1이 귀엽다라는 의미
* 귀여운지 안 귀여운지를 출력

:heavy_check_mark: 해결  
* N만큼 입력받아 count를 사용해 0, 1 개수 비교

---  

## LeetCode 3247 (Remove Element)
:pushpin: 유형
* 배열

:question: 문제
* 배열 nums와 값 val이 주어졌을 때, nums에서 val을 제거하고 새로운 길이를 출력

:heavy_check_mark: 해결  
* len(nums)의 고정 길이만큼 반복
* idx는 nums의 비교해야 할 원소를 가리킴
* idx번째 값과 val이 같으면 삭제하고 idx를 그대로 냅둠 <br>
  -> 그렇게 해야 다음 비교 때 idx번째의 원소를 다시 비교 <br>
  같지 않은 경우에는 idx를 1 증가시켜 다음 원소를 비교하게 함
  
---

## LeetCode 3248 (Remove Duplicates from Sorted Array)

:pushpin: 유형
* 배열

:question: 문제
* num(정렬된 상태)의 중복되는 원소값을 제거한 후, nums 길이 반환

:heavy_check_mark: 해결
* idx는 현재 nums의 인덱스를 가리킴
* idx와 idx+1번째 원소가 같은지를 비교하므로 len(nums)-1만큼 반복
* 같으면 del, 다르면 idx+=1

>> sample
---  

## 백준 10156 (과자)
:pushpin: 유형
* 시뮬레이션

:question: 문제
* K: 과자 가격, N: 사려는 과자 개수, M: 현재 가진 돈
* 과자를 사려할 때 부모님한테 받아야 하는 돈 계산(부족할 때)

:heavy_check_mark: 해결  
* C연산을 행<->열을 통해 같은 R연산으로 해줌

:heavy_plus_sign: 추가
* 연산을 하면서 기존 열 개수 값을 바꿔버려 틀림
  => tmpCol을 만들어 연산이 끝날 때 열 개수를 바꿔 해결