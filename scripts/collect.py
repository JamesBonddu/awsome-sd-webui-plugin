import requests
import time
import json

MAX_PAGE = 10
plugin_file = 'sd-webui-plugins.md'


class SDWebuiPlugin:
    def __init__(self):
        self.url = 'https://api.github.com/search/repositories'
        self.plugins = {}
        self.last_updated = None  # 上次更新时间

    def get_all_plugins(self):
        for page in range(1, MAX_PAGE + 1):
            params = {'q': 'sd-webui', 'sort': 'stars', 'order': 'desc',
                      'page': page, 'per_page': 100}
            r = requests.get(self.url, headers={'Accept': 'application/vnd.github.v3+json'},
                             params=params)
            r.encoding = 'utf-8'
            repos = json.loads(r.content.decode('utf-8'))

            for repo in repos['items']:
                name = repo['name']
                if name in self.plugins:
                    continue
                desc = repo['description']
                author = repo['owner']['login']
                stars = repo['stargazers_count']
                url = repo['html_url']
                self.plugins[name] = {'desc': desc, 'author': author,
                                     'stars': stars, 'url': url}
        # 获取本次更新时间
        self.last_updated = time.strftime('%Y-%m-%d %H:%M:%S')

    def generate_readme(self):
        md = ''
        for name, plugin in self.plugins.items():
            md += f'### [{name}]({plugin["url"]})\n'
            md += f'- 描述: {plugin["desc"]}\n'
            md += f'- 作者: [@{plugin["author"]}](https://github.com/{plugin["author"]}/>)\n'
            md += f'- 星标: {plugin["stars"]}\n'
            md += f'- 项目地址: {plugin["url"]}\n\n'

        if self.last_updated:
            md = f'#### {self.last_updated} 更新\n{md}'

        with open(plugin_file, 'w', encoding='utf-8') as f:
            f.write(md)

if __name__ == '__main__':
    plugin = SDWebuiPlugin()
    plugin.get_all_plugins()
    plugin.generate_readme()
