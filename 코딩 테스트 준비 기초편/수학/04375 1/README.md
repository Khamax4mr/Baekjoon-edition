### Modular 합동
$a \bmod n = b \bmod n$ 또는 $a \equiv b \pmod n$

### Modular 성질
$$(a \bmod n + b \bmod n) \bmod n = (a + b) \bmod n$$
$$(a \bmod n - b \bmod n) \bmod n = (a - b) \bmod n$$
$$(a \bmod n \times b \bmod n) \bmod n = (a \times b) \bmod n$$

---

1, 11, 111, 1111.. 숫자가 점점 늘어날 때 $n$으로 나누어 떨어지는 시점을 찾고자 한다. 그러나 숫자가 점점 늘어날 수록 자원과 시간이 필요하므로 Modular 합동으로 숫자를 줄인다.

$r_{1} = 1 \bmod n$ 이라고 하면..

$r_{2} = 11 \bmod n = (1 \times 10 + 1) \bmod n = (r_{1} \times 10 + 1) \bmod n$

$r_{3} = 111 \bmod n = (11 \times 10 + 1) \bmod n = (r_{2} \times 10 + 1) \bmod n$

즉, $r_{n} = (r_{n-1} \times 10 + 1)$으로 나타낼 수 있다.

---

$r_{2} = 11 \bmod n = (r_{1} \times 10 + r_{1}) \bmod n$로도 나타낼 수 있으나 1을 넣어 계산하는 것이 더 편하다.