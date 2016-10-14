# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyramid_storage.local import LocalFileStorage
from pyramid_storage.s3 import S3FileStorage


class StorageServiceException(Exception):
    pass


class StorageService(object):
    _storage = None

    def __init__(self, settings):
        storage_type = settings.get('storage.type', 'local')

        if storage_type == 'local':
            self._storage = LocalFileStorage.from_settings(
                settings, prefix='storage.')

        elif storage_type == 'aws':
            self._storage = S3FileStorage.from_settings(
                settings, prefix='storage.')

        else:
            raise StorageServiceException(
                'No implemented storage type: {0}'.format(storage_type))

    def save(self, file, folder='files'):
        return self._storage.save(file, folder=folder, randomize=True)
