from pyforms.basewidget import BaseWidget
from confapp import conf

from pyforms.controls import ControlButton
from pyforms.controls import ControlText
from pyforms.controls import ControlList

class SiteCrawlApp(BaseWidget):

    UID                  = 'site-crawl-app'
    TITLE                = 'Site crawl'

    LAYOUT_POSITION      = conf.ORQUESTRA_HOME

    ORQUESTRA_MENU       = 'left'
    ORQUESTRA_MENU_ICON  = 'browser'
    ORQUESTRA_MENU_ORDER = 0


    def __init__(self, *args, **kwargs):

        super(SiteCrawlApp, self).__init__(*args, **kwargs)

        self._url          = ControlText('Page url')
        self._getlinks_btn = ControlButton('Get links', default=self.___getlinks_btn_evt, label_visible=False)

        self._links_list   = ControlList('Links list', horizontal_headers=['Found links'])

        self.formset = ['_url', '_getlinks_btn', '_links_list']


    def ___getlinks_btn_evt(self):

        self._links_list.value = [
            ['Link1'],
            ['Link2']
        ]