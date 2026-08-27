# 대칭 행렬인지 판별하기

**난이도:** ★★★
**문제 링크:** https://compilerun.vercel.app/problems/4088188a-1d14-417d-bb1c-569dde257276

## 문제 지문

정수 n과 n×n 정수 행렬을 입력받아, 그 행렬이 **대칭 행렬**이면 `대칭`, 아니면 `비대칭`을 출력하세요.
대칭 행렬은 전치해도 자기 자신과 같은 행렬입니다.

[입력]
첫 줄에 n
다음 n줄, 각 줄에 n개의 정수

[출력]
`대칭` 또는 `비대칭`

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
n=v[0]
a=v[1:1+n*n]
ok=all(a[i*n+j]==a[j*n+i] for i in range(n) for j in range(n))
print("대칭" if ok else "비대칭")
```

## 모범 답안

```python
#include <stdio.h>
static int a[100][100];
int main(void)
{
    int n, i, j;
    scanf("%d", &n);
    for (i = 0; i < n; i++) for (j = 0; j < n; j++) scanf("%d", &a[i][j]);
    int sym = 1;
    for (i = 0; i < n && sym; i++)
        for (j = i + 1; j < n; j++)
            if (a[i][j] != a[j][i]) { sym = 0; break; }
    printf("%s\n", sym ? "대칭" : "비대칭");
    return 0;
}
```

## 해설

대칭이라는 것은 모든 칸에서 `a[i][j] == a[j][i]`라는 뜻입니다. **전치 행렬을 실제로 만들 필요가 없습니다** — 정의를 그대로 조건으로 쓰면 됩니다. 게다가 `j > i`인 위쪽 절반만 확인해도 충분합니다(아래 절반은 같은 비교의 반복).

_해결일: 2026-08-27_