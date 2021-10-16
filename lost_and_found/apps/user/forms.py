from flask_wtf import FlaskForm
from wtforms import DateField,SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Length


class user_login(FlaskForm):
    name=StringField(label='用户名',validators=[DataRequired()])
    password=PasswordField(label='密  码',validators=[DataRequired(),Length(6,18,message='密码必须在6~13位之间')])
    sub=SubmitField(label= '登录')

class user_register(FlaskForm):

    name=StringField('账号',validators=[DataRequired()])
    pwd=PasswordField(validators=[DataRequired(),Length(6,18,message='密码必须在6~13位之间')])
    pwd2=PasswordField(validators=[DataRequired(),Length(6,18,message='密码必须在6~13位之间'),EqualTo('pwd',message='两次输入密码不正确')])
    phone=StringField('手机号',validators=[DataRequired(),Length(min=11,max=11,message='手机号不符合规范')])
    sub = SubmitField(label='注册')

class user_release(FlaskForm):
    title=StringField('标题',validators=[DataRequired()])
    sub1=SubmitField('选择文件')