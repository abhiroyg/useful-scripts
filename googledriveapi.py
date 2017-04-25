import httplib2
import logging
import os

from apiclient import discovery
from apiclient.http import MediaFileUpload
import argparse
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GDriveApi:
    """Class to perform google drive realted operations. """

    def __init__(self, config):
        self.LOCAL_FOLDER_PATH = config['folder_path']
        if self.LOCAL_FOLDER_PATH[-1] != '/':
            self.LOCAL_FOLDER_PATH += '/'

        credentials = self.get_credentials(config)
        http = credentials.authorize(httplib2.Http())
        self.DRIVE_SERVICE = discovery.build('drive', 'v3', http=http)
        self.PARENT_FOLDER_ID = None
        self.parent_folder = config['drive_folder']
        # self.create_parent_folder()

    def get_credentials(self, config):
        """Get valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """

        USER_CREDENTIALS_FILE = config["google_drive"]["user_credentials_json"]
        CLIENT_SECRET_FILE = config["google_drive"]["client_secret_json"]
        SCOPES = config["google_drive"]["scopes"]
        APPLICATION_NAME = config["google_drive"]["application_name"]
        try:
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None

        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       USER_CREDENTIALS_FILE)

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  # Needed only for compatibility with Python 2.6
                credentials = tools.run(flow, store)
            logger.info(msg='Storing credentials to {}'.format(credential_path))
        return credentials

    def drive_folder_creator(self, folder_name):
        """Show basic usage of the Google Drive API.

        Creates a Google Drive API service object and outputs the names and IDs
        for up to 10 files.
        """

        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if self.PARENT_FOLDER_ID:
            file_metadata['parents'] = [self.PARENT_FOLDER_ID]

        folder_data = self.DRIVE_SERVICE.files().create(body=file_metadata,
                                                        fields='id').execute()
        logger.info(msg='Folder created; Folder ID: %s' % folder_data.get('id').encode('utf-8'))
        return folder_data.get('id').encode('utf-8')

    def file_upload(self, png_file, folder_id):
        """Upload file to the specified folder.

        :return:
        """

        if not png_file.startswith(self.LOCAL_FOLDER_PATH):
            upload_file = self.LOCAL_FOLDER_PATH + png_file
        else:
            upload_file = png_file
            png_file = png_file.replace(self.LOCAL_FOLDER_PATH, '')

        media_body = MediaFileUpload(upload_file, mimetype='text/plain', resumable=True)
        body = {
            'name': png_file,
            'parents': [folder_id],
            'mimeType': 'image/png'
        }

        file_data = self.DRIVE_SERVICE.files().create(body=body, media_body=media_body).execute()
        logger.info(msg='File uploaded; File id {}'.format(file_data))

    def get(self, file_id):
        response = self.DRIVE_SERVICE.files().get(fileId=file_id).execute()
        print response

    def search_folder(self, folder_name, option=False):
        """List all the folders within the parent drive.

        :return:
        """

        if option:
            query = "mimeType='application/vnd.google-apps.folder' and name='{}'".format(
                folder_name)
        else:
            query = "mimeType='application/vnd.google-apps.folder' and name='{}' and '{}' in parents".format(
                folder_name,
                self.PARENT_FOLDER_ID)
        query = "name='{}'".format(folder_name)
        page_token = None
        while True:
            response = self.DRIVE_SERVICE.files().list(q=query,
                                                       spaces='drive',
                                                       fields='nextPageToken, files(id, name, parents)',
                                                       pageToken=page_token).execute()
            print response
            for file in response.get('files', []):
                # Process change
                print file
                logger.info(msg='Found Folder: %s (%s)' % (file.get('name'), file.get('id')))
                return file.get('id')
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        logger.info('Could not find the folder: {}'.format(folder_name))
        return None

    def create_parent_folder(self):
        """Create parent folder

        :return: Folder id
        """

        root = True
        folder_id = self.search_folder(self.parent_folder, root)
        if folder_id:
            self.PARENT_FOLDER_ID = folder_id
            logger.info(msg="Parent folder exists; id: {} and name: {}".format(folder_id, self.parent_folder))
        else:
            folder_id = self.drive_folder_creator(self.parent_folder)
            self.PARENT_FOLDER_ID = folder_id
            logger.info(msg="Parent folder created; id: {} and name: {}".format(folder_id, self.parent_folder))

if __name__ == '__main__':
    config = {"google_drive": {
        "scopes": 'https://www.googleapis.com/auth/drive',
        "application_name": "Drive API Python Quickstart",
        "client_secret_json": "client_secret.json",
        "user_credentials_json": "drive-python-quickstart.json"
    },
        "folder_path": "/home/nineleaps/Pictures/craigslist/",
        "drive_folder": "CraigslistScreenshots"
    }
    g = GDriveApi(config)
    # g.search_folder('http:__sfbay.craigslist.org_sfc_trp_6055151815.html?lang=en&cc=usdate:2017-03-22.png')
    g.search_folder('2017-03-22')
    # g.get('0B6F91w9SjBQ1X2JUQmZaLVVzUEE')
    g.get('0B6F91w9SjBQ1cm5yV09rNjNLX00')
