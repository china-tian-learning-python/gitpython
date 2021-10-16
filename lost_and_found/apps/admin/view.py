from flask import Blueprint,redirect,url_for,request,render_template,flash,message_flashed
import datetime
from lost_and_found.apps.user.sql import user, db, text_1, text_2
import os


bp_admin=Blueprint('bp_admin',__name__)
path='D:/flask_开发/lost_and_found/static/file'
'''
管理员功能:
    1.具有封号的功能
    2.具有删除内容的功能
    3.首页具有滚动日志的功能
    
'''


@bp_admin.route('/admin')
def admin_index():
    wa=db.session.query(user).all()
    # message_flashed
    return render_template('admin_index.html',wa=wa)


@bp_admin.route("/admin/del")
def admin_del():
    id=request.args.get('id')
    db.session.query(user).filter(user.id==str(id)).delete()
    db.session.commit()
    return redirect('/admin')

@bp_admin.route("/admin/ban")
def admin_ban():
        global newtime, id
        times=request.args.get('time')
        if times==None:
            id=request.args.get('id')
            return render_template("admin_ban.html",id=id)
        else:

            if times=='1分钟':
                now = datetime.datetime.now()
                delta = datetime.timedelta(minutes=1)
                newtime = now + delta
                test = db.session.query(user).filter(user.id == id).all()
                test[0].date = newtime
                db.session.commit()
            elif times=='一天':
                now = datetime.datetime.now()
                delta = datetime.timedelta(hours=1)
                newtime = now + delta
                test=db.session.query(user).filter(user.id==id).all()
                test[0].date=newtime
                db.session.commit()
            elif times=='永久':
                test = db.session.query(user).filter(user.id == id).all()
                test[0].bool ='true'
                db.session.commit()
            flash("封号成功")
            return redirect('/admin')


@bp_admin.route("/admin/data")
def admin_data():
    all_list=db.session.query(text_1).order_by(text_1.times.desc()).all()
    return render_template('admin_data.html',all_list=all_list)

@bp_admin.route("/admin/data/del")
def admin_dels():
    id=request.args.get('id')
    wt=db.session.query(text_1).filter(text_1.id == str(id)).all()
    plase=wt[0].place
    new_plase=os.path.join(path,plase)
    try:
        os.remove(new_plase)
    except:
        pass
    db.session.query(text_1).filter(text_1.id==str(id)).delete()
    db.session.query(text_2).filter(text_2.id==str(id)).delete()
    db.session.commit()
    return redirect('/admin/data')
