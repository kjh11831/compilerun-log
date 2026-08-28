# float와 double

**난이도:** ★
**문제 링크:** https://compilerun.vercel.app/problems/48bdb9af-39a5-4220-aeb9-7672fd4af5f0

## 문제 지문

반지름 5.0인 원의 면적(원주율 3.14159265359)을 float형과 double형으로 각각 계산해, float 결과는 소수점 7자리, double 결과는 소수점 12자리로 출력하여 정밀도 차이를 확인하세요.

[입력] 없음
[출력]
원의 면적 (float): (float 계산 결과, 소수점 7자리)
원의 면적 (double): (double 계산 결과, 소수점 12자리)

## 내 오답 코드

```python
d
```

## 내 정답 코드 (Python)

```python
import struct
PI = 3.14159265359
r = 5.0
f = struct.unpack('f', struct.pack('f', struct.unpack('f', struct.pack('f', r))[0] * struct.unpack('f', struct.pack('f', r))[0] * struct.unpack('f', struct.pack('f', PI))[0]))[0]
d = r * r * PI
print(f"원의 면적 (float): {f:.7f}")
print(f"원의 면적 (double): {d:.12f}")
```

## 모범 답안

```python
#include <stdio.h>
int main(void)
{
    float rf = 5.0f, pf = 3.14159265359f;
    double rd = 5.0, pd = 3.14159265359;
    float areaF = rf * rf * pf;
    double areaD = rd * rd * pd;
    printf("원의 면적 (float): %.7f\n", areaF);
    printf("원의 면적 (double): %.12f\n", areaD);
    return 0;
}
```

## 해설

float는 약 7자리, double은 약 15자리의 유효숫자를 가집니다. 소수점 아래 깊은 자리에서 float의 오차가 드러납니다.

_해결일: 2026-08-28_