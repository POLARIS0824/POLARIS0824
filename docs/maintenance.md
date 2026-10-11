# 主页维护

这份主页面向 Android 客户端实习，优先展示 FitLog 和 PetChat 的具体实现。

## 更新

1. 编辑根目录 `profile.json` 中的介绍、项目文案和技术栈。
2. 运行 `python tools/build_profile.py`。只需要 Python 3 标准库。
3. 查看生成的 `preview.html`，检查电脑和手机尺寸、浅色和深色主题。
4. 将 `README.md`、`profile.json` 与生成的 `assets/` 一起提交。

需要公开求职邮箱时，在 `profile.json` 的 `contact_email` 填写你希望公开的地址，重新生成即可。不要填私密账号信息、密钥或令牌。

SVG 图形由代码生成，没有外部字体、外部脚本或第三方图片依赖。动画通过 SVG 内的 CSS 运行；系统开启减少动态效果时会暂停。卡片布局在 620px 以下切换为手机版本。GitHub 的实际图片与 Markdown 渲染可能与本地预览略有差异。

## 内容依据

审阅日期：2026-10-11。能力文案依据公开仓库默认分支的源码与测试文件；没有将本次源码检查写成测试通过、性能测量或真机验收结果。

- FitLog：`main`，检查时提交 `4bcc2ed531691fa49cf03bd10e89458c351559c0`。
- PetChat：`main`，检查时提交 `9907895f27915972c7dc8c066924bcc76b0368ac`。
- Quick-Switcher：`main`，检查时提交 `2d3f512bf85a74c19bac5ce134005baf7b99d862`。

README 的项目描述保留了源码入口，便于核对。Quick-Switcher 按其 README 标为基于 Lumno 改造的项目。未将 Fork 项目写成原创成果。

## 设计参考

模块化 SVG 卡片、深浅色主题和手机版本的组织方式参考 [abhixv 的主页](https://github.com/abhixv)。本仓库的图形、动画路径、配色和生成代码为新制作，未复制其 SVG 或字体数据。
