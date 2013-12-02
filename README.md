基于dnspod-api的工具,自动更新DNSPOD域名A记录。

家庭带宽多无固定IP地址，这个应用自动检测Wan口IP（公网IP）变化，并自动更新先前在https://www.dnspod.cn/Domain
上填写的A域名记录指定的IP字段。

##使用：
- 1. 首先，注册登录https://www.dnspod.cn/Domain
填写相关域名信息。
- 2. 填写dnspod.conf配置文件中相关信息，email，password及域名名称是必须的。
- 3. 运行start.py开始监控。
