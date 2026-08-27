# 3x3 행렬의 두 대각선 합

**난이도:** ★★★
**문제 링크:** https://compilerun.vercel.app/problems/fbdbed63-b955-4ceb-b581-da035e71b0e2

## 문제 지문

3행 3열의 정수 행렬을 입력받아 **주대각선의 합**과 **부대각선의 합**을 한 줄에 공백으로 구분해 출력하세요.
주대각선은 왼쪽 위에서 오른쪽 아래로, 부대각선은 오른쪽 위에서 왼쪽 아래로 가는 대각선입니다.

[입력]
3줄, 각 줄에 3개의 정수

[출력]
주대각선합 부대각선합

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
print(v[0]+v[4]+v[8], v[2]+v[4]+v[6])
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int a[3][3], i, j;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++) scanf("%d", &a[i][j]);
    int d1 = 0, d2 = 0;
    for (i = 0; i < 3; i++) { d1 += a[i][i]; d2 += a[i][2 - i]; }
    printf("%d %d\n", d1, d2);
    return 0;
}
```

## 해설

주대각선은 `i == j`인 칸, 부대각선은 `i + j == n - 1`인 칸입니다. **두 인덱스의 관계로 위치를 표현하는 것**이 2차원 배열을 다루는 핵심입니다. 반복문 하나로 두 합을 동시에 구할 수 있습니다.

_해결일: 2026-08-27_