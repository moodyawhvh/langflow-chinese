# 搭建开发环境

> 🌐 本文档由 [langflow-ai/langflow](https://github.com/langflow-ai/langflow) 翻译,英文原版见原项目。
>
> 📝 原文较长,本页为中文核心章节翻译;命令与输出示例保持原样。

本文档详细介绍如何搭建本地开发环境,让你能够为项目贡献改动!

## 基础要求

- 项目托管在 GitHub 上,所以你需要一个 GitHub 账号(能读到这份文档,你多半已经有了!)
- 一个 IDE,例如 Microsoft VS Code:https://code.visualstudio.com/

## 设置 Git 仓库 Fork

你需要把改动推送到 Langflow 仓库的 fork,再从那里向项目仓库发起 Pull Request。

Fork [Langflow GitHub 仓库](https://github.com/langflow-ai/langflow/fork),按提示创建新 fork。

在你的新 fork 上,点击 "<> Code" 按钮,获取 [clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 地址,用你喜欢的方式克隆仓库;例如用 `https`:

```bash
git clone https://github.com/<your username>/langflow.git
```

最后,把项目仓库添加为 `upstream`:

```bash
cd langflow
git remote add upstream https://github.com/langflow-ai/langflow.git
git remote set-url --push upstream no_push
```

> [!TIP]
> **Windows/WSL 用户**:你可能发现文件"变了",尤其是文件权限位,例如 "changed file mode 100755 → 100644"。可以用 `git config core.filemode false` 规避这个问题。

## 设置环境

有两种选择:用 `make` 命令使用本地环境(macOS 和 Linux 推荐),或使用开发容器("[Dev Container](https://containers.dev/)")(Windows 用户推荐)。

### 选项 1(推荐):使用本地环境

安装前置依赖:

- **操作系统**:macOS 或 Linux;Windows 用户请使用 WSL,或考虑选项 2(Dev Container)。
- **`git`**:项目使用通用的 `git` 做版本控制。
- **`make`**:项目使用 `make` 协调打包。
- **`uv`**:本项目使用 Astral 的 Python 包与项目管理器 `uv`(`>=0.4`)。安装说明见 https://docs.astral.sh/uv/getting-started/installation/。
- **`npm`**:前端使用 Node.js(`v22.12 LTS`)和 `npm`(`v10.9`)构建。安装说明见 https://nodejs.org/en/download/package-manager。
  - Windows(WSL)用户:确保 `npm` 安装在 WSL 环境内;`which npm` 应指向 Linux 路径而不是 Windows 路径。

### 选项 2:使用 Dev Container(Windows 推荐)

按你的 IDE 的说明,把本仓库作为 Dev Container 打开。

仓库内已包含预配置的 `.devcontainer`,支持的 IDE 会自动识别。

#### Microsoft VS Code

要启动预配置的 `.devcontainer`,请安装 VS Code Dev Containers 扩展,然后在命令面板运行 Dev Containers: Reopen in Container 命令。

- 参见 [Developing inside a Container](https://code.visualstudio.com/docs/devcontainers/containers)
- 你可能还想与容器[共享 `git` 凭据](https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials)

### 初始环境验证

运行以下命令搭建并验证初始环境:

```bash
make init
```

该命令通过安装后端和前端依赖、安装 pre-commit 钩子来搭建开发环境。它会依次执行 `make install_backend`、`make install_frontend` 和 `uvx pre-commit install`。

> [!TIP]
> 如果你想快速从源码跑起 Langflow 而不搭建完整开发环境,可以改用 `make run_cli`。该命令会一步完成依赖安装、前端构建并启动应用。

运行 `make init` 后,你有两种运行 Langflow 的方式:

- 用 `make run_cli` 立即构建并运行应用。
- 继续下一节,以开发模式运行 Langflow。

### 前端构建问题排查

如果遇到前端构建问题,或从旧版本升级而来,先运行一次 `make run_clic`。

```bash
make run_clic
```

该命令会清理构建缓存并完全重建,能解决版本切换时的大部分前端问题。

## 完整开发环境设置

正式开发前,还有一些步骤值得考虑。

### 可选的 pre-commit 钩子

pre-commit 钩子有助于保持你的改动整洁、格式规范。

> [!NOTE]
> 安装这些钩子后,`git commit` 需要在 Python 环境内运行,命令需改为 `uv run git commit`。

运行以下命令安装 pre-commit 钩子:

```bash
uv sync
uv run pre-commit install
```

## 以开发模式运行 Langflow

完成上述验证后,你就可以让后端(FastAPI)和前端(Node)服务以"热重载"方式运行你的改动。在这种模式下,FastAPI 服务器需要一个 Node.js 服务器来提供前端页面,而不是自己直接提供。

> [!NOTE]
> 正常开发流程中你会同时开着多个终端会话,下文分别标注为 _Backend Terminal_、_Frontend Terminal_、_Documentation Terminal_ 和 _Build Terminal_。

### 调试模式

VS Code 用户可以使用现成的调试配置:在 Debug 标签页启动(后端调试模式可直接按 F5 启动)。你可能更喜欢以这种方式启动服务。仍然建议阅读下面的小节,了解预期的控制台输出和服务就绪状态。

### 启动后端服务

后端服务以 Python 上的 FastAPI 服务运行,负责处理 API 请求。在 _Backend Terminal_ 中启动后端:

```bash
make backend
```

> [!TIP]
> **组件开发模式**:默认情况下,Langflow 使用预构建的组件索引以实现快速启动(约 10ms)。如果你正在开发或修改组件,请用 `LFX_DEV` 启用动态组件加载:
>
> ```bash
> # 动态加载全部组件
> LFX_DEV=1 make backend
>
> # 只加载指定的组件模块(开发工作流更快)
> LFX_DEV=mistral,openai,anthropic make backend
> ```
>
> 列表模式在开发特定集成时尤其有用,只加载所需组件能显著加快启动时间。
>
> 不带 `LFX_DEV` 时,组件改动需要重建索引:
>
> ```bash
> uv run python scripts/build_component_index.py
> ```

你会看到类似如下输出:

```
INFO:     Will watch for changes in these directories: ['/home/phil/git/langflow']
INFO:     Loading environment from '.env'
INFO:     Uvicorn running on http://0.0.0.0:7860 (Press CTRL+C to quit)
INFO:     Started reloader process [22330] using WatchFiles
Starting Langflow ...
```

此时可在浏览器中访问 http://localhost:7860/health;后端服务就绪后会返回类似文档:

```json
{ "status": "ok" }
```

### 启动前端服务

前端(用户界面)在发行代码中(即 `langflow run`)是静态编译文件,由后端 FastAPI 服务通过端口 `7860` 提供给客户端。开发模式下,这些文件由运行在端口 `3000` 的 Node.js 服务提供。在 _Frontend Terminal_ 中启动前端服务:

```bash
make frontend
```

你会看到类似如下输出:

```
  VITE v5.4.11  ready in 552 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

此时可在浏览器中访问 http://localhost:3000/ 进入 Langflow 用户界面。

### 构建并查看文档

> [!IMPORTANT]
> 如果你使用的是 dev container,请在容器外的宿主终端构建文档,不要在 dev container 工作区内运行。文档构建在容器内可能无法正常工作。

如果你要为文档贡献改动(永远欢迎!),文档使用 [Docusaurus](https://docusaurus.io/) 构建,同样基于 Node.js 独立提供服务。

在终端中,于项目根目录运行:

```bash
cd docs
npm install
npm run start
```

如果前端服务已占用端口 `3000`,系统会提示 `Would you like to run the app on another port instead?`,回答"yes"即可。你会看到类似输出:

```
[SUCCESS] Docusaurus website is running at: http://localhost:3001/
```

浏览器访问 http://localhost:3001/ 查看文档。文档保存后即可看到更新,不过有时需要手动刷新浏览器页面。

## 添加或修改组件

组件位于 `src/backend/base/langflow` 下的各个文件夹,单元测试位于 `src/backend/base/tests/unit/components`。

> [!IMPORTANT]
> **组件开发模式**:积极开发组件时,请务必用 `LFX_DEV=1` 运行后端以启用实时重载:
>
> ```bash
> LFX_DEV=1 make backend
> ```
>
> 这样你的组件改动会立即生效,无需重建组件索引。

### 添加组件

把组件添加到合适的子目录,并在 `__init__.py` 中登记(按 `import` 和 `__all__` 列表字母序)。假设后端和前端服务正以 **`LFX_DEV=1`** 运行,这些文件变化时后端服务会自动重启。新组件会在后端重启后、_并且_你在浏览器点击"刷新"后可见。

> [!TIP]
> 更快的做法是:先把组件代码从编辑器粘贴到 UI 中试用,_先不_保存源码;确认工作正常后再保存(触发后端重启)并刷新浏览器确认组件已出现。

你应该为组件补充单元测试,不过相关模板和最佳实践仍在完善中。至少请在组件对应的单元测试子目录中创建一个 Markdown 文件(目录不存在就创建),文件名与组件同名、扩展名为 `.md`,内容写明你手动测试该组件的步骤。

### 修改组件

修改组件与添加组件基本相同:通常先在 UI 里改,再把文件保存回仓库更方便。请务必检查并同步修改单元测试;如果该组件还没有单元测试,能补一个至少覆盖你改动的测试将不胜感激!

> [!NOTE]
> 如果改动保存、后端服务重启时,画布上还是该组件的旧版本,重新加载画布(即浏览器刷新)后组件应显示 "Updates Available"。[Issue 5179](https://github.com/langflow-ai/langflow/issues/5179) 表明该行为并不总是一致,至少在开发环境下如此。

### 组件索引

组件修改完成、准备提交时,组件索引会在你创建 Pull Request 时由 CI 自动更新。GitHub Actions 工作流会检测组件变更并重建索引,必要时自动提交到你的 PR 分支。

如果想在本地手动重建索引用于测试:

```bash
uv run python scripts/build_component_index.py
```

## 构建与测试改动

准备提交时,提交前建议执行:

- `make lint`
- `make format_backend` 和 `make format_frontend` 分别对后端、前端代码运行格式化
- `make unit_tests` 运行(后端)单元测试(测试相关的更多信息见下文"一些怪癖")。

改动就绪后,建议将你的改动 rebase 到 `upstream` 的 `main` 分支之上,确保拿到的是最新代码!当然,如果你中途合并过他人的改动,可能需要重新 lint/format/unit_test。

作为最终验证,停掉后端和前端服务并运行 `make init`;这会做一次干净构建,UI 应在端口 `7860` 可用(因为内部执行了 `langflow run`)。新开一个**新的**浏览器标签页访问该服务,从 Components 列表中把新增/修改的组件拖到画布上,做最后检查。

## 提交、推送与 Pull Request

确认改动完成后,提交并推送到你自己的 fork(按上文操作,它就是 `origin`)。然后可以在 GitHub 网页界面或 IDE 中向项目仓库发起 Pull Request。

> [!TIP]
> 记住,如果启用了 pre-commit 钩子,需要以 `uv run git` 的形式运行 `git` 命令来激活所需的 Python 环境!

## 一些怪癖!

你可能会遇到一些奇怪的现象:

### 测试

- 后端测试 `src/backend/tests/unit/test_database.py` 在 `make tests` 下可能失败,但单独手动运行可以通过
  - 可以按顺序单独运行来验证:`uv run pytest src/backend/tests/unit/test_database.py`
- 还有其他测试目标:`integration_tests`、`coverage`、`tests_frontend`,但它们需要本文档未覆盖的额外配置。

### 会自己变化的文件

有些文件你没改它也会变:

- `src/backend/base/langflow/initial_setup/starter_projects` 下的文件在 `langflow run` 后会变;这些只是格式变化。提交或忽略都可以。
- `uv.lock` 和 `src/frontend/package-lock.json` 可能被 `make` 目标修改;个人贡献者不应提交这些变化。
  - 可以让 git 忽略它们:`git update-index --assume-unchanged uv.lock src/frontend/package-lock.json`
  - 需要恢复跟踪时:`git update-index --no-assume-unchanged uv.lock src/frontend/package-lock.json`
