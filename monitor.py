import psutil,time

class Monitor():

    cpu_data = [] #cpu值存放列表

    @classmethod
    def men(cls,max):
        '''内存'''
        val = psutil.virtual_memory().percent
        print(val)
        if val > max:
            cls.send_msg('内存使用率为{}%，超过了{}%，请关注'.format(val,max))

    @classmethod
    def cpu(cls,max):
        '''CPU'''
        val = psutil.cpu_percent()
        cls.cpu_data.append(val)
        print(cls.cpu_data)
        if len(cls.cpu_data) >=3:
            avg = sum(cls.cpu_data) / len(cls.cpu_data)
            if avg > max:
                cls.send_msg('CPU使用率为{}%，超过了{}%，请关注'.format(val,max))
            cls.cpu_data.pop(0)



    @classmethod#类方法
    def send_msg(cls,content):
        print(content)
        cls.mail(content)
        cls.wechat(content)


    @classmethod
    def mail(cls,content):
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr

        '''邮件回复'''
        nickname = '监控程序'
        sender ='912550157@qq.com' #发送邮箱
        password = 'qhfhjtujrsjrbbhg' #授权码
        receiver = '912550157@qq.com' #接收邮箱

        msg = MIMEText(content,'html','utf-8') #邮件内容
        msg['From'] = formataddr([nickname,sender]) #邮箱来源
        msg['Subject'] = '自动报警' #邮件标题

        server = smtplib.SMTP_SSL('smtp.qq.com',465) #邮箱服务器
        try:
            server.login(sender,password) #登录
            server.sendmail(sender,[receiver],msg.as_string()) #邮件内容转字符串
        except Exception as ex:
            print(ex)
        finally:
            server.quit()

    @classmethod
    def wechat(cls,content):
        '''微信回复'''
        # wechatpy pycrypto

        from wechatpy import WeChatClient
        import datetime

        client =WeChatClient('wxb66fd33ef90daa90','57dd07eed24da1364f26afeeece18feb') #测试号信息
        templates_id = 'fUvUlHrsWK2iI5EUYyO5pFw3rzXpODaPQLyqERUVhHM' #模板ID
        user_id = 'oK87O0cXYy6_IuD16dVe2voCouT8' #微信号

        data ={
            'msg':{"value":content,"color":"#173177"},
            'time':{"value":datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'), "color":"#173177"}
        }
        client.message.send_template(user_id,templates_id,data)

while True:
    Monitor.men(90)
    Monitor.cpu(90)
    time.sleep(5)
