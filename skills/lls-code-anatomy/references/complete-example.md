# 完整示例：解剖一个列表推导式

## 输入代码

```python
items = [name.strip().lower() for name in raw_names if name.strip()]
```

## 事实、假设与未知

| 类型 | 内容 |
|---|---|
| 已知事实 | 代码遍历 `raw_names`，过滤空白字符串，再把保留项去掉首尾空白并转成小写 |
| 暂定假设 | `raw_names` 是只包含字符串的可迭代对象 |
| 仍然未知 | 谁调用这段代码、结果交给哪个模块、是否允许 `None` 或数字 |

## 记忆路线

`逐个取名字 → 先过滤纯空白项 → 清理首尾空白 → 转小写 → 收集成新列表`

## 解剖式注释

```python
# 遍历原始名字：跳过纯空白项，把保留项清理首尾空白并统一转成小写
items = [name.strip().lower() for name in raw_names if name.strip()]
```

| 片段 | 作用 | 输入 | 输出 | 常见误解 |
|---|---|---|---|---|
| `for name in raw_names` | 逐项遍历 | 可迭代对象 | 当前元素 `name` | 不是一次处理整个列表 |
| `if name.strip()` | 过滤纯空白项 | 当前字符串 | 真或假 | 会额外调用一次 `strip()` |
| `name.strip().lower()` | 清理并转小写 | 被保留的字符串 | 新字符串 | 小写转换不等于去重 |

## 书写顺序与运行顺序

书写时，结果表达式写在最左边；真实执行时却是：

1. `for name in raw_names` 取出当前元素；
2. `if name.strip()` 判断是否保留；
3. 只有保留时才执行 `name.strip().lower()`；
4. 把结果加入新列表；
5. 对下一个元素重复。

因此，保留项的 `strip()` 会调用两次，纯空白项调用一次。元素若为 `None` 或数字，会因为没有 `.strip()` 而报 `AttributeError`。

## 最难一行逐 token 解剖

- `items =`：把右侧创建的新列表绑定给 `items`。
- `[` `]`：列表推导式边界，最终产生一个新列表。
- `name.strip().lower()`：对通过过滤的当前字符串先清理首尾空白，再转成小写。
- `for name in raw_names`：依次把 `raw_names` 中的元素绑定给临时变量 `name`。
- `if name.strip()`：只有清理后仍为非空字符串的元素才保留。

最小等价写法：

```python
items = []
for name in raw_names:
    if name.strip():
        items.append(name.strip().lower())
```

## 预测—改动—运行

安全改动：把 `.lower()` 改成 `.upper()`。

待用户预测：输入包含 `" Alice "`、纯空格和 `"BOB"` 时，新列表会是什么？

实际验证命令：

```bash
python3 - <<'PY'
raw_names = [" Alice ", " ", "BOB", "\tCarol\n", "  dAvE  "]
lower_items = [name.strip().lower() for name in raw_names if name.strip()]
upper_items = [name.strip().upper() for name in raw_names if name.strip()]
print("lower:", lower_items)
print("upper:", upper_items)
PY
```

运行证据：

```text
exit code: 0
stdout:
lower: ['alice', 'bob', 'carol', 'dave']
upper: ['ALICE', 'BOB', 'CAROL', 'DAVE']
stderr: <empty>
```

## 通用模式

模式名称：过滤后映射。

```python
RESULT = [transform(ITEM) for ITEM in SOURCE if keep(ITEM)]
```

适用：每个输入元素都能独立判断和转换。
不适用：元素间存在前后依赖、转换有昂贵副作用，或错误需要逐项记录。

## 学习卡片

- 这是什么：一行完成“遍历、过滤、转换、收集”的列表推导式。
- 关键条件：`raw_names` 中的元素需要支持 `.strip()`。
- 最容易错：按字面从左到右理解运行顺序；忽略 `strip()` 重复调用；误以为 `lower()` 会去重。
- 我亲手改动：把 `lower()` 改成 `upper()`。
- 实际结果：保留项变成大写，过滤规则不变。

## 新术语与稍后学习

| 术语 | 一句话含义 | 最小例子 |
|---|---|---|
| 列表推导式 | 从可迭代对象过滤、转换并生成新列表 | `[x * 2 for x in nums]` |
| 真值测试 | 非空字符串为真，空字符串为假 | `bool("") is False` |
| 链式调用 | 前一个方法的返回值继续调用下一个方法 | `text.strip().lower()` |

稍后学习：海象运算符可避免某些重复计算，但会增加新手阅读成本，本轮不展开。

## 三道可判分自测题

1. 解释题：为什么 `if name.strip()` 的真实执行时机早于左侧的 `name.strip().lower()`？
   判分点：能说出列表推导式先遍历、再过滤、最后计算结果表达式。
2. 预测题：把输入改成 `[" A ", "", " a "]`，原代码输出什么？它会自动去重吗？
   判分点：输出 `["a", "a"]`，并明确不会去重。
3. 迁移题：写一个列表推导式，从 `raw_scores` 中保留非负数并全部乘以 100。
   判分点：包含遍历、`if score >= 0` 和 `score * 100`。
