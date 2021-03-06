## 인프런 문제 3 (섬으로 건너가라!)
:pushpin: 유형
* 시간연산

:question: 문제
* 한 배에 탈 수 있는 인원이 정시 25명, 10분마다 15명
* 배는 매일 9시부터 21시 전까지 10분 단위로 들어옴 (9시 미포함)
* 1월은 1024일, 2월은 512일, 3월은 256일, 4월은 128일, 5월은 64일, 
  6월은 32일, 7월은 16일, 8월은 8일, 9월은 4일, 10월은 2일
* 시간 개념은 동일
* 배에 타는 순간 자바독이 화장실이 급해 현재 시간에 '분'만큼 배 출발이 늦어짐
* 입력받은 인원수 다음 두 명이 라이캣과 자바독의 탑승 차례임
* 라이캣과 자바독이 배에 타는 날짜를 구하기 (둘이 같은 배를 타야 함)

:heavy_check_mark: 해결
* 정각에는 +25, 10분마다 +15 -> 1시간에 100명
* 12시간이면 1200명 -> 하루에 1200명까지 탑승 가능
* 출발 년도 : 대기인원//1200(하루수용 인원)//일년 총 일수
* 출발 월 : 년도를 구하고 남은 일수가 어느 달에 포함되는지 체크
* 출발 일 : 남은 일수 - (출발 월-1)월의 누적 일수
* 출발 시간 : 대기 인원 % 1200 // 100(한 시간 수용 인원) + 9(시작 시간)
* 출발 분 : 남은 대기 인원 + 1과 +2가 탈 수 있는 분을 구함 
  -> 해당 시간의 마지막 배이면 다음 시간의 배로 바꿔줌
  -> 현재 시간에서 분을 더한 값이 시간을 넘어가면 처리해줌
  
---

## 백준 2644 (촌수계산)
:pushpin: 유형
* bfs

:question: 문제
* 사람 수 n
* 촌수를 계산해야 하는 두 사람 a, b
* 부모, 자식들 간의 관계 개수 m
* 부모-자식간의 관계 x, y (x가 부모)
* 두 사람의 친척관계가 없어 촌수 계산이 불가능한 경우 -1 출력

:heavy_check_mark: 해결
* rel 배열에 각 사람의 연결 관계 저장
* a부터 시작해서 bfs 실행
  -> deque에 a를 넣고 빌 때까지 실행
  -> 왼쪽 원소를 뽑아 해당 원소와 연결된 방문 안 한 사람을 deque에 저장
  -> result 배열에 방문한 사람의 촌수 관계를 현재 사람의 result값 + 1로 저장
* result[b]의 값이 0이 아니면 연결된 관계이므로 출력, 아니면 -1 출력
  
---

## 백준 7569 (토마토)
:pushpin: 유형
* bfs

:question: 문제
* 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토는 익게 됨 (위, 아래, 왼, 오, 앞, 뒤)
* -1 : 토마토 X, 0 : 익지 않음, 1 : 익음
* 며칠이 지나면 다 익게 되는지 최소 일수를 알고 싶음

:heavy_check_mark: 해결
* 익은 토마토를 저장
* 여섯 방향에 대해서 익지않은 토마토가 있는 곳에 기존 토마토+1을 하고 큐에 저장
* 큐가 빌 때까지 반복
* 안 익은 토마토가 존재하면 -1 출력, 아니면 box의 최댓값-1을 출력 (기존 토마토가 1이라서)

:heavy_plus_sign: 추가
* 3중 배열을 계속 돌면서 deque에 방문 가능한 토마토가 없을 때까지  실행 -> runtime error
* 기존 bfs를 실행해 bfs 안에서 다음 토마토에 대한 익히는 행동을 실행 -> 재귀 수 초과 recursion error
* box에다가 기존 수에 +1을 누적해서 저장하면 총 일수를 알 수 있음
  
---

## 백준 2178 (미로찾기)
:pushpin: 유형
* bfs

:question: 문제
* 1은 이동할 수 있는 칸, 0은 이동 불가능
* 1, 1에서 출발하여 N, M의 위치로 이동할 때 지나야 하는 최소 칸 수를 출력
* 항상 도착 위치에 이동할 수 있는 경우가 주어짐


:heavy_check_mark: 해결
* 0, 0을 큐에 넣고 이동가능한 위치이면 현재값+1 해서 maze에 저장
* bfs 실행 후 maze[n-1][m-1]에 최소값이 저장되어 있음
  
---