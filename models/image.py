from . import *


class Image(db.Document, ModelMixin):
    """
    数字病理图像
    """
    name = db.StringField(required=True)
    path = db.StringField(required=True)
    mark = db.ListField(db.EmbeddedDocumentField('mark'))
    report = db.ListField(db.EmbeddedDocumentField('report'))
    created_time = db.DateTimeField(default=datetime.datetime.now())

# created by Cai


class Mark(db.Document, ModelMixin):
    """
    图像标记
    """
    created_time = db.DateTimeField(default=datetime.datetime.now())
    update_time = db.DateTimeField(default=datetime.datetime.now())


class Report(db.Document, ModelMixin):
    """
    病理报告
    """
    text = db.StringField(required=True)
    created_time = db.DateTimeField(default=datetime.datetime.now())
    update_time = db.DateTimeField(default=datetime.datetime.now())
