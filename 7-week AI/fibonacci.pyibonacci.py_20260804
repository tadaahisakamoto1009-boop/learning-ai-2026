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

Week 1 Python実装課題1：フィボナッチ数列
2つの実装（再帰版とループ版）の比較

学び：
- 純粋関数として設計することで、副作用がなく(効率よく)検証可能
- 再帰版は同じ計算を繰り返すため、ループ版より大幅に遅い
- 「正しく動く」と「効率的に動く」は別問題
