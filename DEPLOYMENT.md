# 发布说明

本仓库已经配置 Quartz 5 和 GitHub Pages 自动发布。

## 首次启用

1. 打开 GitHub 仓库的 **Settings**。
2. 在侧边栏选择 **Pages**。
3. 将 **Source** 设置为 **GitHub Actions**。
4. 打开 **Actions**，等待 “Deploy Quartz site to GitHub Pages” 完成。
5. 访问 <https://lan-007.github.io/Notes-of-Dive-into-DeepLearning/>。

## 日常更新

只需编辑 `content` 目录中的 Markdown 文件并推送到 `main`。GitHub Actions 会自动重新构建和发布网站。

## 本地检查

提交前运行：

```shell
python scripts/check_markdown_links.py
```

如果需要重新统一标题、公式块、代码围栏和空行：

```shell
python scripts/normalize_markdown.py
```
