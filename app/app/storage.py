import logging
import os

log = logging.getLogger(__name__)


class Storage:
    def init_app(self, app):
        self.app = app
        self.create_all()
        try:
            self.validate()
        except Exception:
            raise

    def create_all(self):
        self.create_upload_folder()
        self.create_downloads_folder()
        self.create_html_templates_folder()

    def create_upload_folder(self):
        if not os.path.exists(self.app.config['UPLOAD_FOLDER']):
            log.debug("creating UPLOAD_FOLDER folder")
            os.makedirs(self.app.config['UPLOAD_FOLDER'])
            return
        log.debug("skipping UPLOAD_FOLDER creation, \
            folder already exists")  

    def create_downloads_folder(self):
        if not os.path.exists(self.app.config['DOWNLOADS_FOLDER']):
            log.debug("creating DOWNLOADS_FOLDER folder")
            os.makedirs(self.app.config['DOWNLOADS_FOLDER'])
            return
        log.debug("skipping DOWNLOADS_FOLDER creation, \
            folder already exists")

    def create_html_templates_folder(self):
        if not os.path.exists(self.app.config['HTML_TEMPLATES_FOLDER']):
            log.debug("creating HTML_TEMPLATES_FOLDER folder")
            os.makedirs(self.app.config['HTML_TEMPLATES_FOLDER'])
            return
        log.debug("skipping HTML_TEMPLATES_FOLDER creation, \
            folder already exists")

    def get_upload_folder(self):
        return self.app.config['UPLOAD_FOLDER']

    def get_downloads_folder(self):
        return self.app.config['DOWNLOADS_FOLDER']

    def get_html_templates_folder(self):
        return self.app.config['HTML_TEMPLATES_FOLDER']

    def validate(self): 
        if not os.path.exists(self.get_upload_folder()):
            log.error("UPLOAD_FOLDER folder does not exist, \
                cannot start web application")
            raise Exception("UPLOAD_FOLDER folder does not exist")
        if not os.path.exists(self.get_downloads_folder()):
            log.error("DOWNLOADS_FOLDER folder does not exist, \
                cannot start web application")
            raise Exception("DOWNLOADS_FOLDER folder does not exist")
        if not os.path.exists(self.get_html_templates_folder()):
            log.error("HTML_TEMPLATES_FOLDER folder does not exist, \
                cannot start web application")
            raise Exception("HTML_TEMPLATES_FOLDER folder does not exist")
