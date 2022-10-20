# 广州29th萤火虫自由行通过检测

# 写在前面
    本人代码能力几乎为0，此项目为一时兴起缝合怪，轻喷。🙇‍♂️
Special Thanks [0xJacky](https://github.com/0xJacky)

# 效果展示
![](https://raw.githubusercontent.com/MOLIzhang/Pass_check/main/IMG_4122.JPEG)

# 使用工具
+ Bark

# 使用方法
1.fork此项目  
2.在[广州29th萤火虫自由行查询页面](https://jinshuju.net/f/AVoQg6/s/Ya4vJd)输入手机号，复制结果页面URL并填写到secrets中，变量名为`URL`    
3.将自己的barktoken添加到secrets中，变量名为`BARKTOKEN`  
4.自行配置cron定时  

# ToDo-list
+ 邮箱推送

# 更新记录
+ 2022-10-21 实现github action推送，使用Bark。
