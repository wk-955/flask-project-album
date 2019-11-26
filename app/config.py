import os

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class Operations:
    CONFIRM = 'confirm'
    RESET_PASSWORD = 'reset-password'
    CHANGE_EMAIL = 'change-email'


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'album'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ALBUM_ADMIN_EMAIL = 'wu@qq.com'

    ALBUM_PHOTO_PER_PAGE = 5
    ALBUM_COMMENT_PER_PAGE = 15
    ALBUM_NOTIFICATION_PER_PAGE = 20
    ALBUM_USER_PER_PAGE = 20
    ALBUM_SEARCH_RESULT_PER_PAGE = 20

    ALBUM_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    ALBUM_PHOTO_SIZE = {
        'small': 400, 'medium': 800
    }
    ALBUM_PHOTO_SUFFIX = {
        ALBUM_PHOTO_SIZE['small']: '_s',
        ALBUM_PHOTO_SIZE['medium']: '_m'
    }

    MAX_CONTENT_LENGTH = 3 * 1024 * 1024  # 文件不能超过3M

    AVATARS_SAVE_PATH = os.path.join(ALBUM_UPLOAD_PATH, 'avatars')
    AVATARS_SIZE_TUPLE = (30, 100, 200)

    DROPZONE_ALLOWED_FILE_TYPE = 'image'
    DROPZONE_MAX_FILE_SIZE = 3
    DROPZONE_MAX_FILES = 30
    DROPZONE_ENABLE_CSRF = True
    DROPZONE_DEFAULT_MESSAGE = '在此处放置文件或点击上传'
    DROPZONE_MAX_FILE_EXCEED = '最多只能上传三个文件'

    WHOOSHEE_MIN_STRING_LEN = 1

    BOOTSTRAP_SERVE_LOCAL = True

    ALBUM_MAIL_SUBJECT_PREFIX = '[Album]'

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('Album Admin', MAIL_USERNAME)