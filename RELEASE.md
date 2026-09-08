# 发布 Langflow

> 🌐 本文档由 [langflow-ai/langflow](https://github.com/langflow-ai/langflow) 翻译,英文原版见原项目。

Langflow 采用**就绪即发布**的节奏,每个周期通常持续 4–6 周,视 QA 和稳定性需求而定。

## 目标

* 保持 `main` 分支快速迭代日常开发,同时确保功能成熟时能产出稳定的发布版本。
* 为 QA 和临门修 bug 提供一个隔离分支(发布候选,RC)。
* 尽可能保持线性、可读的提交历史。
* 确保发布代码在公开前经过充分测试。
* 尽量缩短关键 bug 的解决时间。

## 流程概览

### 1. OSS QA

创建包含 `langflow` 及相关 PyPI 包(如 `lfx`)的 OSS 发布候选(RC)分支。
在此期间:

* 手动执行 QA。
* Bug 修复合入 RC 分支。
* 新功能继续在 `main` 上开发。

这一步通常持续约一周。

### 2. Desktop QA

OSS QA 和 bug 修复完成后,创建 Desktop 发布候选。

* Desktop RC 基于最终版 OSS RC。
* 执行手动 QA。
* Bug 修复合入 Desktop RC。
* 新功能继续在 `main` 上开发。

这一步通常也持续约一周。

### 3. 发布

OSS 和 Desktop 的 QA、bug 修复都完成后:

* 从各自的 RC 分支切出最终发布版本。
* 发布时间与 Langflow 的 DevRel 团队协调。
* 发布后至少 24 小时内,需持续关注 Discord、GitHub 及其他支持渠道的关键 bug 报告。

### 4. 发布产物

发布工作流会自动发布以下产物:

* **PyPI 包:**
  * `langflow` - 包含全部集成的主包
  * `langflow-base` - 不含集成的核心框架
  * `lfx` - 轻量级执行器 CLI
  * `langflow-sdk` - 用于编程访问的 SDK(有更新时)

* **Docker 镜像:**
  * `langflowai/langflow` - 完整 Langflow 镜像
  * `langflowai/langflow-backend` - 仅后端镜像(独立发布)
  * `langflowai/langflow-frontend` - 仅前端镜像(独立发布)
  * `langflowai/langflow-ep` - 企业版镜像(独立发布)
  * `langflowai/langflow-base` - 不含集成的基础镜像

**注意:** 后端、前端和企业版镜像与主镜像分开发布;即使主版本已存在于 Docker Hub,这些镜像仍会构建。

## 分支模型

| 分支 | 用途 | 合并策略 |
| --- | --- | --- |
| **`main`** | 集成分支。所有功能 PR 默认以此为目标。 | **Squash & Merge**(线性历史) |
| **`release-X.Y.Z`**<br>(如 `release-1.4.3`) | 临时 RC 分支。仅在发布周期内活跃。接受带 `type:release` 标签的 QA 和阻塞性 bug PR。 | 分支内 **Squash & Merge**。<br>最终合回前先 rebase 到 **`main`**。 |

## 发布步骤

### 1. 切出发布候选分支

```sh
git checkout main && git pull          # 确保本地 main 是最新
git checkout -b release-X.Y.Z          # 创建新的发布候选分支
git push -u origin release-X.Y.Z       # 推送 RC 分支到远端
```

### 2. 向 RC 应用 bug 修复

1. 照常创建功能分支。
2. 发起以 `release-X.Y.Z` 为目标的 GitHub PR。
3. 正常评审并批准。
4. 评审通过后合入 RC 分支。

### 3. 审查回归日志

打标签前,检查 `regressions/X.Y.x.yaml`,确认没有未处理的 `blocking` 条目。
如存在 `blocking` 条目,必须完成签核。

完整的 schema 和条目录入说明见 [regressions/README.md](./regressions/README.md)。

### 4. 最终发布

```sh
git checkout release-X.Y.Z && git pull # 确保 RC 分支最新
git tag vX.Y.Z                         # 创建最终发布标签
git push origin vX.Y.Z                 # 推送标签到远端
```

### 5. 将 RC 合回 main

```sh
git checkout main
git merge --ff-only release-X.Y.Z      # 快进 main 以包含 RC 改动
```

## 合并策略

1. 全程使用 **Squash & Merge**,保证原子提交和干净的历史。

2. RC 存续期间,定期与 main 重新同步:

   ```sh
   git checkout release-X.Y.Z
   git fetch origin
   git rebase origin/main
   ```

   *这样可以尽早解决冲突,同时保持线性历史。*

3. 最终合回必须只允许 fast-forward。如无法满足,先把 RC rebase 到 `main` 再合并。

## 版本与标签

* 遵循[语义化版本](https://semver.org):`MAJOR.MINOR.PATCH`。
* RC 标签使用 `-rc.N`,如 `v1.8.0-rc.1`。
* **所有标签必须以 `v` 开头**(例如 `v1.9.1`,而不是 `1.9.1`)。
  * 发布工作流会校验该格式,拒绝缺少 `v` 前缀的标签。
  * 重复标签(例如 `1.8.3` 和 `v1.8.3` 并存)会导致 GitHub 生成发布说明时选错比对基准,产出不完整的变更日志。
  * 工作流会自动检查并阻止重复标签。

## LFX 兼容性

Langflow 和 LFX 共享**major.minor 版本线**。兼容性约定是:

> **LFX X.Y.N 保证兼容任何从 Langflow X.Y.M 导出的 Flow。**

补丁版本(`N` 和 `M`)相互独立——LFX 打补丁不需要 Langflow 同步发补丁,反之亦然。

### 版本管理

`make patch v=X.Y.Z` 会同时更新以下四个产物:

| 产物 | 版本设为 |
|---|---|
| `langflow` | `X.Y.Z` |
| `langflow-base` | `0.Y.Z` |
| `lfx` | `X.Y.Z` |
| 前端 | `X.Y.Z` |

### 发布 LFX 补丁版本

使用 `scripts/release-lfx.sh <version>`。如果 LFX 的 minor 版本与当前 Langflow 的 minor 版本不一致(会违反兼容性约定),脚本会给出警告。警告不是硬性阻断——同一 minor 内的纯补丁 LFX 发布是预期内且允许的。

### 对用户的影响

用户可以在 `requirements.txt` 中固定 `lfx~=X.Y.0`,以获取某个 Langflow minor 下所有兼容的 LFX 补丁版本。

### 从 lfx 0.5.x 迁移到 1.10.0

LFX 已从独立的 `0.5.x` 版本线重新对齐到 Langflow 的 `major.minor` 版本线,版本号从 `0.5.0` 一步跳到 `1.10.0`。这只是版本编号的调整,不是 95 个 minor 的功能大变动。这次跳变会影响下游的版本固定,而 pip 和 uv 都不会给出提示——所以必须在发布公告中明确说明,而不只是写在这里:

- `lfx==0.5.x` 或 `lfx<1.0` 的固定**不会**升级(有意为之——这类部署保持原状)。
- `lfx>=0.5,<1` 的固定**不会**升级。
- `lfx>=0.5` 这种没有上限的固定**会**在下次安装时拉取 `1.10.0`——一次毫无预警的大跳变。

今后请固定为 `lfx~=X.Y.0`(例如 `lfx~=1.10.0`),这样既能跟踪某个 Langflow minor 下的兼容补丁,又不会悄悄跨过 minor 版本线。

## 角色

| 角色 | 职责 |
| --- | --- |
| **发布负责人**(每周期轮换) | 负责时间线、切分支、打标签、合回。 |
| **PR 作者** | 确保测试通过;必要时在 RC 中给 PR 加 `type:release` 标签。 |
| **CI** | 测试失败或缺少标签时阻止合并。 |

## FAQ

### 会把 main 合进 RC 吗?

不会。始终把 RC rebase 到 `main` 上,以保持线性历史。

### 分支删除能自动化吗?

还不能——合回和清理都是手动操作。

### 时间线有多灵活?

非常灵活。QA 和稳定化阶段可以按质量需要延长。
