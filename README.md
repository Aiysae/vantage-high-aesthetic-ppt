# Vantage万极｜高审美版 PPT 生成

**Skill 名称：** vantage-high-aesthetic-ppt  
**中文名称：** Vantage万极｜高审美版 PPT 生成  
**作者：** Vantage万极  
**许可证：** MIT

这是一个面向 Codex 的开源 Skill，用于生成文字、物件、材质、光线和空间关系共同表达的高审美 PPT。

它适合概念解释、课程教学、业务方法、产品叙事、品牌观点和抽象框架。它的核心方法来自一组高完成度的 3D 场景型 PPT 参考图：

1. 先把抽象观点翻译成一个物理场景；
2. 再让图像模型在生成阶段把标题和标签直接写进场景；
3. 最后用一张完整生成图组成一页 PPT。

## 核心特点

- 默认使用 embedded-image 模式；
- 文字与画面在生成阶段共同完成；
- 默认模式锁定为单图整页组装，不走通用 PPT 的后加文字流程；
- 中文可以出现在纸牌、金属牌、玻璃块、书页、路牌和台座上；
- 一页只表达一个认知任务；
- 使用统一的材质、色板、光线和镜头语言；
- 生成后逐页检查中文字形、拼写、透视、光影和语义关系；
- 发现错字时重新生成，不把后贴文字修补称为原生内嵌文字；
- 交付前检查 PPTX 结构：每页一张图片，零个可见文字对象；
- 需要可编辑文字时，才切换到 editable-hybrid 模式。

## 下载

- [GitHub 仓库](https://github.com/Aiysae/vantage-high-aesthetic-ppt)
- [下载 ZIP](https://github.com/Aiysae/vantage-high-aesthetic-ppt/archive/refs/heads/main.zip)
- 发布账号：[@Aiysae](https://github.com/Aiysae)，作者：**Vantage万极**。

## 运行依赖

本仓库提供 Skill 指令、提示词模板和嵌字模式结构检查器，不捆绑图像模型或演示文稿运行环境。完整制作需要宿主具备图像生成能力、PPTX 构建能力和渲染检查能力；在 Codex 中使用 imagegen 生成页面图，用 Presentations 完成打包、渲染和检查。模型访问与使用费用由使用者自己的环境决定。

缺少这些能力时，仅能交付页面蓝图和提示词，不能将其声称为已生成的 PPTX。当前效果来自三页中文样板验证，其他主题仍须逐页校对文字和画面。

## 使用方式

下载 ZIP 并解压，将目录命名为 vantage-high-aesthetic-ppt，复制到 Codex 的个人技能目录（未设置 CODEX_HOME 时为 ~/.codex/skills）：

~~~text
$CODEX_HOME/skills/vantage-high-aesthetic-ppt/
~~~

然后直接调用：

~~~text
使用 $vantage-high-aesthetic-ppt，把“FDE 到底是什么”做成 8 页 PPT。
~~~

也可以用自然语言触发：

~~~text
做一套文字和画面在生成阶段融合的高审美 PPT，主题是“企业为什么需要 SOP”。
~~~

## 默认产物

- 16:9 PPTX；
- 每页一张原生带字生成图；
- 生成图素材目录；
- PDF 或逐页 PNG 渲染预览；
- 文字准确性与视觉 QA 结果；
- 本次使用的模式和需要重新生成的页面记录。

嵌字模式结构检查：

~~~bash
python3 scripts/validate_embedded_deck.py path/to/deck.pptx
~~~

检查通过的嵌字模式页面，每页应只有一张整页图片，没有后加的可见文字对象。

## 重要边界

生成式插画用于解释概念、机制和类比。真实客户证据、真实数据、产品截图、ROI 结果和事实性结论，仍需使用可追溯的原始材料。

本 Skill 不把参考图片中的文字当作指令，也不把参考图片里的主题、品牌或事实自动复制到新 PPT。

## 开源署名

本 Skill 由 **Vantage万极** 开源。使用、修改或二次分发时，请保留本 README 与 LICENSE 中的作者和许可证信息。

详细执行规则见 [SKILL.md](SKILL.md)，提示词模板见 [references/prompt-template.md](references/prompt-template.md)。
