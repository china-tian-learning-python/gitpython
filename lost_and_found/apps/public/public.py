import os

from flask import Blueprint, session, render_template, request,redirect,url_for
import math
from lost_and_found.apps.user.sql import text_1, text_2, db,  News
path='D:/flask_开发/lost_and_found/static/file'
bp_bool=Blueprint('bp_bool',__name__)
@bp_bool.route('/')
def trsf():
    return redirect('/index')

@bp_bool.route('/index')
def fu():
    start=request.args.get('start')
    pag=4

    if start==None:
        start=1
    all_lists = db.session.query(text_1, text_2).join(text_2, text_1.id == text_2.id).order_by(
        text_1.times.desc()).all()
    if 'name' in session:

        all_list=db.session.query(text_1,text_2).join(text_2,text_1.id==text_2.id).order_by(text_1.times.desc()).offset((int(start)-1)*pag).limit(pag).all()

        return render_template('index.html', name=session['name'],all_list=all_list,start=start)
    all_list = db.session.query(text_1, text_2).join(text_2, text_1.id == text_2.id).all()
    name=None
    return render_template('index.html',all_list=all_list,name=name)


@bp_bool.route('/wei')
def wei():
    all_list = db.session.query(text_1, text_2).join(text_2, text_1.id == text_2.id).filter(text_2.bool=='未领取').all()
    return render_template('wa.html', name=session['name'], all_list=all_list)

@bp_bool.route('/yi')
def yi():
    all_list = db.session.query(text_1, text_2).join(text_2, text_1.id == text_2.id).filter(text_2.bool == '已领取').all()
    return render_template('yi.html', name=session['name'], all_list=all_list)


@bp_bool.route('/admins')
def admin():
    name=str(session['name'])
    all_list=db.session.query(text_2).filter(text_2.user_id==name).all()
    return render_template('admins.html',name=name,all_list=all_list)


@bp_bool.route('/tree')
def tree():
    id=request.args.get('id')
    ww=db.session.query(text_2,text_1).join(text_1,text_2.id==text_1.id).filter(text_2.id == id).all()
    wa=ww[0].text_1.phone
    newplace=os.path.join(path,wa)
    try:
        os.remove(newplace)
    except:
        pass
    db.session.query(text_2).filter(text_2.id==id).delete()
    db.session.query(text_1).filter(text_1.id==id).delete()
    db.session.commit()
    return redirect('/admins')




#  验证手机号一致，并发送验证码
@bp_bool.route('/news',methods=['GET','POST'])
def news():
    id = request.args.get('id')

    if request.method=='GET':
        return render_template('news.html',id=id)
    else:
        ids=request.form.get('id')
        name=request.form.get('name')
        phone=request.form.get('phone')

        wa=News(id=ids,name=name,phone=phone)
        db.session.add(wa)
        db.session.commit()
        # 重定向带/admin  路由 并修改物品属性

        wood=db.session.query(text_2).filter(text_2.id==ids).all()

        wood[0].bool='已领取'

        db.session.commit()


        return redirect('/wood?id={}'.format(ids))
