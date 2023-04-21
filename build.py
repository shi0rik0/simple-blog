import json
import os
import shutil
from pathlib import Path

import yaml

# 指定目录路径
src_path = Path('./articles')
dst_path = Path('./public/articles')
if dst_path.is_file():
    os.remove(dst_path)
elif dst_path.is_dir():
    shutil.rmtree(dst_path)
shutil.copytree(src_path, dst_path)


articles = []

# 遍历目录下所有文件
for path in dst_path.glob('*.yaml'):
    if not path.with_suffix('.md').is_file():
        print('warning: ')
        continue
    with open(path, encoding='utf-8') as f:
        obj = yaml.load(f, yaml.SafeLoader)
    articles.append({
        **obj,
        'link': path.stem
    })

articles.sort(key=lambda x: x['date'])
for i in articles:
    i['date'] = str(i['date'])

with open(dst_path / 'metadata.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f)
