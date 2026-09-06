# 质量门禁

## 三重验证

每个方法单元必须同时通过：

1. **跨段支持**：至少两处独立证据，不能是一句话的不同改写；
2. **预测能力**：能指导一个原文未直接回答的新情境；
3. **独特价值**：比“要努力、要复盘、用户很重要”等常识更具体。

## 测试题最小集合

```json
{
  "skill": "generated-skill-slug",
  "cases": [
    {"type": "should_trigger", "prompt": "真实任务", "expected_behavior": "应执行的动作"},
    {"type": "should_not_trigger", "prompt": "相似但不适用的任务", "expected_behavior": "说明不调用原因"},
    {"type": "edge_case", "prompt": "边界任务", "expected_behavior": "先检查哪项条件"}
  ]
}
```

至少 3 条 `should_trigger`、2 条 `should_not_trigger`、1 条 `edge_case`。有兄弟 Skill 时，不触发题至少包含一条兄弟 Skill 场景。

## 结果判定

- 不触发题容错为 0：发生串岗就回炉修改 `description` 或边界；
- 触发题不仅要选中 Skill，还要按方法步骤产生有用结果；
- 边界题必须先检查条件，不能直接套模板；
- 同会话自测要明确标注，独立新会话测试的证据等级更高。

## 发布门禁

- 不含完整受限原文、私人资料和本机绝对路径；
- 来源与改编记录完整；
- Skill 在 WorkBuddy 安装目录中读回成功；
- 新会话至少完成一正一反两条触发检查；
- GitHub、飞书和 SkillHub 分别做发布后读回。
