---
name: folk-tale
description: 民间故事创作助手，专注怪谈、传说、志怪、奇谈、寓言等民间叙事体裁；本技能用于创作新故事，重述经典见 classic-folk-story。支持短篇（1-2万字）、中篇（2-5万字）、长篇（~10万字）三种篇幅。默认采用莫言式民间故事风格——说书人叙述、魔幻现实、乡土气息浓郁。故事可融合恐怖、惊悚、香艳元素。Use when the user wants to write folk tales, ghost stories, legends, supernatural tales, fables, or Chinese folklore-inspired narratives. Triggers on requests like "写民间故事", "怪谈", "传说", "志怪", "寓言", "鬼故事", "奇谈", "聊斋", "民间传说", "folk tale", "ghost story", "legend", "fable", "supernatural tale", "写一个恐怖故事", "乡村怪事".
---

# Folk Tale Writer

民间故事创作技能，覆盖从构思到成稿的完整工作流。扎根中国民间叙事传统（聊斋志异、搜神记、子不语、阅微草堂笔记），融合现代叙事技法。

**路径说明：** 本技能内所有 `references/` 路径均相对于本 skill 根目录（即 `folk-tale/`）。

## 默认风格

本技能默认采用**莫言式民间故事风格**——说书人叙述框架、魔幻现实笔触、浓烈的乡土感官。详细风格卡见 [references/style/moyan-folk.md](references/style/moyan-folk.md)。

可选风格：**东野圭吾式**——冷静精密、信息控制、叙述性诡计、真相反转。适合"鬼故事的真相其实是人的故事"这类民间悬疑。详细风格卡见 [references/style/higashino.md](references/style/higashino.md)。两种风格也可混合使用（莫言的氛围 + 东野的结构）。

用户可要求调整风格（如"写得像聊斋"、"要现代都市感"），此时根据需求修改或重建风格卡。

## 创作工作流

根据篇幅选择路径：

**短篇（1-2万字）：**
1. 确认故事核 → 2. 快速设定（步骤2的精简版：只做地理空间、时间锚点、超自然规则与民俗底色中的核心几条）→ 3. 章节划分（3-6章）→ 4. 逐章写作 → 5. 通读修订 → **7. 创建 novel-editor-runner subagent 并执行评测（必做）**

**中篇（2-5万字）：**
1. 构思定位 → 2. 世界设定 → 3. 角色设计 → 4. 情节架构（8-15章） → 5. 逐章写作 → 6. 修订润色 → **7. 创建 novel-editor-runner subagent 并执行评测（必做）**

**长篇（~10万字）：**
1. 构思定位 → 2. 世界设定 → 3. 角色设计 → 4. 情节架构（25-40章） → 5. 逐章写作 → 6. 修订润色 → **7. 创建 novel-editor-runner subagent 并执行评测（必做）**
- 长篇额外要求：建立设定追踪文档，每5章回顾一致性

**局部协作（已有素材）：**
- 已有大纲 → 直接逐章写作
- 已有初稿 → 直接修订润色
- 只需灵感 → 按需进入任意步骤

## 步骤 1：构思定位

与用户确认以下要素（未提供的主动询问）：

- **子类型**：怪谈 / 传说 / 志怪 / 奇谈 / 寓言 / 复合型。寓言读取 [references/types/fable.md](references/types/fable.md)；复合型按用户指定的类型组合读取多个类型参考文件。
- **一句话故事核**：25字以内概括核心悬念（如"村里的哑巴媳妇死后第七天开口说话了"）
- **时代背景**：古代 / 民国 / 当代 / 架空（影响语言和设定）
- **地域根基**：北方乡村 / 南方水乡 / 西南山地 / 沿海渔村 / 都市边缘…（影响方言、风俗、景观）
- **篇幅**：短篇（1-2万字）/ 中篇（2-5万字）/ 长篇（~10万字）
- **元素倾向**：恐怖惊悚 / 香艳旖旎 / 悲情苍凉 / 荒诞戏谑 / 复合
- **尺度**：暗示留白 / 适度展开 / 浓墨重彩
- **参考作品/风格**：如有 → 创建或调整风格卡

## 步骤 2：世界设定

民间故事的设定不追求系统化，追求"可信的在地感"：

### 必备设定
- **地理空间**：村庄/镇子的名字、地形地貌、标志性地点（古井、祠堂、老宅、河湾、坟地）
- **时间锚点**：用节气、农事、民俗节日标记时间（而非日期）
- **超自然规则**：这个世界里哪些"不可能的事"是可能的？规则不必系统化，但需内部一致
- **民俗底色**：婚丧嫁娶、禁忌信仰、方言俗语、饮食习惯

### 可选设定（中长篇）
- **家族谱系**：民间故事常跨代叙述，理清人物关系
- **地方志式背景**：有什么传说从祖辈传下来？本地有什么讲究和忌讳？
- **权力结构**：族长、地主、神婆、村长……谁说了算？

输出为结构化 Markdown 设定文档。

## 步骤 3：角色设计

民间故事角色有其独特原型体系：

### 常见原型
- **普通人**：老实巴交的农民/书生/猎户/渔夫——被卷入超自然事件
- **异类**：狐仙、蛇精、花妖、鬼魂——以人形出现，有自己的欲望和悲欢
- **通灵者**：神婆、道士、瞎眼老人、疯子——知道真相但不被人信
- **权威者**：族长、地主、县令——代表世俗秩序
- **叙述者**：讲故事的人——可以是"我爷爷"、村里长辈、说书人

### 角色卡模板
```
【角色名】
身份：一句话（如"渡口撑船的哑巴"）
辨识特征：2-3个（外貌、习惯、口头禅）
表面：别人眼中的他/她
底色：真实的欲望或秘密
与超自然的关系：见证者 / 当事人 / 通灵者 / 不信者
命运走向：一句话概括结局
说话方式：方言程度、话多话少、有无口头禅
```

短篇角色2-4人即可，中篇5-8人，长篇视需要扩展但核心角色控制在8人以内。

## 步骤 4：情节架构

根据故事类型选择叙事结构（详见结构参考文件）：

| 结构 | 适用 | 文件 |
|------|------|------|
| 说书人框架 | 最常用，口述体民间故事 | [references/structure/oral-frame.md](references/structure/oral-frame.md) |
| 故事套故事 | 多层嵌套叙事 | [references/structure/nested.md](references/structure/nested.md) |
| 单元连环式 | 长篇中多个独立故事串联 | [references/structure/episodic.md](references/structure/episodic.md) |

**大纲编写要点：**
1. 确定叙述框架（谁在讲这个故事？为什么讲？）
2. 标定"异变点"——正常世界和超自然的交汇时刻
3. 设计悬念链：每一章结尾留一个让人想继续的钩子
4. 安排元素节奏：恐怖/香艳/温情/荒诞的穿插，避免单一情绪疲劳
5. 拆分章节，每章标注：视角、场景概要、情绪走向、伏笔埋/收

### 章节规划参考

| 篇幅 | 章节数 | 每章字数 | 节奏特征 |
|------|--------|---------|---------|
| 短篇 1-2万字 | 3-6章 | 2000-4000字 | 紧凑，一条主线，快速进入异变 |
| 中篇 2-5万字 | 8-15章 | 2500-4000字 | 有铺垫空间，可有副线，氛围层层递进 |
| 长篇 ~10万字 | 25-40章 | 2500-4000字 | 多线交织或单元串联，有呼吸空间 |

## 步骤 5：逐章写作

### 写作前回顾
- 本章在大纲中的定位
- 上一章结尾的情绪和悬念状态
- 当前活跃的伏笔
- 风格卡（确保文风一致）

### 民间故事写作原则

**1. 说书人的口吻**
- 用"讲"的语气而非"写"的语气
- 可以插入说书人的议论（"你说怪不怪"、"这事儿到底是真是假，谁也说不清"）
- 叙述者的声音要统一：别一会儿文绉绉，一会儿大白话

**2. 超自然当日常写**
- 狐狸变成美人、死人托梦、井底有龙——用平淡的口吻叙述，不惊不怪
- 越是离奇的事，叙述语气越要平稳——"我奶奶说，那年冬天，河里的鱼都是倒着游的"
- 不解释超自然的科学原因，也不刻意渲染其神秘

**3. 感官浸入**
- 五感并用，嗅觉和触觉尤为重要（腐叶的潮气、灶台的焦糊味、粗布衫的触感）
- 用感官细节让虚幻变得逼真——读者在"闻到"、"摸到"的时候最容易相信
- 感官与情绪挂钩：恐惧写冷、欲望写热、哀伤写潮湿

**4. 节奏与呼吸**
- 恐怖和香艳段落不宜连续，中间要有日常生活的"呼吸"段落
- 日常段落不是废笔——炊烟、农活、邻里闲话本身就是民间故事的质地
- 高潮前放慢节奏（越慢越紧张），高潮时加快节奏（短句、快动作）

**5. 对话的乡土味**
- 农民说农民的话，不要文绉绉
- 适度使用方言词汇和俗语（但不要多到阻碍阅读）
- 异类（狐仙、鬼魂）的说话方式应有微妙区别——略带古意或略显不自然

**6. 修辞克制**
- 少用"不是……是……"句式和"像……"明喻，需要比喻时优先用暗喻或直接以具象细节替代
- 控制排比频率：偶尔一用增强势头可以，连续排比铺陈会滑向朗诵腔
- 拒绝词藻堆砌：形容词不叠加，一个准确的动词胜过三个华丽的形容词
- 民间故事的力量在于"说事儿"而非"炫文采"——朴素、干净、有劲就够了

### 特殊元素写作指引

不同元素的写作技巧详见技法参考文件：

| 元素 | 文件 |
|------|------|
| 恐怖惊悚 | [references/techniques/horror.md](references/techniques/horror.md) |
| 香艳旖旎 | [references/techniques/erotic.md](references/techniques/erotic.md) |
| 超自然 | [references/techniques/supernatural.md](references/techniques/supernatural.md) |
| 氛围营造 | [references/techniques/atmosphere.md](references/techniques/atmosphere.md) |
| 民间叙述声音 | [references/techniques/folk-voice.md](references/techniques/folk-voice.md) |

## 步骤 6：修订润色

### 民间故事专用自查清单

- [ ] 说书人的声音是否全篇统一
- [ ] 超自然元素是否"自然"——有无突然变成科幻或悬疑的解释腔
- [ ] 感官细节是否扎根于故事的地域和时代
- [ ] 恐怖/香艳段落的节奏是否有张弛
- [ ] 方言和俗语的浓度是否均匀（不要忽浓忽淡）
- [ ] 角色的命运是否有民间故事的"因果感"（善恶有报，但不必是简单的好人好报）
- [ ] 结尾是否有余韵——民间故事最忌解释过度
- [ ] 伏笔是否收束（或有意留白让读者去想）
- [ ] 修辞是否克制——有无"像……""不是……是……"泛滥、排比连续、词藻堆砌

### 润色层次
按以下顺序进行，避免只改字句而忽略结构：  
1. **叙述层**：说书人口吻是否一致，代际叙述框架是否完整  
2. **情节层**：超自然逻辑是否自洽，因果链是否成立  
3. **语言层**：删除书面腔，强化乡土感官，统一方言浓度，清理多余比喻和排比  

用户若在步骤1选择了**尺度**（暗示留白 / 适度展开 / 浓墨重彩），香艳段落须严格按该尺度执行；技法见 [references/techniques/erotic.md](references/techniques/erotic.md) 中的对应层次。

## 一致性维护（中长篇）

维护设定追踪文档，模板见 [references/structure/tracking-template.md](references/structure/tracking-template.md)。核心项包括：
- 地名、人名统一表
- 超自然规则清单（什么可以发生，什么不行）
- 时间线（用节气/农事标记）
- 伏笔追踪（已埋/已收/待收）
- 角色状态追踪（谁知道了什么，谁还蒙在鼓里）

每完成 5 章回顾一次；可将模板复制到作品目录下随写随填。

## 输出规范

- 故事正文用自然段落输出，不加 Markdown 标记
- 设定文档、大纲、角色卡用结构化 Markdown
- 每次输出标注章节编号和标题
- 分批输出时在每批结尾简述下一批衔接点
- 所有文档保存到用户指定目录（默认工作区根目录下的 `novel/`，不存在则创建）
- **字数检查**：涉及正文字数时（如汇报篇幅、进入步骤 7 前），应调用 MCP 工具 **count_document(正文路径)** 获取精确字数，勿口头估算。
- **完成步骤 5 或 6 后，必须执行步骤 7（创建 novel-editor-runner subagent 并执行评测），否则流程视为未完成。**

## 步骤 7（必做）：创建 novel-editor-runner subagent 并执行评测

**当民间故事创作流程完成（至少完成初稿或修订稿、有可评测的正文）后，必须通过「创建 subagent」的方式执行评测**：使用 **mcp_task** 创建并调用 **novel-editor-runner** 这个 subagent，将刚生成的作品路径（及可选的大纲、设定路径）传给它，由它按 novel-editor 技能完成多维评测并产出报告。

- **触发时机**：完成步骤 5（逐章写作）或步骤 6（修订润色）后，立即执行本步骤。
- **执行方式**：主 agent 不在此对话中直接跑 novel-editor，而是 **创建 subagent**——调用 **mcp_task**，让 subagent 扮演 novel-editor-runner（职责见 `.cursor/agents/novel-editor-runner.md`），对指定作品执行 novel-editor 全流程。
- **mcp_task 调用要点**：
  - **subagent_type**：`generalPurpose`（需完整执行 novel-editor 工作流与读写）。
  - **description**：简短说明，如「对刚完成的民间故事执行 novel-editor 多维评测（novel-editor-runner）」。
  - **prompt**：在 prompt 中明确写出（以下为必含内容）：
    1. 你是 **novel-editor-runner**  agent，请按 `.cursor/agents/novel-editor-runner.md` 的职责执行：加载 novel-editor 技能，对指定作品进行多维评测。
    2. **待评测材料**（须一并提供给 subagent）：
       - **正文**：写明完整路径（如 `novel/作品名.md`）；若正文仅在对话上文未保存，写明「待评测正文即上文由 folk-tale 流程输出的故事正文」并确保 subagent 能访问。
       - **大纲**：若有（如 `novel/作品名-大纲.md`），写明完整路径。
       - **设定**：若有（如 `novel/作品名-设定.md`），写明完整路径。
    3. **评测参数**：小说类型为本流程已确定的子类型（怪谈/传说/志怪等），篇幅与步骤 1 一致，作品阶段为「初稿」或「修订稿」；其余按 novel-editor 步骤 2 取默认。
    4. 按 novel-editor 完整流程执行并保存报告到 `novel/作品名-评测报告.md`；最终将评测结论与报告路径返回给主对话。
- **不跳过**：除非用户明确表示「不要评测」或「先不评测」，否则完成创作后**必须**发起上述「创建 novel-editor-runner subagent」的 mcp_task 调用，不可省略。

---

## 何时加载哪些参考文件

执行对应步骤时按需读取，避免一次性加载全部：

| 时机 | 应加载的文件 |
|------|--------------|
| 步骤1 用户选定子类型后 | 该类型对应的 [references/types/](references/types/) 下文件；复合型则加载用户指定的多个类型文件 |
| 步骤2 世界设定 | 一般不需单独参考；若涉及超自然规则可参看 [references/techniques/supernatural.md](references/techniques/supernatural.md) |
| 步骤4 选定叙事结构后 | 对应 [references/structure/](references/structure/) 下文件（说书人框架 / 嵌套 / 单元连环） |
| 长篇开始写作前 | 加载 [references/structure/tracking-template.md](references/structure/tracking-template.md)，复制到作品目录并随写随填 |
| 步骤5 逐章写作前 | 默认风格 [references/style/moyan-folk.md](references/style/moyan-folk.md)；若用户指定东野风格则加载 [references/style/higashino.md](references/style/higashino.md) |
| 步骤5 写作涉及恐怖/香艳/氛围/叙述口吻时 | 按需加载 [references/techniques/](references/techniques/) 下对应技法文件 |
| 步骤6 修订润色 | 可复看风格卡与技法文件做自查 |

## 参考文件索引

所有参考文件按需加载，只读取当前任务需要的文件。

### 故事类型（选定类型后读取对应文件）

| 类型 | 文件 |
|------|------|
| 怪谈（鬼怪异闻） | [references/types/ghost-tale.md](references/types/ghost-tale.md) |
| 传说（地方人物传说） | [references/types/legend.md](references/types/legend.md) |
| 志怪（超自然记录体） | [references/types/zhiguai.md](references/types/zhiguai.md) |
| 奇谈（荒诞离奇） | [references/types/strange-tale.md](references/types/strange-tale.md) |
| 寓言 | [references/types/fable.md](references/types/fable.md) |

### 叙事结构

| 结构 | 文件 |
|------|------|
| 说书人框架 | [references/structure/oral-frame.md](references/structure/oral-frame.md) |
| 故事套故事 | [references/structure/nested.md](references/structure/nested.md) |
| 单元连环式 | [references/structure/episodic.md](references/structure/episodic.md) |
| 长篇设定追踪（模板） | [references/structure/tracking-template.md](references/structure/tracking-template.md) |

### 写作技法

| 技法 | 文件 |
|------|------|
| 恐怖惊悚 | [references/techniques/horror.md](references/techniques/horror.md) |
| 香艳旖旎 | [references/techniques/erotic.md](references/techniques/erotic.md) |
| 超自然写法 | [references/techniques/supernatural.md](references/techniques/supernatural.md) |
| 氛围营造 | [references/techniques/atmosphere.md](references/techniques/atmosphere.md) |
| 民间叙述声音 | [references/techniques/folk-voice.md](references/techniques/folk-voice.md) |

### 风格参考

| 内容 | 文件 |
|------|------|
| 莫言民间故事风格卡（默认） | [references/style/moyan-folk.md](references/style/moyan-folk.md) |
| 东野圭吾风格卡 | [references/style/higashino.md](references/style/higashino.md) |
