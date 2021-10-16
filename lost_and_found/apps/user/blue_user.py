from datetime import datetime
import os
import random
list1=['a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','v','w','x','y','z']
list2=[str(i) for i in range(10)]
list3=list1+list2
from flask import Blueprint, request, render_template, url_for, session, redirect, flash
from werkzeug.utils import secure_filename

from .sql import user, db, text_1, text_2
from lost_and_found.apps.user.forms import user_login, user_register
bp_user=Blueprint('bp_user',__name__)
path=r'D:\flask_开发\lost_and_found\static\file'



@bp_user.route('/login',methods=['GET','POST'])
def fun():
    froms=user_login(csrf_enabled=False)
    if request.method=='POST':
        if froms.validate_on_submit():
            username=int(froms.name.data)
            password=int(froms.password.data)

            wa = user.query.filter(user.id == username).all()
            if wa!=[]:
                if username==wa[0].id and password==wa[0].pwd and wa[0].bool=='false':
                    if wa[0].bool=='false':
                        now = datetime.now()
                        if wa[0].date >str(now):
                            return '你的账号已经被封号,解封时间:{}'.format(wa[0].date)

                        else:
                            session['name'] = username
                            # session.permanent=True
                            return redirect('/index')
                    else:
                        return "该用户已经永久封号"

                else:
                    return '密码或账号错误'
            else:
                if username==111 and password==123456:
                    return redirect(url_for('bp_admin.admin_index'))
        else:
            return render_template('login.html',froms=froms)
    else:
        return render_template('login.html',froms=froms)
@bp_user.route('/register',methods=['GET','POST'])
def fun2():
    form=user_register(csrf_enabled=False)
    if request.method == 'POST':
        if form.validate_on_submit():
            name=int(form.name.data)
            pwd=form.pwd.data
            pwd2=form.pwd2.data
            phone=form.phone.data
            bool='false'
            usernames=[  li.id for li in user.query.filter(user.id ==name).all()]
            if name not in usernames and name !=111:
                if pwd == pwd2:
                    data=user(id=name,pwd=pwd,phone=phone,bool=bool)
                    db.session.add(data)
                    db.session.commit()
                    return redirect('/login')
                else:

                    return '失败'
            else:
                return '账号已存在'
        else:

            return render_template('register.html', form=form)
    else:
        return render_template('register.html', form=form)




@bp_user.route('/release',methods=['GET','POST'])
def one():
    if request.method == 'GET':
        return render_template('one.html')
    else:
        title=request.form.get('title')
        file = request.files['file']
        phone = request.form.get('phone')
        text=request.form.get('caption')
        times=datetime.now()
        tr = random.sample(list3, random.randint(4, 9))
        id = ''.join(tr)

        filename = secure_filename(file.filename).split('.')[-1]

        number = random.randint(1, 300)
        filenames = datetime.now().strftime("%Y%m%d%H%M%S") + str(number) + '.' + filename
        if file:
            paths=os.path.join(path,filenames)

            user_id=session.get('name')
            bool='未领取'
            flash('发布成功')
            wa=text_1(id=id,title=title,user_id=user_id,phone=phone,place=filenames,text=text,times=times)
            wt=text_2(id=id,user_id=user_id,phone=phone,bool=bool)
            db.session.add_all([wa,wt])
            db.session.commit()
            file.save(paths)
            return redirect('/index')


@bp_user.route('/pop')
def pop():
    session.pop('name')
    return redirect('/index')



@bp_user.route('/wood')
def wood():
    id=request.args.get('id')

    all_list = db.session.query(text_1, text_2).join(text_2, text_1.id == text_2.id).filter(text_2.id==id).all()
    return render_template('show.html',all_list=all_list)

