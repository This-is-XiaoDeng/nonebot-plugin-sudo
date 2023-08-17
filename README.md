<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-sudo

_✨ 使用其他用户身份执行命令 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/This-is-XiaoDeng/nonebot-plugin-sudo.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-sudo">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-sudo.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

<!--

这是一个 nonebot2 插件项目的模板库, 你可以直接使用本模板创建你的 nonebot2 插件项目的仓库

模板库使用方法:
1. 点击仓库中的 "Use this template" 按钮, 输入仓库名与描述, 点击 "  Create repository from template" 创建仓库
2. 在创建好的新仓库中, 在 "Add file" 菜单中选择 "Create new file", 在新文件名处输入`LICENSE`, 此时在右侧会出现一个 "Choose a license template" 按钮, 点击此按钮选择开源协议模板, 然后在最下方提交新文件到主分支
3. 全局替换`This-is-XiaoDeng`为仓库所有者ID; 全局替换`nonebot-plugin-sudo`为插件名; 全局替换`nonebot_plugin_sudo`为包名; 修改 python 徽标中的版本为你插件的运行所需版本
4. 修改 README 中的插件名和插件描述, 并在下方填充相应的内容

配置发布工作流:
1. 前往 https://pypi.org/manage/account/#api-tokens 并创建一个新的 API 令牌。创建成功后不要关闭页面，不然你将无法再次查看此令牌。
2. 在单独的浏览器选项卡或窗口中，[打开 Actions secrets and variables 页面](./settings/secrets/actions)。你也可以在 Settings - Secrets and variables - Actions 中找到此页面。
3. 点击 New repository secret 按钮，创建一个名为 `PYPI_API_TOKEN` 的新令牌，并从第一步复制粘贴令牌。

触发发布工作流:
推送任意 tag 即可触发。

创建 tag:

    git tag <tag_name>

推送本地所有 tag:

    git push origin --tags

-->

## 📖 介绍

XDbot2 SUDO 插件独立版，允许使用其他用户身份执行命令

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-sudo

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-sudo
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-sudo
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-sudo
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-sudo
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_sudo"]

</details>

## ⚙️ 配置

在 nonebot2 项目的`.env`文件中添加下表中的必填配置

| 配置项     | 必填 | 默认值 | 说明 |
|:---------:|:----:|:----:|:----:|
| `SUDOERS` | 是 | 无 | 可以使用 sudo 指令的用户 |
| `SUDO_INSERT_CMDSTART` | 否 | `0` | 是否自动插入指令前缀 |

## 🎉 使用

> 仅在 Onebot V11 适配器下测试可用，暂不支持 sudo 嵌套

### 指令表

| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| `sudo <uin> <消息...>` | SUDOER | 否 | 无限制 | 以用户`<uin>`的身份执行`<消息...>` |

### 效果图

待补充
