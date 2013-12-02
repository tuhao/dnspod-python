一个使用Python编写的，基于dnspod-api的工具。

家庭带宽多无固定IP地址，使得自己设置的域名指向的ip经常失效。
这个应用自动检测Wan口IP（公网IP）变化，并自动更新先前在https://www.dnspod.cn/Domain
上填写的域名记录中，指定的IP字段。

##使用：
1.首先，注册登录https://www.dnspod.cn/Domain
填写相关域名信息。
2.填写dnspod.conf配置文件中相关信息，email，password及域名名称是必须的。
3.运行start.py开始监控。
