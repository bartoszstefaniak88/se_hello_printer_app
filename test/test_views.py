import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


XML_EXP = "<greetings><name>Natalia</name><msg>Hello World!</msg></greetings>"


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        imie = "Natalia"
        expected = {"imie": imie, "msg": "Hello World!"}
        rv = self.app.get('/?output=json&imie=' + imie)
        js = json.loads(rv.data)
        self.assertEqual(expected["imie"], js["imie"])
        self.assertEqual(expected["msg"], js["msg"])

    def test_msg_with_xml_output(self):
        rv = self.app.get('/?output=xml')
        self.assertEquals(XML_EXP, rv.data)

    def test_msg_with_output_name(self):
        imie = 'Bartosz'
        rv = self.app.get('/?name=' + imie + '&output=json')
        self.assertEquals('{"imie": ' + '"' + imie + '"' +
                          ', "msg": "Hello World!"}', rv.data)
