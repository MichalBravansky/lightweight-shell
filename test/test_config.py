import unittest
import tempfile
import json
from config import Config


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+')
        config_data = {
            'test': {
                'named_args': {
                    'test': {
                        'type': 'STRING',
                        'name': 'test',
                        'value': 'test',
                    }
                },
                'positional_args': [
                    {'type': 'STRING', 'name': 'test', 'value': 'test'}
                ],
            }
        }
        self.config_data = config_data
        json.dump(config_data, self.temp_file)
        self.temp_file.close()
        self.config = Config(self.temp_file.name)

    def tearDown(self):
        self.temp_file.close()

    def test_get(self):
        self.assertIsNotNone(self.config.get('test'))

    def test_get_not_found(self):
        self.assertIsNone(self.config.get('no_match'))
