# 배열의 홀수 인덱스와 짝수 인덱스에 저장된 값의 합

**난이도:** ★★
**문제 링크:** https://compilerun.vercel.app/problems/b6748b05-0f47-452c-acf1-f745b60f3800

## 문제 지문

정수 10개를 입력받아 짝수 인덱스(0,2,4,…)에 저장된 값의 합과 홀수 인덱스(1,3,5,…)에 저장된 값의 합을 출력하세요.

[입력] 정수 10개 (공백 구분)
[출력]
짝수 인덱스 합: (값)
홀수 인덱스 합: (값)

## 내 오답 코드

```python
ㄷㅇㅇㅇㅇㅇㅇㅇ
```

## 내 정답 코드 (Python)

```python
arr = list(map(int, input().split()))
even_idx = sum(arr[i] for i in range(10) if i % 2 == 0)
odd_idx = sum(arr[i] for i in range(10) if i % 2 == 1)
print(f"짝수 인덱스 합: {even_idx}")
print(f"홀수 인덱스 합: {odd_idx}")
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int arr[10];
    int even = 0, odd = 0;
    for (int i = 0; i < 10; i++) {
        scanf("%d", &arr[i]);
        if (i % 2 == 0) even += arr[i];
        else odd += arr[i];
    }
    printf("짝수 인덱스 합: %d\n", even);
    printf("홀수 인덱스 합: %d\n", odd);
    return 0;
}
```

## 해설

87장(값 기준)과 달리 i % 2 로 분기합니다. 인덱스가 0부터 시작함에 주의하세요.

_해결일: 2026-11-21_