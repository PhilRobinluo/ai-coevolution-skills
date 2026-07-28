# 完整示例：理解一个折扣计算函数

## 输入代码

```python
def final_price(price, discount=0):
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return round(price * (1 - discount), 2)
```

## 记忆路线

`接收价格和折扣 → 校验折扣范围 → 计算剩余比例 → 保留两位小数`

## 数据流地图

- 谁调用它：结算或报价逻辑。
- 输入：原价 `price` 和 0 到 1 之间的折扣 `discount`。
- 中间处理：先检查折扣，再计算 `price * (1 - discount)`。
- 输出：保留两位小数的最终价格。

## 最难一行逐 token 解剖

原句：

```python
if not 0 <= discount <= 1:
```

- `if`：只有条件成立时才进入下面的代码块。
- `not`：把后面的真假结果反过来。
- `0 <= discount <= 1`：Python 的链式比较，等价于 `0 <= discount and discount <= 1`。
- `:`：表示条件代码块从下一行开始。
- 整句人话：如果折扣不在 0 到 1 之间，就进入报错分支。

## 预测—改动—运行

安全改动：把测试输入从 `discount=0.2` 改成 `discount=1.2`。

先预测：函数会在计算价格前抛出 `ValueError`。

验证命令：

```bash
python3 - <<'PY'
def final_price(price, discount=0):
    if not 0 <= discount <= 1:
        raise ValueError("discount must be between 0 and 1")
    return round(price * (1 - discount), 2)

print(final_price(100, 0.2))
print(final_price(100, 1.2))
PY
```

预期观察：先输出 `80.0`，然后出现 `ValueError`。

## 通用模式

这是“先校验，再计算”的防御式函数：

```python
def transform(INPUT):
    if not is_valid(INPUT):
        raise ValueError("invalid input")
    return calculate(INPUT)
```

看到“外部输入会影响计算结果”时，应优先想到这个模式。

