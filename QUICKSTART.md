# Quick Start

## 1. Choose a command

```text
/idea  输入一个研究想法
/lit   基于当前 idea 查文献
/gap   找研究空白和新颖性风险
/frame 构建研究框架
/exp   规划实验
/paper 生成论文核心思路
/log   写日报/周报/月报
```

## 2. Start from a raw idea

```text
/idea 我想研究多模态大模型在遥感变化检测中的应用
```

The agent should use `research-idea-refine` and produce:

- research question
- assumptions
- variants
- recommended direction
- not-doing list
- next action

## 3. Ground it in literature

```text
/lit 基于当前 idea 查最近三年的相关文献，并找最接近工作
```

The agent should use `literature-grounding` and produce:

- search queries
- candidate paper matrix
- closest-work comparison
- novelty risk
- baselines/datasets

## 4. Decide whether to continue

```text
/gap 判断这个 idea 是否值得继续做
```

The agent should use `gap-and-novelty-review` and output:

- Go / Pivot / Stop / Need More Literature
- concrete reasons
- next actions

## 5. Build toward a paper

```text
/frame 生成研究框架
/exp 设计实验计划
/paper 生成 one-sentence pitch、contribution 和 abstract
```

## 6. Keep logs independent

```text
/log 写本周跨项目研究周报，不要只围绕项目
```

The agent should use `research-log-review` and include project work, idea work, literature, non-project work, decisions, blockers, and next strategy.
