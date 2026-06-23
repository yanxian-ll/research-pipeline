---
name: paper-deep-reading
description: Performs source-grounded, beginner-friendly-to-expert close reading of an academic paper. Use when the user asks to 精读/深读/深入解读 a paper, wants to quickly understand a paper even as a beginner, understand why a method was proposed, trace how each module follows from the problem, inspect figures/tables/ablations, request reproduction-level analysis, prepare for technical discussion, or produce detailed paper notes rather than a brief summary or broad survey.
---

# Paper Deep Reading

## Overview

Deep reading should help the reader learn the paper quickly, not only audit it
like an expert. Always build understanding in layers:

```text
quick intuition -> problem story -> method map -> technical details
-> evidence audit -> reusable takeaways
```

Start from what the paper is trying to make possible, explain the problem in
plain language, then gradually deepen into architecture, equations,
supervision, experiments, ablations, limitations, and reproduction details.

Default output language should follow the user. If the user writes Chinese,
write the reading notes in Chinese.

## When to Use

- The user asks for 精读, 深读, 深入解读, 细读, paper deep reading, or close reading.
- The user wants to understand a paper from scratch, including as a beginner.
- The user asks why a method was proposed or how each module follows from the
  problem.
- Figures, tables, equations, ablations, limitations, or appendix details must
  be connected into one evidence chain.
- A paper must be understood well enough for reproduction, presentation,
  framework design, technical discussion, or future research use.

Use `paper-reading-and-synthesis` for concise summaries, paper comparisons, and
topic surveys. Use `literature-grounding` when the primary goal is novelty,
closest-work, baseline, or citation search for a named idea or project.

## Reading Style

Prefer a teaching-first style:

- Explain the paper as if the reader is smart but may not know this subfield.
- Define important terms when they first appear.
- Use analogies only when they clarify the mechanism, not as decoration.
- State the plain-language idea before formulas or architecture details.
- Keep expert critique, failure modes, and reproduction notes, but place them
  after the reader has enough context.
- Separate `作者明确声称`, `从论文证据可推出`, and `我的推断`.
- Do not hide weaknesses; explain why they matter.

Avoid these failure modes:

- Starting with architecture before explaining the problem.
- Writing only expert audit notes that a beginner cannot follow.
- Listing modules without explaining why they exist.
- Reporting numbers without saying what the metric measures.
- Treating qualitative figures as proof without protocol.
- Overclaiming from abstract or leaderboard results.

## Workflow

### 1. Fix Scope and Evidence

1. Classify the reading as independent, idea-linked, or project-linked.
2. Verify title, version, venue, authors, source, code, supplementary material,
   and available artifacts using primary sources.
3. State evidence status clearly: full text, appendix, code, abstract only,
   inaccessible appendix, unreleased code, etc.
4. Read introduction, related work, method, experiments, ablations,
   limitations, and relevant appendix before claiming a full reading.
5. If only partial material is available, label the reading as partial and
   avoid reproduction-level certainty.

### 2. Start with a Beginner-Friendly First Pass

Before technical analysis, give the reader a quick entry point:

1. **One-sentence answer:** What is this paper about?
2. **Why should we care?** What capability or bottleneck does it address?
3. **Before this paper:** What did people normally do?
4. **Main pain point:** What breaks in the old way?
5. **Core idea in plain language:** What is the paper's central trick?
6. **What goes in and what comes out?** State inputs, outputs, and task setting.
7. **One simple mental model:** Provide a compact intuitive picture.

This section should let a beginner understand the paper's purpose without
knowing the architecture yet.

### 3. Reconstruct the Problem Story

Then reconstruct the paper's reasoning:

1. **Target capability:** What should an ideal system do?
2. **Prior paradigm:** What was the field's usual solution?
3. **Concrete failure:** On what data, geometry, scale, cost, assumption, or
   supervision does it fail?
4. **Why the obvious fix is insufficient:** What tempting solution does not
   solve the failure, and why?
5. **Core contradiction:** Which two desirable properties appear hard to get
   together?
6. **Design constraints:** What must a valid solution preserve, avoid, or make
   efficient?

Separate author-stated motivation from reconstructed interpretation. If the
paper does not prove a premise, label it as a premise or hypothesis.

### 4. Build a Method Map Before Details

Create a high-level map before diving into components:

```text
input -> representation -> main modules -> output -> loss/evaluation
```

Then build a problem-to-design table:

| Problem or constraint | Required capability | Proposed mechanism | Expected observable effect |
|---|---|---|---|

For every major module:

1. Explain the module in one plain sentence.
2. Identify the exact problem or constraint it addresses.
3. Explain inputs, outputs, representation, coordinate frame, and information
   flow.
4. Explain why this mechanism is preferable to a simpler alternative.
5. State what would likely break if the module were removed.
6. Classify it as core innovation, enabling component, inherited baseline, or
   implementation detail.

Do not present architecture order as causal reasoning. A component that cannot
be tied back to the starting problem is not automatically a contribution.

### 5. Gradually Enter Technical Details

After the reader understands the map, go deeper:

- For equations: define each symbol, explain the physical or algorithmic
  meaning, state the assumption that makes the equation valid, and explain what
  behavior the equation encourages.
- For losses: explain what each loss can and cannot enforce.
- For representations: explain coordinate system, scale, gauge freedom,
  normalization, and what information is lost or preserved.
- For attention/transformer/modules: explain what communicates with what, over
  which tokens, and why that matters.
- For pipelines: mark preprocessing, post-processing, external sensors,
  retrieval, optimization, alignment, and hidden dependencies.

Use small diagrams or pseudocode when they make the mechanism easier to learn.

### 6. Trace Supervision and Inference

Audit:

- training data, labels, pseudo-labels, priors, frozen modules, and leakage;
- objectives and what behavior each loss can actually enforce;
- train/inference mismatch;
- preprocessing, post-processing, alignment, retrieval, optimization, or
  external sensors required at inference;
- coordinate systems, scale assumptions, normalization, and gauge freedoms;
- computational cost and scaling variable.

Make clear what is required during training only and what is required at
inference.

### 7. Teach the Figures, Tables, and Ablations

For each central figure/table/ablation, explain:

1. What question is this figure/table answering?
2. What comparison should the reader inspect?
3. What does the result show in plain language?
4. What claim does it support?
5. What ambiguity remains?

For ablations, distinguish:

- necessity: does removing a module hurt?
- interaction: do modules work only together?
- alternative explanation: could another change explain the result?

### 8. Audit the Evidence Chain

For each principal claim, record:

| Claim | Evidence | Metric/protocol | What it supports | What it does not support |
|---|---|---|---|---|

Check:

- whether baselines isolate the claimed novelty;
- whether metrics measure the target capability directly or through alignment;
- whether generalization crosses datasets, domains, scales, or only scenes;
- whether efficiency comparisons use comparable hardware and settings;
- whether qualitative examples are representative or selected;
- whether limitations contradict broad wording in the abstract or conclusion.

### 9. Rebuild the Paper in One Causal Chain

Produce a concise chain:

```text
desired capability
-> prior paradigm
-> observed failure
-> core contradiction
-> design constraints
-> proposed mechanism
-> training signal
-> experimental test
-> supported conclusion
-> unresolved boundary
```

If any arrow is unsupported, mark the gap instead of smoothing it over.

### 10. Extract Reusable Understanding

Conclude with:

- beginner takeaway: the paper in 3-5 simple bullets;
- strongest supported contribution;
- contribution that is mainly engineering or presentation;
- hidden assumptions and likely failure cases;
- what to copy or reuse in another project;
- what not to copy blindly;
- minimum reproduction recipe;
- most informative ablation to rerun;
- follow-up questions suggested by the paper itself.

Add implications for an idea or project only when the user explicitly requests
that linkage or provides an idea/project context.

## Recommended Artifact Structure

Use this structure by default, adjusting to paper complexity:

```markdown
# <Paper Title> 精读笔记

## 论文信息与证据状态
## 先用一句话讲清楚
## 小白友好版：这篇论文到底想解决什么？
## 任务设定：输入、输出、数据和评价
## 问题背景：旧方法为什么不够？
## 核心想法：作者的关键转折
## 方法总览图 / 流程
## 模块逐个解释：先直觉，后细节
## 训练与推理：监督、损失、依赖和成本
## 图表和实验怎么读
## 证据链审计
## 局限、风险和隐藏假设
## 如果我要复现，最小步骤是什么？
## 对我的研究/项目有什么启发（仅在相关时）
## 最终总结：3 层理解
```

The `最终总结：3 层理解` should contain:

1. **30 秒版:** one paragraph for quick memory.
2. **5 分钟版:** problem, method, result, limitation.
3. **深入版:** key mechanism, evidence, and open boundary.

## Artifacts

Independent:

- `knowledge/papers/<paper-id>-deep-read.md`
- `reviews/<paper-id>-deep-read.md`

Idea/project-linked:

- `ideas/<idea-id>/literature/<paper-id>-deep-read.md`
- `projects/<project-id>/literature/papers/<paper-id>-deep-read.md`

Use an existing template if present, but prefer the beginner-to-deep structure
above when the old template is too expert-only.

## Verification

- [ ] Paper identity, version, and available sources are recorded.
- [ ] A beginner can understand the task, motivation, and core idea before
      technical details begin.
- [ ] The task setting clearly states inputs, outputs, data, and metrics.
- [ ] The starting point includes prior paradigm, failure, contradiction, and
      constraints.
- [ ] Every major method component maps to a problem or is labeled an
      implementation detail.
- [ ] Equations/losses are explained in meaning, not only notation.
- [ ] Training, inference, coordinate frames, scale, and post-processing are
      explicit.
- [ ] Main claims map to figures, tables, metrics, or ablations.
- [ ] Evidence limits and alternative explanations are stated.
- [ ] The causal chain contains no silently unsupported arrow.
- [ ] Artifact scope and location are correct.
- [ ] The next reading or reproduction action is concrete.

