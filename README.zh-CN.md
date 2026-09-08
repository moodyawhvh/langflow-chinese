<div align="center">

# langflow 中文文档

**[中文版] langflow — 可视化构建与部署 AI 智能体和工作流的强大平台**

[![原项目](https://img.shields.io/badge/原项目-langflow-ai--langflow-blue?style=flat-square&logo=github)](https://github.com/langflow-ai/langflow)
[![License](https://img.shields.io/badge/license-MIT-orange)](https://opensource.org/licenses/MIT)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 本文档是 [langflow-ai/langflow](https://github.com/langflow-ai/langflow) 官方 README 的完整中文翻译。
> 完整源代码请访问原项目:https://github.com/langflow-ai/langflow

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 简介

[Langflow](https://langflow.org) 是一个用于构建和部署 AI 智能体与工作流的强大平台。它为开发者同时提供可视化编排体验,以及内置的 API 服务器和 MCP 服务器——后者能把每个工作流直接变成一个工具,集成到基于任何框架、任何技术栈构建的应用中。Langflow 开箱即用,支持所有主流大语言模型、向量数据库,以及不断增长的 AI 工具库。

## ✨ 核心特性

- **可视化构建界面**:快速上手、快速迭代。
- **源码可访问**:任何组件都可以用 Python 自定义。
- **交互式 Playground**:支持逐步执行控制,即时测试和改进你的 Flow。
- **多智能体编排**:内置会话管理与检索。
- **部署为 API**:或导出为 JSON,供 Python 应用使用。
- **部署为 MCP 服务器**:把你的工作流变成 MCP 客户端可用的工具。
- **可观测性**:支持 LangSmith、LangFuse 等集成。
- **企业级就绪**:安全与可扩展性兼备。

## 🖥️ Langflow Desktop

Langflow Desktop 是上手 Langflow 最简单的方式。所有依赖均已内置,你无需管理 Python 环境,也不用手动安装软件包。支持 Windows 和 macOS。

[📥 下载 Langflow Desktop](https://www.langflow.org/desktop)

## ⚡️ 快速开始

### 本地安装(推荐)

需要 Python 3.10–3.14 以及 [uv](https://docs.astral.sh/uv/getting-started/installation/)(推荐的包管理器)。

#### 安装

在一个全新的目录中运行:

```shell
uv pip install langflow -U
```

即可安装最新版 Langflow 包。更多信息参见官方文档 [Install and run the Langflow OSS Python package](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package)。

#### 运行

启动 Langflow:

```shell
uv run langflow run
```

Langflow 将在 http://127.0.0.1:7860 启动。

搞定!现在可以开始用 Langflow 构建了!🎉

## 📦 其他安装方式

### 从源码运行

如果你已克隆本仓库并希望参与贡献,请在仓库根目录运行:

```shell
make run_cli
```

更多信息参见 [DEVELOPMENT.md](https://github.com/langflow-ai/langflow/blob/main/DEVELOPMENT.md)。

### Docker

以默认配置启动 Langflow 容器:

```shell
docker run -p 7860:7860 langflowai/langflow:latest
```

然后即可在 http://localhost:7860/ 访问 Langflow。配置选项参见 [Docker 部署指南](https://docs.langflow.org/deployment-docker)。

## 🛡️ 安全

安全相关信息参见原项目的 [安全策略](https://github.com/langflow-ai/langflow/blob/main/SECURITY.md)。

## 🚀 部署

Langflow 完全开源,可部署到各大主流云平台。部署方法参见官方 [Langflow 部署指南](https://docs.langflow.org/deployment-overview)。

## ⭐ 保持更新

在 GitHub 上给 Langflow 点个 Star,即可第一时间收到新版本发布通知。

## 👋 参与贡献

原项目欢迎各水平开发者的贡献。如果想参与贡献,请查阅 [贡献指南](https://github.com/langflow-ai/langflow/blob/main/CONTRIBUTING.md),帮助 Langflow 变得更加易用。

## ❤️ 贡献者

感谢原项目所有贡献者,完整名单见 [contributors](https://github.com/langflow-ai/langflow/graphs/contributors)。

---

## 版权声明

本文档为 [langflow-ai/langflow](https://github.com/langflow-ai/langflow) 官方 README 的中文翻译版本,仅供学习交流使用。原项目及所有代码版权归原项目作者所有,遵循其原始 MIT 许可证。

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

**如果觉得有用,请给原项目点个 Star!** ⭐
