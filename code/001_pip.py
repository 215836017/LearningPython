print('pip常用命令')

# 标题： pip -- 包管理器，可以下载外在的库

'''
pip 命令格式
pip <command> [options]
'''

'''
pip常用命令
pip install xxx:   下载并安装xxx包， 并且默认是最新版本的xxx包   --- 安装的路径为：Python安装路径/Lib/site-packages
pip install xxx==(版本号)： 下载并安装指定版本号的xxx包，如果已经有其他版本的xxx包，则会先卸载，再安装。
pip uninstall xxx: 删除安装的xxx包

pip freeze -r requirements.txt:  把所有安装的包输出到文件requirements.txt中      ---- 文件不存在时会报错
或者  pip freeze > requirements.txt  把所有安装的包输出到文件requirements.txt中   ----  文件不存在时会自动创建文件 

生成 requirements.txt后，安装requirements.txt中所有指定的包时， 用如下命令：
pip install -r requirements.txt

pip list：列出所有安装的包

python -m  pip install --upgrade pip: 升级pip


'''
