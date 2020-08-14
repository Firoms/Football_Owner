Football Owner
==============
---
GUI, DB를 중심으로 한 Football Owner 게임입니다. (FM을 모티브로 만듬)
--------------------------------------------------------------------
---
### 0. 준비사항
* 선수 데이터 수집   
  - API 이용   
  - Crawling 이용   
     
  두개 다 시도해 본 결과 Crawling을 이용해서 얻은 데이터가 더 많아 Crawling 사용하기로 함
* GUI 베이스 제작
* GUI 화면 디자인
---

### 1. 기초
* 구단주 이름 받기
* 초반 자금 설정
* 초반 팀 인수
---
### 2. 시스템
* 경기 결과 시뮬레이터
* 시즌 시뮬레이터
* 대회별 상금 & 스폰서 수익
* 선수별 능력치 / 잠재능력
* 팀 명성
* 선수 가치 업데이트
---
### 3. 플레이어
* 구단 인수 & 매각 기능
* 감독 / 스태프 선임 & 경질
* 선수 영입 & 재계약
* 스폰서 관리
* 아이템 사용
---
### 4. 이벤트
* 부상 상황
* 선수 영입 제안 & 매각 제안
* 타 구단주의 팀 인수 제안
* 경기 진행
* 플레이어에게 조언 해 주는 캐릭터
* 인터뷰
* 선수 재계약 제안
* 선수 가치 및 능력 관련 이벤트
---
### 5. Data Base
* 선수 
* 팀 
* 리그 
* 코치 
* 스태프
* 플레이어
* 이벤트 저장
* 현재 상황 저장   
   
  저장 방식 : 자동저장 파일로 게임 진행 & 저장 시 자동 저장파일을 1, 2번 저장파일에 저장
---
### 6. 고려해볼 사항
* 선수 사진 추가
* 경기 내용 표현
* 팀별 특성
---



## 게임 진행 방식

### 경기
각 팀은 기회를 20번 부여받는다.   
기회를 골로 성공시키기 위해서는 찬스메이킹에 성공하고 골을 성공시키는 과정이 필요하다   
> 찬스메이킹
>> * 두팀 간 수비수 & 미드필더의 능력치 합의 차이를 구한 후   
>> 50% +- 해서 찬스메이킹 확률을 부여한다   
>> ---
>> * 공격수 능력치 합/100 + 1% 확률로 PK를 얻는다   
>> (PK는 70 % 확률로 성공하게 된다.)   
>> ---
>> * 키퍼/10 + 1% 의 확률로 슈퍼세이브를 한다   
>---
> 골 확률   
>> * 수비수 & 키퍼x2 와 공격수 & 미드필더의 능력치 합의 차이 + 10% 확률로 골이 들어간다   
>> ---
>> * 단, 2%의 확률로 VAR이 발동하여 골이 무효가 된다.

---

### 선수 선발
전체 선수중   
14107명이 공격수   
18097명이 미드필더   
17786명이 수비수   
6307명이 골키퍼   
이기 때문에 전체선수의 비율을 고려하여   
공격수 3명 (교체 1명)   
미드필더 3명 (교체 2명)   
수비수 4명   
골키퍼 1명   
이 능력치 순으로 자동 선발된다.   

---

### 선수 스텟
|  | 공격수 | 미드필더 | 수비수 | 골키퍼 |
|---|:---:|:---:|:---:|:---:|
| 골 | 능력치 x 1 | 능력치 x 1/3 | 능력치 x 1/8 | 능력치 x 1/100 |
| 어시스트 | 능력치 x 1 | 능력치 x 1 | 능력치 x 1/2 | 능력치 x 1/50 |   

다음과 같은 비율로 확률을 조정하여 랜덤으로 골과 어시스트를 한 선수가 정해진다

---

### 능력치 변화
> 능력치가 90 이상인 경우   
>> 승리 시   
>>> 하락 1 그대로 18 증가 0 의 확률로 조정   
>> 패배 시   
>>> 하락 3 그대로 16 증가 0 의 확률로 조정   
> ---
> 능력치가 80 이상인 경우   
>> 승리 시   
>>> 하락 1 그대로 18 증가 1 의 확률로 조정   
>> 패배 시   
>>> 하락 3 그대로 16 증가 0 의 확률로 조정   
> ---
> 능력치가 70 이상인 경우   
>> 승리 시   
>>> 하락 1 그대로 18 증가 2 의 확률로 조정   
>> 패배 시   
>>> 하락 3 그대로 16 증가 1 의 확률로 조정   
> ---
> 능력치가 60 이상인 경우   
>> 승리 시   
>>> 하락 1 그대로 18 증가 4 의 확률로 조정   
>> 패배 시   
>>> 하락 3 그대로 16 증가 2 의 확률로 조정   
> ---
> 능력치가 50 이상인 경우   
>> 승리 시   
>>> 하락 1 그대로 18 증가 8 의 확률로 조정   
>> 패배 시   
>>> 하락 3 그대로 16 증가 4 의 확률로 조정   
> ---
> 능력치가 40 이상인 경우   
>> 승리 시   
>>> 하락 1 그대로 18 증가 16 의 확률로 조정   
>> 패배 시   
>>> 하락 3 그대로 16 증가 8 의 확률로 조정   
