# 행렬의 스칼라 곱

**난이도:** ★★
**문제 링크:** https://compilerun.vercel.app/problems/e4c64ba1-ac6b-4fbf-8271-7492cf6f5724

## 문제 지문

첫째 줄에 2×2 행렬의 원소 4개, 둘째 줄에 스칼라 k를 입력받아 모든 원소에 k를 곱한 행렬을 2줄로 출력하세요.

[입력] 첫째 줄: 정수 4개 / 둘째 줄: 정수 k
[출력]
(k배 행렬 1행)
(k배 행렬 2행)

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
k=v[4]
print(v[0]*k, v[1]*k)
print(v[2]*k, v[3]*k)
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int a[4], k;
    for (int i = 0; i < 4; i++) scanf("%d", &a[i]);
    scanf("%d", &k);
    printf("%d %d\n", a[0]*k, a[1]*k);
    printf("%d %d\n", a[2]*k, a[3]*k);
    return 0;
}
```

## 해설

스칼라 곱은 원소별 곱셈 한 번씩이면 됩니다.

_해결일: 2026-08-27_