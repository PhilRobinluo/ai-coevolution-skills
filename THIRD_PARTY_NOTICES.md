# Third-Party Notices

## 范围

本仓库的默认分流许可证仅覆盖明确标注为 `lls-original` 的原创内容及其适用脚本。第三方内容、改编内容和社区推荐不因位于本仓库而被重新授权。

## Adapted

`adapted/<slug>/` 中的每个改编 Skill 必须保留 `ORIGIN.md`、上游许可证、版权声明、来源链接、上游版本/提交和本仓修改记录。其许可证以该目录的上游标注为准。

## Community

`community/` 默认只提供目录、中文说明和原仓库链接；`community/catalog.json` 记录来源、作者、许可证和核验信息。社区条目的源码不因目录收录而进入本仓默认许可范围。

## 外部许可证文本

- Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International：`LICENSES/CC-BY-NC-SA-4.0.txt`，来源 <https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode>。
- PolyForm Noncommercial License 1.0.0：`LICENSES/PolyForm-Noncommercial-1.0.0.txt`，来源 <https://polyformproject.org/licenses/noncommercial/1.0.0/>。

新增或更新第三方材料时，维护者必须更新本文件或对应 `ORIGIN.md`，并通过 `python3 tools/validate-provenance.py`。
