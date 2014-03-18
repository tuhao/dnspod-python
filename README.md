##用途：
基于dnspod-api,定期（60秒一次）自动更新DNSPOD域名A记录。

##原因：
家庭带宽多无固定IP地址，这个应用自动检测Wan口IP（公网IP）变化，并自动更新先前在https://www.dnspod.cn/Domain
上填写的A域名记录指定的IP字段。

##使用：
- 1. 首先，注册登录https://www.dnspod.cn/Domain
填写相关域名信息。
- 2. 填写dnspod.conf配置文件中相关信息，email，password及domain_name是必须的（域名如有多个请使用英文的,分隔）。
- 3. 利用crontab实现监控，格式为: * * * * * python start.py >> dnspod.log 2>&1 &
