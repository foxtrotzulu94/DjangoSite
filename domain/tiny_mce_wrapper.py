from django.utils import translation
from wagtailtinymce.rich_text import TinyMCERichTextArea
from django.conf import settings

class TinyMCEWrapper(TinyMCERichTextArea):
    def __init__(self, *args, **kwargs):
        translation.trans_real.activate(settings.LANGUAGE_CODE)
        super(TinyMCEWrapper, self).__init__(*args, **kwargs)