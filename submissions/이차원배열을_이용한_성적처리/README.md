# 이차원배열을 이용한 성적처리

**난이도:** ★★★
**문제 링크:** https://compilerun.vercel.app/problems/cf7a158a-244a-4f54-ba2f-15378c940ea8

## 문제 지문

학생 3명의 3과목 점수를 세 줄로 입력받아, 각 학생의 총점과 평균(소수 1자리)을 출력하세요.

[입력] 세 줄, 각 줄에 정수 3개 (공백 구분)
[출력]
학생1 총점: (합), 평균: (소수 1자리)
학생2 총점: (합), 평균: (소수 1자리)
학생3 총점: (합), 평균: (소수 1자리)

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
s1=v[0]+v[1]+v[2]
s2=v[3]+v[4]+v[5]
s3=v[6]+v[7]+v[8]
f="학생%d 총점: %d, 평균: %.1f"
print(f % (1, s1, s1/3))
print(f % (2, s2, s2/3))
print(f % (3, s3, s3/3))
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int s[3][3];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            scanf("%d", &s[i][j]);
    for (int i = 0; i < 3; i++) {
        int total = s[i][0] + s[i][1] + s[i][2];
        printf("학생%d 총점: %d, 평균: %.1f\n", i + 1, total, total / 3.0);
    }
    return 0;
}
```

## 해설

행(학생)마다 열(과목)을 누적하는 이중 반복의 전형입니다.

_해결일: 2026-08-27_