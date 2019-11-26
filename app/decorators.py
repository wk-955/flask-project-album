from functools import wraps
from flask import Markup, flash, url_for, redirect, abort
from flask_login import current_user


def confirm_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.confirmed:
            msg = Markup(
                '请先确认您的帐户。'
                '没有收到电子邮件？'
                '<a class=“alert link”href=“%s”>重新发送确认电子邮件</a>' %
                url_for('auth.resend_confirm_email'))
            flash(msg, 'warning')
            return redirect(url_for('main.index'))
        return func(*args, **kwargs)
    return decorated_function


def permission_required(permission_name):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission_name):
                abort(403)
            return func(*func, **kwargs)
        return decorated_function
    return decorator


def admin_required(func):
    return permission_required('ADMINISTER')(func)
