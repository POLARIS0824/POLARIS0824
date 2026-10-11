<picture>
  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/hero-dark-compact.svg">
  <source media="(max-width: 620px)" srcset="assets/hero-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <img src="assets/hero-light.svg" width="100%" alt="POLARIS · Android 客户端开发 · 寻找 Android 实习">
</picture>

我正在寻找 **Android 客户端开发实习**，围绕 Kotlin、Jetpack Compose 和 Android 数据层持续做项目。

目前重点开发 **FitLog**：把 Markdown 日记、Android 文件访问、编辑状态和数据分析连接起来。我关注功能背后的状态变化、数据保护和失败处理，也在 PetChat 中实践流式聊天与后台任务。

## <picture>  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/section-1-dark-compact.svg">  <source media="(max-width: 620px)" srcset="assets/section-1-light-compact.svg">  <source media="(prefers-color-scheme: dark)" srcset="assets/section-1-dark.svg">  <img src="assets/section-1-light.svg" width="100%" alt="项目中实践的能力"></picture>

<picture>
  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/skills-1-dark-compact.svg">
  <source media="(max-width: 620px)" srcset="assets/skills-1-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/skills-1-dark.svg">
  <img src="assets/skills-1-light.svg" width="100%" alt="Compose &amp; UI state: Screen states, navigation and Material 3. ViewModel + StateFlow in PetChat. · Storage &amp; recovery: SAF files, Room and DataStore. Conflict checks and draft recovery.">
</picture>

<picture>
  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/skills-2-dark-compact.svg">
  <source media="(max-width: 620px)" srcset="assets/skills-2-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/skills-2-dark.svg">
  <img src="assets/skills-2-light.svg" width="100%" alt="Network &amp; coroutines: Streaming responses and async work. Ktor / Retrofit / OkHttp in projects. · Tests &amp; build: Repository and ViewModel test cases. Gradle, lint and a CI workflow.">
</picture>

## <picture>  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/section-2-dark-compact.svg">  <source media="(max-width: 620px)" srcset="assets/section-2-light-compact.svg">  <source media="(prefers-color-scheme: dark)" srcset="assets/section-2-dark.svg">  <img src="assets/section-2-light.svg" width="100%" alt="精选项目"></picture>

<a href="https://github.com/POLARIS0824/FitLog">
<picture>
  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/project-1-dark-compact.svg">
  <source media="(max-width: 620px)" srcset="assets/project-1-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-1-dark.svg">
  <img src="assets/project-1-light.svg" width="100%" alt="FitLog. A Markdown-first training diary for Android. File access, editing, recovery and analysis data.">
</picture>
</a>

- **文件访问与编辑可靠性：**通过 SAF 连接 Markdown 文件夹；保存前核对文件指纹，遇到外部修改时提示冲突；保留草稿并提供恢复入口。
- **数据建模与边界：**将原文、解析候选和用户确认数据分开保存，关联来源文件与内容版本。项目仍在持续开发。

实现与测试：[文件读写与冲突检测](https://github.com/POLARIS0824/FitLog/blob/main/app/src/main/java/com/example/fitlog/data/vault/MarkdownDocumentRepository.kt) · [编辑与草稿状态](https://github.com/POLARIS0824/FitLog/blob/main/app/src/main/java/com/example/fitlog/editor/EditorViewModel.kt) · [分析数据与确认](https://github.com/POLARIS0824/FitLog/blob/main/app/src/main/java/com/example/fitlog/data/analysis/DiaryAnalysisRepository.kt) · [文件仓库测试](https://github.com/POLARIS0824/FitLog/blob/main/app/src/test/java/com/example/fitlog/data/vault/MarkdownDocumentRepositoryTest.kt)

<a href="https://github.com/POLARIS0824/PetChat">
<picture>
  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/project-2-dark-compact.svg">
  <source media="(max-width: 620px)" srcset="assets/project-2-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-2-dark.svg">
  <img src="assets/project-2-light.svg" width="100%" alt="PetChat. An Android pet-chat project with streaming AI replies. Compose UI, local history and background greetings.">
</picture>
</a>

- **异步请求与界面状态：**使用 ViewModel 和 StateFlow 管理聊天界面，通过流式接口逐步展示回复；用 Room 保存聊天记录。
- **Android 组件协作：**使用 DataStore 保存配置，WorkManager 调度问候任务；仓库包含会话、网络和 ViewModel 等测试用例。

实现与测试：[聊天 ViewModel](https://github.com/POLARIS0824/PetChat/blob/main/app/src/main/java/com/example/chat/ui/chat/PetChatViewModel.kt) · [流式网络处理](https://github.com/POLARIS0824/PetChat/blob/main/app/src/main/java/com/example/chat/data/repository/ChatApiService.kt) · [后台问候任务](https://github.com/POLARIS0824/PetChat/blob/main/app/src/main/java/com/example/chat/service/PetGreetingWorker.kt) · [ViewModel 测试](https://github.com/POLARIS0824/PetChat/blob/main/app/src/test/java/com/example/chat/ui/chat/PetChatViewModelTest.kt)

<a href="https://github.com/POLARIS0824/Quick-Switcher">
<picture>
  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/project-3-dark-compact.svg">
  <source media="(max-width: 620px)" srcset="assets/project-3-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/project-3-dark.svg">
  <img src="assets/project-3-light.svg" width="100%" alt="QuickSwitcher. A keyboard-first Chrome tab switcher adapted from Lumno. MRU tabs, thumbnail previews and hold-to-select input.">
</picture>
</a>

- **交互与开源代码阅读：**在 Lumno 开源实现基础上改造标签切换器，围绕按住选取、松开切换、缩略图和特殊页面行为调整交互。
- 作为客户端交互实践的补充项目；原始 MRU 与部分实现来自 Lumno，来源说明保留在项目 README 中。

实现与测试：[实现与来源说明](https://github.com/POLARIS0824/Quick-Switcher/blob/main/README.md) · [上游 Lumno](https://github.com/kubai087/lumno-extension)

## <picture>  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/section-3-dark-compact.svg">  <source media="(max-width: 620px)" srcset="assets/section-3-light-compact.svg">  <source media="(prefers-color-scheme: dark)" srcset="assets/section-3-dark.svg">  <img src="assets/section-3-light.svg" width="100%" alt="项目技术栈"></picture>

<picture>
  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/stack-dark-compact.svg">
  <source media="(max-width: 620px)" srcset="assets/stack-light-compact.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/stack-dark.svg">
  <img src="assets/stack-light.svg" width="100%" alt="项目技术栈：Kotlin, Java, JavaScript, Compose, ViewModel, Navigation 3, WorkManager, Room, DataStore, SAF, Coroutines / Flow, Ktor, Retrofit, OkHttp, JUnit, Git / Gradle">
</picture>

## <picture>  <source media="(max-width: 620px) and (prefers-color-scheme: dark)" srcset="assets/section-4-dark-compact.svg">  <source media="(max-width: 620px)" srcset="assets/section-4-light-compact.svg">  <source media="(prefers-color-scheme: dark)" srcset="assets/section-4-dark.svg">  <img src="assets/section-4-light.svg" width="100%" alt="联系与交流"></picture>

[GitHub](https://github.com/POLARIS0824) · [Android 项目](https://github.com/POLARIS0824/FitLog) · [项目交流](https://github.com/POLARIS0824/FitLog/issues)

欢迎通过 GitHub 项目 Issues 交流实现与设计。

<sub>主页按公开仓库的实现与测试源码整理。FitLog 持续开发中；项目状态与测试结果以各仓库记录为准。</sub>
