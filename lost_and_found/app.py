from flask_script import Manager

from lost_and_found.apps import create_app
from flask import render_template,request,url_for,session
app=create_app()
app.config['WTF_CSRF_SECRET_KEY ']='sfgopd;asmfnpalafnsoufh;afsf'
app.config['SECRET_KEY ']='oifjasf;lhfoamsfuheger'
'''
完善
    1.在二级页面中对接邮箱验证或者短信验证
    2.在注册页面中接入邮箱验证或者短信验证
    3.用户表，注册模块，信息表很大可能要更改
    4.在密码保存要做数据加密
    5.页面全面优化
    6.后期加入地方划分
    7.添加聊天功能
    8.添加日志功能
    9.添加内容管理功能，具有修改功能
        添加一个详情按钮，
        详情页面要用post请求  内容显示用文本框，并默认值从数据库中获取
    10.添加数据表的外键，让数据同步
    11.做一个数据一致，如果不存在数据同步，则自动删除
    
'''

'''
已实现功能：
    1.登录
    2.注册
    3.注销
    4.上传图片，具有发布功能
    5.二级页面
    6.按照物品的属性来分组
    7.内容管理功能 具有删除功能
    8.添加管理员页面
    9.添加管理员封号的功能
    10.添加管理员删除数据功能
    11.物品具有翻页功能
    
    
    
问题:
    1.并发问题
    
'''


manager = Manager(app)
if __name__ == '__main__':
    app.run(debug=True)