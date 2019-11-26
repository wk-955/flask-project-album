from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, HiddenField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, Regexp

from app.models import User


class EditProfileForm(FlaskForm):
    name = StringField('名字', validators=[DataRequired(), Length(1, 30)])
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    website = StringField('网站', validators=[Optional(), Length(0, 255)])
    location = StringField('城市', validators=[Optional(), Length(0, 255)])
    bio = TextAreaField('个性签名', validators=[Optional(), Length(0, 120)])
    submit = SubmitField()

    def validate_username(self, field):
        if field.data != current_user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名早已存在.')


class UploadAvatarForm(FlaskForm):
    image = FileField('上传', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], '文件必须是jpg或png格式')
    ])
    submit = SubmitField()


class CropAvatarForm(FlaskForm):
    x = HiddenField()
    y = HiddenField()
    w = HiddenField()
    h = HiddenField()
    submit = SubmitField('裁剪')


class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField()

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('邮箱早已注册.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[DataRequired(), Length(4, 128), EqualTo('password2')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('提交')


class NotificationSettingForm(FlaskForm):
    receive_comment_notification = BooleanField('新评论')
    receive_follow_notification = BooleanField('新关注者')
    receive_collect_notification = BooleanField('新收藏者')
    submit = SubmitField('提交')


class PrivacySettingForm(FlaskForm):
    public_collections = BooleanField('公开我的收藏')
    submit = SubmitField('确定')


class DeleteAccountForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('确定')

    def validate_username(self, field):
        if field.data != current_user.username:
            raise ValidationError('用户名错误.')