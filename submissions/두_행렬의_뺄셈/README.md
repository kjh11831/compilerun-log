# 두 행렬의 뺄셈

**난이도:** ★★★
**문제 링크:** https://compilerun.vercel.app/problems/dbae6aaa-9d8c-4dd1-9aaf-19d84cfa5d8b

## 문제 지문

행의 수 n과 열의 수 m을 입력받고, n×m 정수 행렬 두 개를 차례로 입력받아 **첫 행렬에서 둘째 행렬을 뺀 결과**를 출력하세요.
각 행은 한 줄에 출력하고, 값 사이는 공백 하나로 구분합니다.

[입력]
첫 줄에 n m
다음 n줄: 첫째 행렬
다음 n줄: 둘째 행렬

[출력]
n줄의 결과 행렬

## 내 정답 코드 (Python)

```python
import sys
v=list(map(int,sys.stdin.read().split()))
n=v[0]
m=v[1]
a=v[2:2+n*m]
b=v[2+n*m:2+2*n*m]
d=[a[i]-b[i] for i in range(n*m)]
print("\n".join(" ".join(map(str,d[i*m:(i+1)*m])) for i in range(n)))
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int n, m, i, j;
    static int a[100][100], b[100][100];
    scanf("%d %d", &n, &m);
    for (i = 0; i < n; i++) for (j = 0; j < m; j++) scanf("%d", &a[i][j]);
    for (i = 0; i < n; i++) for (j = 0; j < m; j++) scanf("%d", &b[i][j]);
    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (j) printf(" ");
            printf("%d", a[i][j] - b[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

## 해설

행렬의 덧셈·뺄셈은 **같은 자리끼리** 계산합니다(곱셈과 달리 행/열을 섞지 않습니다). 그래서 이중 반복문 하나로 끝나고, 두 행렬의 크기가 같아야만 정의됩니다. 출력할 때 **줄 끝에 공백이 남지 않도록** 주의하세요.

_해결일: 2026-08-27_