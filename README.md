# Research Pipeline Skill

端到端科研工作流管理系统，为 Claude Code 提供完整的科研项目管理能力。

## ✨ 功能特性

### 🎯 核心功能
- **项目管理**: 新建/切换研究项目，自动创建标准目录结构
- **研究方向配置**: 通过 `direction.md` 快速记录研究背景、技术栈、目标
- **文献管理**: 批量检索论文、生成结构化笔记、综合分析
- **Idea 分析**: 使用 Socratic 对话评估研究想法的创新性、可行性
- **日报/周报**: 支持自动总结、文献阅读日报、常规日报
- **论文撰写**: 根据目标会议自动选择合适的写作技能
- **进度追踪**: 维护项目进度日志
- **GitHub 集成**: 克隆第三方代码仓库，方便阅读和复现

### 🤖 智能特性
- **研究方向感知**: 自动读取 `direction.md`，理解研究目标和技术栈
- **自动总结日报**: 扫描聊天历史，智能分类科研相关和其他工作
- **智能关联分析**: 基于研究方向评估论文与项目的关联度
- **跨技能协调**: 文献→idea→论文的无缝衔接

## 🚀 快速开始

### 1. 初始化工作区（首次使用）
```
帮我设置科研工作区，路径 ~/research-hub
```

### 2. 新建研究项目
```
新建项目「基于 Transformer 的遥感影像分类」
```

### 3. 设置研究方向（重要！）
```
设置研究方向
```
交互式配置研究背景、问题、技术栈、目标等。

### 4. 开始使用
```
写日报                    # 自动总结今日工作
写日报 论文A 论文B         # 文献阅读日报
查找文献 Vision Transformer  # 文献搜索
分析 idea                  # Idea 分析
开始写论文                 # 论文撰写
```

## 📁 目录结构

```
research-hub/
├── projects/                    # 研究项目
│   └── <project-id>/           # 每个项目一个目录
│       ├── meta.md             # 项目元信息
│       ├── direction.md        # 研究方向配置
│       ├── idea.md             # 研究想法与假设
│       ├── literature/         # 文献笔记
│       │   ├── notes/          # 单篇文献笔记
│       │   └── synthesis.md    # 文献综合分析
│       ├── experiments/        # 实验记录
│       ├── drafts/             # 论文草稿
│       ├── third_party/        # 第三方代码仓库（git clone）
│       └── progress.md         # 项目进度日志
├── daily/                       # 日报
│   └── YYYY-MM-DD.md
├── weekly/                      # 周报
│   └── YYYY-WXX.md
├── inbox/                       # 快速收集
│   └── *.md
└── templates/                   # 模板
    ├── project-meta.md
    ├── direction.md
    ├── daily.md
    ├── weekly.md
    └── lit-note.md
```

## 📋 命令参考

| 命令 | 说明 |
|------|------|
| `新建项目 <name>` | 初始化研究项目 |
| `切换项目 <name>` | 切换活跃项目 |
| `设置研究方向` | 交互式配置研究方向 |
| `更新研究方向 <字段>: <值>` | 更新研究方向的特定字段 |
| `查看研究方向` | 显示当前研究方向配置 |
| `快速了解项目` | 读取 direction.md 并总结 |
| `查找文献 <query>` | 执行文献搜索 |
| `分析 idea` | 启动 idea 分析 |
| `写日报` | 自动扫描聊天历史，智能分类总结 |
| `写日报 论文A、论文B` | 生成文献阅读日报（自动检索） |
| `记录文献：论文A、论文B` | 仅记录文献到日报 |
| `写周报` | 生成本周周报 |
| `开始写论文` | 启动论文撰写流程 |
| `项目进度` | 显示当前项目状态 |
| `列出项目` | 显示所有项目 |
| `连接 github <url>` | 克隆第三方仓库到项目 |
| `拉取代码 <url>` | 同上，更口语化的表达 |
| `同步 github` | 更新所有第三方仓库 |
| `查看依赖` | 列出所有已克隆的第三方仓库 |

## 📊 日报功能

### 自动总结日报
输入 `写日报` 时，系统会：
1. 自动扫描今日聊天历史
2. 基于研究方向智能分类活动
3. 生成结构化日报，分为：
   - **科研项目相关**: 文献阅读、实验进展、论文写作等
   - **其他工作**: 工具开发、技能制作、系统配置等

### 文献阅读日报
输入 `写日报 论文A 论文B` 时，系统会：
1. 自动检索论文信息（arXiv、Semantic Scholar）
2. 提取核心贡献、方法、关键结果
3. 评估与当前项目的关联度
4. 生成结构化日报并保存文献笔记

## 🔗 GitHub 集成

### 功能说明
支持将第三方代码仓库克隆到项目目录中，方便：
- 阅读和分析相关代码
- 复现实验结果
- 基于现有代码进行改进
- 管理项目依赖

### 使用方法

#### 1. 首次使用：认证 GitHub
```bash
# 安装 GitHub CLI（如果未安装）
winget install GitHub.cli

# 登录认证
gh auth login
```

#### 2. 克隆第三方仓库
```
连接 github https://github.com/user/repo
拉取代码 https://github.com/user/repo
```

系统会：
1. 检查 GitHub CLI 认证状态
2. 使用浅克隆（`--depth 1`）加速下载
3. 克隆到 `projects/<project-id>/third_party/<repo-name>/`
4. 更新 `direction.md` 添加代码仓库信息
5. 记录到 `progress.md`

#### 3. 管理第三方仓库
```
同步 github          # 更新所有第三方仓库
查看依赖            # 列出所有已克隆的第三方仓库
```

### 安全管理
- **自动 .gitignore**: 确保 `third_party/` 不会被提交到项目仓库
- **浅克隆**: 使用 `--depth 1` 减少下载时间
- **认证管理**: 使用 GitHub CLI 管理认证，避免暴露 Token

### 示例
```
连接 github https://github.com/facebookresearch/map-anything

系统执行：
1. 检查 gh auth status → 已认证
2. git clone --depth 1 https://github.com/facebookresearch/map-anything.git projects/feedforward-3d-reconstruction/third_party/map-anything
3. 更新 direction.md：添加 MapAnything 作为关键参考代码
4. 更新 progress.md：记录克隆操作
```

## 🔗 与其他技能的集成

本技能是编排层，协调以下技能完成科研全流程：

| 技能 | 用途 |
|------|------|
| `deep-research` | 文献搜索、系统综述 |
| `nature-academic-search` | PubMed/CrossRef/arXiv 检索 |
| `nature-citation` | 添加引用 |
| `academic-paper` | 通用论文撰写 |
| `ml-paper-writing` | ML 论文 |
| `nature-writing` | Nature 风格写作 |
| `academic-paper-reviewer` | 论文审稿 |
| `nature-paper2ppt` | 论文 PPT |

## 📝 模板说明

### direction.md（研究方向配置）
项目的快速上下文文件，包含：
- 研究背景和动机
- 具体研究内容
- 技术栈和方法偏好
- 目标会议/期刊
- 关键文献和参考
- 当前进展和下一步

### 为什么需要 direction.md？
- 让模型快速了解项目上下文
- 每次交互时自动读取
- 提供针对性的分析和建议
- 跨会话保持项目状态

## 🛠️ 开发相关

### 文件结构
- `SKILL.md`: 主技能文件，包含完整工作流
- `QUICKSTART.md`: 快速开始指南
- `templates/`: 各类模板文件

### 贡献
欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- Claude Code 团队
- 所有贡献者和用户
