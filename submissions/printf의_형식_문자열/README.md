# printf의 형식 문자열

**난이도:** ★
**문제 링크:** https://compilerun.vercel.app/problems/5a5856c4-eb7e-4ee8-bc00-00bb64976d6a

## 문제 지문

정수 123, 실수 5.95, 문자 B를 각각 변수에 저장한 뒤, 형식에 맞춰 아래와 같이 출력하세요. (실수는 소수점 둘째 자리까지)

[입력] 없음
[출력]
정수: 123
실수: 5.95
문자: B

## 내 정답 코드 (Python)

```python
print("정수: 123")
print("실수: 5.95")
print("문자: B")
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    int i = 123;
    float f = 5.95f;
    char c = 'B';
    printf("정수: %d\n", i);
    printf("실수: %.2f\n", f);
    printf("문자: %c\n", c);
    return 0;
}
```

## 해설

값을 문자열 틀에 끼워 출력하는 형식 지정 출력은 모든 언어에 존재합니다. C는 %d·%f·%c, 파이썬은 f-문자열을 사용합니다.

_해결일: 2026-08-28_