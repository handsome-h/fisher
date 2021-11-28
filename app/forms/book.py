from wtforms import Form, StringField
from wtforms.validators import Length, DataRequired


class SearchForm(Form):
    """搜索关键词验证器"""
    q = StringField(validators=[Length(min=1, max=30), DataRequired()], default='game')
