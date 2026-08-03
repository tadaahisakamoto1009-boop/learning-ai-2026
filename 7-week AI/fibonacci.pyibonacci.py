再帰版
def fib_recursive(n):
    # まず「終了条件」を書く（n=0とn=1の場合）
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # 次に「再帰呼び出し」を書く（n≥2の場合）
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

display(fib_recursive(10))

ループ版
def fib_iterative(n):
    a, b = 0, 1
    results = []
    for i in range(n):
        results.append(a)
        a, b = b, a + b
        if i == 9: # Stop when n reaches 10 (index 9 for 0-based range)
            break
    return results

display(fib_iterative(10))
