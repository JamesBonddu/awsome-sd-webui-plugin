1. 使用GitHub REST API进行搜索。使用GitHub REST API搜索sd-webui相关内容,并获取搜索结果。具体的搜索URL可以是: `https://api.github.com/search/repositories?q=sd-webui&sort=stars&order=desc`。
2. 解析搜索结果,提取感兴趣的插件仓库信息。从搜索结果中,我们可以解析出每个仓库的名称、描述、创建者、星标数量等信息。
3. 按照我们讨论的格式整理插件信息。例如,对每个插件可以生成如下整理内容:
```md
### [sd-webui-plugin-name](https://github.com/user/sd-webui-plugin-name)
- 描述: 插件简短描述
- 作者: [@user]()
- 星标: [![stars](https://img.shields.io/github/stars/user/sd-webui-plugin-name.svg?style=social)](https://github.com/user/sd-webui-plugin-name)
- 项目地址: https://github.com/user/sd-webui-plugin-name
```
4. 生成完整的sd-webui插件清单,并以 Markdown 格式保存。

给出完整的代码示例，同时考虑有新的插件信息进来后如何进行更新，根据github api v3 考虑未在response中有header link 给出完整详细的代码, 同时考虑有新的插件信息进来后如何进行更新， 考虑编码格式为utf8, 优化代码并考虑时间和空间。
