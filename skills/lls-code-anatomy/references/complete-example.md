# 完整示例：解剖一个列表推导式

## 输入代码

```python
items = [name.strip().lower() for name in raw_names if name.strip()]
```

## 事实、假设与未知

| 类型 | 内容 |
|---|---|
| 已知事实 | 代码遍历 `raw_names`，使用 `strip()` 的结果做过滤，并对保留项继续调用 `strip().lower()` |
| 暂定假设 | `raw_names` 是只包含字符串的可迭代对象 |
| 仍然未知 | 谁调用这段代码、结果交给哪个模块、是否允许 `None` 或数字 |

## 记忆路线

`逐个取名字 → 先过滤纯空白项 → 清理首尾空白 → 转小写 → 收集成新列表`

## 数据流地图

- 谁调用它：未知；需要用户补充所在函数或文件上下文。
- 输入是什么：暂按“只包含字符串的可迭代对象 `raw_names`”讲解。
- 中间做了什么：逐项遍历，用 `strip()` 过滤假值项，再对保留项执行 `strip().lower()`。
- 输出给谁：新列表绑定到变量 `items`；后续消费者未知。

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

- `items`：接收最终新列表的变量名。
- `=`：赋值运算符，把右侧计算结果绑定给左侧变量。
- `[`：开始一个列表推导式。
- `name`：当前遍历到的元素。
- `.`：属性访问运算符，表示到左侧对象上查找方法。
- `strip`：字符串方法名，用于移除首尾空白。
- `(` `)`：调用 `strip`，这里没有传参数。
- `.`：在 `strip()` 返回的新字符串上继续查找方法。
- `lower`：字符串方法名，用于返回小写版本。
- `(` `)`：调用 `lower`，这里没有传参数。
- `for`：开始列表推导式的遍历部分。
- `name`：每轮接收一个元素的临时变量。
- `in`：表示从右侧可迭代对象中逐项取值。
- `raw_names`：被遍历的输入对象。
- `if`：开始过滤条件。
- `name`：当前元素。
- `.`：到当前元素上查找方法。
- `strip`：再次查找字符串的首尾清理方法。
- `(` `)`：实际调用 `strip`；其返回值参与真值判断。
- `]`：结束列表推导式并生成列表。

符号关系：`for ... in ...` 决定元素来源，`if ...` 决定是否保留，最左侧表达式决定保留项如何转换，`[...]` 收集全部转换结果，最后由 `=` 绑定给 `items`。

整句人话：从 `raw_names` 里逐个取出名字，跳过清理后为空的项，把其他项清理并转成小写，组成一个新列表交给 `items`。

类比：像一条分拣传送带——`for` 负责上料，`if` 是质检门，左侧表达式是加工工位，方括号是成品箱。

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

## 完整学习卡片

### 基本信息

- 语言：Python
- 文件或模块：示例夹具
- 本次功能块：过滤并标准化名字列表
- 验证状态：已运行

### 这段代码解决什么问题

在“输入元素均为字符串”的假设下，它从 `raw_names` 中过滤纯空白项，并把保留项规范成去掉首尾空白的小写字符串。调用者与后续消费者仍未知。

### 带意图注释的代码

```python
# 跳过清理后为空的名字，把保留项统一清理并转成小写
items = [name.strip().lower() for name in raw_names if name.strip()]
```

### 最难一行

- 原句：`items = [name.strip().lower() for name in raw_names if name.strip()]`
- 逐 token 解剖：见上文“最难一行逐 token 解剖”。
- 整句人话：遍历、过滤、转换并收集字符串。
- 最小等价写法：见上文普通 `for` 循环版本。
- 类比：传送带上料、质检、加工、装箱。

### 我预测并亲手改动的地方

- 修改前：保留项调用 `.lower()`。
- 我的预测：改成 `.upper()` 后，过滤结果数量不变，字母变成大写。
- 修改内容：`.lower()` → `.upper()`。
- 运行命令：见上文 heredoc 命令。
- 实际结果：得到 `['ALICE', 'BOB', 'CAROL', 'DAVE']`。
- 预测与实际的差异：一致。

### 通用模式

- 模式名称：过滤后映射。
- 适用信号：每个元素可独立过滤和转换。
- 通用骨架：`[transform(item) for item in source if keep(item)]`。
- 不适用场景：元素间有前后依赖、转换含昂贵副作用、需要逐项记录错误。

### 新术语

| 术语 | 一句话含义 | 最小例子 |
|---|---|---|
| 列表推导式 | 从可迭代对象过滤、转换并生成新列表 | `[x * 2 for x in nums]` |
| 真值测试 | 非空字符串为真，空字符串为假 | `bool("") is False` |
| 链式调用 | 前一个方法的返回值继续调用下一个方法 | `text.strip().lower()` |

### 稍后学习

- 本轮暂未展开：海象运算符可避免某些重复计算。
- 建议触发条件：用户已熟悉普通列表推导式，并希望只计算一次 `strip()`。

### 运行证据

- 实际命令：见上文 `python3` heredoc。
- 退出码：`0`。
- stdout：`lower` 与 `upper` 两个列表均符合预测。
- stderr：空。
- 证据状态：已验证。

### 三道可判分自测题

1. 解释题：为什么 `if name.strip()` 的真实执行时机早于左侧的 `name.strip().lower()`？
   判分点：能说出列表推导式先遍历、再过滤、最后计算结果表达式。
2. 预测题：把输入改成 `[" A ", "", " a "]`，原代码输出什么？它会自动去重吗？
   判分点：输出 `["a", "a"]`，并明确不会去重。
3. 迁移题：写一个列表推导式，从 `raw_scores` 中保留非负数并全部乘以 100。
   判分点：包含遍历、`if score >= 0` 和 `score * 100`。

### 下一次复习

- 需要复习的误区：书写顺序不等于运行顺序；`lower()` 不去重；元素类型必须支持 `.strip()`。
- 一个最小练习：把逻辑重写成只调用一次 `strip()` 的普通 `for` 循环，并为 `None` 输入设计处理策略。
