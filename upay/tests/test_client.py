import json

from random import randint
from unittest import TestCase

from django.conf import settings

from rest_framework.status import HTTP_200_OK
from rest_framework.test import RequestsClient

from upay.libupay.uclient import UpayClient


class UpayClientTestCase(TestCase):
    __SUCCESS = 'OK'
    __STATUS_CODE = HTTP_200_OK
    
    def setUp(self) -> None:
        self.test_card: dict = {**settings.UPAY_SERVICE.get('test_cards')}
        self.upay_client: object = UpayClient(**settings.UPAY_SERVICE.get('uclient_test'))

        self.path_list = {
            'reg-card': 'http://localhost:8000/v1/reg-card/',   
        }
        
        self.client = RequestsClient()    

        
    def test_reg_card(self) -> None:
        self.test_card['client_id'] = randint(1, 99)
        resp = self.client.post(url=self.path_list['reg-card'], data=self.test_card)
        data = json.loads(resp._content)
        
        self.assertTrue(data.get('ConfirmUrl'))
        self.assertEquals(resp.status_code, self.__STATUS_CODE)
        self.assertAlmostEqual(data.get('Result').get('code'), self.__SUCCESS)