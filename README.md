##用途：
家庭带宽多无固定IP地址，这个应用定期检测Wan口IP（公网IP）变化，检测到变化后，自动更新用户先前在https://www.dnspod.cn/Domain上填写的A域名记录指定的IP字段。

##使用：
- 1. 首先，注册登录https://www.dnspod.cn/Domain
填写相关域名信息。
- 2. 填写dnspod.conf配置文件中相关信息，email，password及domain_name是必须的（域名如有多个请使用英文的,分隔）。
- 3. 利用crontab实现监控，格式为: * * * * * python start.py >> dnspod.log 2>&1 &
