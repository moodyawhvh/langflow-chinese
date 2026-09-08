<div align="center">

# langflow 中文翻译版

**[中文版] langflow — 可视化构建与部署 AI 智能体和工作流的强大平台**

[![原项目](https://img.shields.io/badge/原项目-langflow-ai--langflow-blue?style=flat-square&logo=github)](https://github.com/langflow-ai/langflow)
[![中文文档](https://img.shields.io/badge/中文文档-README.zh--CN.md-orange?style=flat-square)](README.zh-CN.md)
[![GitHub Stars](https://img.shields.io/github/stars/langflow-ai/langflow?style=flat-square&label=原项目Stars)](https://github.com/langflow-ai/langflow/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 这是 [langflow-ai/langflow](https://github.com/langflow-ai/langflow) 的中文翻译版本。
> 完整源代码请访问原项目:https://github.com/langflow-ai/langflow

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

Langflow 是一个用于构建和部署 AI 智能体与工作流的强大开源平台。它为开发者提供可视化的编排界面,同时内置 API 与 MCP 服务器,可以把每一个工作流直接变成工具,集成到任何框架、任何技术栈构建的应用中。Langflow 开箱即用,支持主流大语言模型、向量数据库,并拥有持续增长的 AI 工具组件库。

## ✨ 主要特性

- **可视化构建界面**:快速上手、快速迭代,拖拽即可编排工作流。
- **源码可定制**:任意组件都能用 Python 直接修改扩展。
- **交互式 Playground**:支持逐步执行控制,即时测试并打磨你的 Flow。
- **多智能体编排**:内置会话管理与检索能力。
- **部署为 API**:一键把工作流发布成 API,或导出 JSON 供 Python 应用使用。
- **部署为 MCP 服务器**:把工作流变成 MCP 客户端可调用的工具。
- **可观测性**:支持 LangSmith、LangFuse 等集成。
- **企业级就绪**:安全性与可扩展性兼备。

## 📁 文件说明

| 文件 | 说明 |
|:-----|:-----|
| README.md | 本文件(中文简介) |
| README.zh-CN.md | 详细中文文档(完整汉化) |

## 🚀 快速开始

1. **桌面版(最简单)**:Langflow Desktop 内置全部依赖,无需手动管理 Python 环境,支持 Windows 与 macOS:[📥 下载 Langflow Desktop](https://www.langflow.org/desktop)。
2. **本地安装(推荐)**:需要 Python 3.10–3.14 与 [uv](https://docs.astral.sh/uv/getting-started/installation/) 包管理器,在全新目录执行:

   ```shell
   uv pip install langflow -U
   ```

3. **启动服务**:

   ```shell
   uv run langflow run
   ```

4. **打开浏览器**访问 http://127.0.0.1:7860,即可开始构建,就这么简单!🎉
5. **Docker 方式**:使用默认配置启动容器:

   ```shell
   docker run -p 7860:7860 langflowai/langflow:latest
   ```

   然后访问 http://localhost:7860/,配置项参见 [Docker 部署指南](https://docs.langflow.org/deployment-docker)。
6. **源码运行**:克隆本仓库后,在仓库根目录执行 `make run_cli`,详见原项目 [DEVELOPMENT.md](https://github.com/langflow-ai/langflow/blob/main/DEVELOPMENT.md)。
7. **云端部署**:Langflow 完全开源,可部署到各大云平台,参见官方[部署指南](https://docs.langflow.org/deployment-overview)。

完整源代码与最新版本请访问原项目:https://github.com/langflow-ai/langflow

## 📞 联系方式

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [langflow-ai/langflow](https://github.com/langflow-ai/langflow) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证。

**如果觉得有用,请给原项目点个 Star!** ⭐
