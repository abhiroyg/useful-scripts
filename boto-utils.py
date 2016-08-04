import base64
import logging

from boto.s3.connection import S3Connection
from boto.s3.key import Key

from django.conf import settings


class Boto:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Opened s3 connection")
        self.conn = S3Connection(
            settings.AWS_ACCESS_KEY_ID,
            settings.AWS_SECRET_ACCESS_KEY)
        self.bucket = self.conn.get_bucket(
            settings.BUCKET_NAME, validate=False)

    def get_url(self, file_name_with_extension):
        url = 'https://{host}/{bucket}/{key}'.format(
            host=self.conn.server_name(),
            bucket=settings.BUCKET_NAME,
            key=file_name_with_extension)
        return url

    def upload(
            self, image_in_base64,
            file_name_with_extension, file_extension):
        k = Key(self.bucket)
        k.key = file_name_with_extension
        k.content_type = 'image/' + file_extension
        k.set_contents_from_string(
            base64.b64decode(image_in_base64), policy='public-read')
        k.set_acl('public-read')
        return self.get_url(file_name_with_extension)

    def delete(self, file_name_with_extension):
        self.bucket.delete_key(file_name_with_extension)
        return True

    def __del__(self):
        self.conn.close()
        self.logger.info("Closed s3 connection")
