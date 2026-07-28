---
name: lls-document-print-restorer
description: "把仍可辨认的纸质文件照片保守增强、规范排版成 A4 PDF，并保留输入哈希、处理参数、预览和人工核对记录。用于表格、票据、手写页或旧文档偏灰、轻微模糊、方向错误、边距不适合打印时；只改善可见内容，不猜测或重造缺失文字、数字、签名、公章和法律证据。"
license: CC-BY-NC-SA-4.0
metadata:
  short-description: 保守增强可见内容并生成可复核 A4 打印版
---

<!-- workbuddy-install: published; slug: lls-document-print-restorer -->
## 在 WorkBuddy 中找到并安装

**Skill slug：`lls-document-print-restorer`**

在 WorkBuddy 新会话粘贴：

```text
请按 https://skillhub.cn/install/skillhub.md 检查 SkillHub，搜索 `lls-document-print-restorer`；仅在 slug 完全一致时安装到 `~/.workbuddy/skills/`。安装后读取 `~/.workbuddy/skills/lls-document-print-restorer/SKILL.md`，核对 name、version 和实际路径，然后新开会话触发该 Skill。
```

也可以打开左侧「技能」→「添加技能 / 查找技能」，搜索 `lls-document-print-restorer` 后安装；界面文字可能随 WorkBuddy 版本变化。

# 罗老师纸质文件打印修复助手

## 边界先说清

本 Skill 做的是“让原本可见的内容更适合阅读和打印”，不是恢复不存在的信息。

允许：方向纠正、保守对比度、轻度锐化、白底 A4 排版、预览和报告。

排除：补写缺字、重绘签名、公章、证件纹理，改变数字，拼接法律证据，声称恢复了无法辨认的原文。

## 必要输入

```text
原始照片：
文件类型和用途：个人阅读 / 普通打印 / 归档参考 / 正式提交
纸张方向：自动 / 竖向 / 横向
是否必须保留颜色：
关键核对字段：金额、日期、编号、签名等
输出 PDF、预览和报告路径：
隐私与本地处理要求：
```

正式提交或证据场景优先咨询相应机构对扫描件、复印件和修复件的接受标准。

## 一、先评估输入

分别标记：

- 清晰：笔画边界稳定，可直接增强；
- 偏灰：背景与文字对比不足；
- 阴影：局部明暗不均；
- 透视：页面四角不平行；
- 运动模糊：字符拖影；
- 过曝/欠曝：细节已经截断；
- 裁切缺失：边缘文字不在照片中；
- 遮挡/折痕：原始内容不可见。

后四类无法通过“增强”可靠补回，应重新拍摄或向原文件来源索取副本。

## 二、决定重拍还是处理

优先重拍的条件：

- 关键数字无法逐字符识别；
- 页面缺角或被手指遮挡；
- 反光覆盖正文；
- 透视严重到行列变形；
- 签名、印章或编号将用于正式用途。

重拍建议：平行页面、均匀散射光、避免数码变焦、四角全部入镜、用最高原始分辨率保存。

## 三、保留原件与输入指纹

不覆盖原图。把原图放在只读 `source/`，处理结果放到 `output/`，报告放到 `qa/`。

脚本会记录输入和输出 SHA256，便于证明处理对象与产物对应，但哈希不证明内容法律效力。

## 四、生成 A4 PDF

```bash
python3 scripts/make_a4_pdf.py   source/form-photo.jpg   output/form-a4.pdf   --orientation auto   --margin-mm 12   --contrast 1.12   --sharpness 1.08   --preview qa/form-a4-preview.png   --report qa/form-a4-report.json
```

脚本会：

1. 按 EXIF 纠正手机方向；
2. 使用有限范围的对比度与锐度；
3. 等比例缩放到 300 DPI A4 页面；
4. 居中并保留指定毫米边距；
5. 生成 PDF、可视预览和 JSON 报告。

目标存在时默认停止；`--force` 会先把旧目标改名备份。

## 五、人工核对关键内容

原图与预览并排，以字符为单位核对：

- 姓名、日期、金额、编号；
- 小数点、负号、斜杠；
- 表格行列对应关系；
- 手写改动、签名和印章位置；
- 页面是否完整、方向是否正确。

看不清的字符标记 `[不可辨认]`，不要依上下文自动补全。

## 六、打印前检查

- PDF 页面尺寸为 A4；
- 打印对话框选择“实际大小”或确认缩放策略；
- 最小文字在纸上可读；
- 边缘没有被打印机不可打印区域裁掉；
- 彩色信息没有因黑白打印丢失含义；
- 试打一页并与原图核对。

## 输出格式

1. 输入质量分级与重拍判断；
2. 处理参数和执行命令；
3. A4 PDF 与预览路径；
4. 输入/输出 SHA256 报告；
5. 关键字段逐项核对表；
6. 不可辨认、未处理和正式用途风险。

## 失败处理

- 输入打不开：保留原文件并报告格式，不自动转存覆盖。
- 处理后笔画出现光晕：降低 sharpness 和 contrast，重新从原图生成。
- 阴影严重：优先重拍；局部算法处理需另行验证，不假装本脚本已解决。
- PDF 太大：先保留无损主版本，再为传输生成副本。
- 输出已存在：更换文件名，或显式 `--force` 并保留备份。
- 关键字符仍不清楚：标记不可辨认并停止推断。

## 质量门禁

- [ ] 原图未被覆盖，输入哈希已记录；
- [ ] 已区分可增强问题与不可恢复信息；
- [ ] 对比度、锐度和边距参数在报告中可复核；
- [ ] 图像未拉伸，方向和页面尺寸正确；
- [ ] 关键数字、日期、编号逐字符与原图核对；
- [ ] 无法辨认的内容没有被猜测补写；
- [ ] PDF 通过预览和实际打印尺寸检查；
- [ ] 正式提交用途保留原始文件并标明处理版本；
- [ ] 票据、签名和个人资料默认本地处理；
- [ ] 产物、预览、报告和风险说明一并交付。

核对表见 [references/restoration-qa.md](references/restoration-qa.md)。

## 使用入口

- [飞书中文教程](https://m2wlgni9k4.feishu.cn/wiki/J6KLwLfvAiemc2kXss0cjOVmnnd)
- [SkillHub 安装页](https://skillhub.cn/skills/lls-document-print-restorer)
- [GitHub 源码](https://github.com/PhilRobinluo/ai-coevolution-skills/tree/main/skills/lls-document-print-restorer)
- [GitHub 1.1.0 安装包](https://github.com/PhilRobinluo/ai-coevolution-skills/releases/download/lls-document-print-restorer-v1.1.0/lls-document-print-restorer-1.1.0.zip)
