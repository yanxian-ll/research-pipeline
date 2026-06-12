# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.4.0] - 2026-06-12

### Added
- **基于代码编写论文方法功能**：自动分析代码仓库，生成论文方法部分草稿
- 代码结构识别：自动扫描模型、损失、数据处理、训练模块
- 技术细节提取：从代码中提取架构、损失、训练配置等信息
- 方法草稿生成：在 `drafts/method_draft.md` 生成结构化方法章节
- 分析模板：提供模型架构、损失函数、训练细节的分析模板

### Changed
- 更新核心流程：新增"基于代码编写论文方法"步骤
- 更新命令参考：添加代码分析相关命令

### Fixed
- 无

## [1.3.0] - 2026-06-12

### Added
- **项目 GitHub 同步功能**：支持将研究项目推送到 GitHub 进行在线备份
- **项目初始化时创建 GitHub 仓库**：`新建项目 X 并上传 github`
- **项目克隆功能**：从 GitHub 克隆已有项目
- **项目同步功能**：更新本地项目到最新版本
- 默认创建 private 仓库，保护研究隐私

### Changed
- 更新目录结构：添加 `third_party/` 目录
- 更新工作流：添加 GitHub 集成和项目同步步骤
- 更新命令参考：添加项目同步相关命令

### Fixed
- 无

## [1.2.0] - 2026-06-12

### Added
- **GitHub 集成功能**：支持克隆第三方代码仓库到项目
- 浅克隆加速：使用 `--depth 1` 减少下载时间
- GitHub CLI 认证管理：自动检查和引导认证
- 第三方代码管理：查看依赖、同步更新
- 自动 .gitignore：确保 third_party/ 不会被提交

### Changed
- 更新目录结构：添加 `third_party/` 目录
- 更新工作流：添加 GitHub 集成步骤
- 更新命令参考：添加 GitHub 相关命令

### Fixed
- 无

## [1.1.0] - 2026-06-12

### Added
- 自动总结日报功能：根据聊天历史智能分类总结工作内容
- 日报分为两部分：科研项目相关和其他工作
- 使用 history 工具自动扫描聊天记录
- 智能分类判断标准：基于研究方向自动分类
- 新增分类判断标准文档

### Changed
- 更新日报触发方式：`写日报` 现在会自动扫描聊天历史
- 优化日报模板：分为科研相关和其他工作两大部分
- 更新命令参考：说明自动总结功能

### Fixed
- 无

## [1.0.0] - 2026-06-11

### Added
- 初始版本发布
- 项目管理功能：新建/切换研究项目
- 研究方向配置：direction.md 快速上下文
- 文献管理：批量检索、结构化笔记
- Idea 分析：Socratic 对话评估
- 日报/周报：文献阅读日报、常规日报
- 论文撰写：根据目标会议自动选择技能
- 进度追踪：维护项目进度日志
- 智能特性：研究方向感知、智能关联分析
- 跨技能协调：文献→idea→论文无缝衔接

### Changed
- 无

### Fixed
- 无

## [0.9.0] - 2026-06-10

### Added
- 开发版本
- 基础框架搭建
- 模板文件创建

### Changed
- 无

### Fixed
- 无
