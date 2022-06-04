from zeep import helpers
from zeep.client import Client

from django.conf import settings

from upay.libupay.types import RegCardRequest


class UpayClient:

    def __init__(self, base_url: str, api_key: str, username: str,
                 password: str, notify_url: str) -> None:

        self.__api_key = api_key
        self.__username = username
        self.__password = password
        self.__base_url = base_url
        self.__notify_url = notify_url
        self.__base_client = Client(wsdl=self.__base_url)
        
        self.__configs: dict = {
            "api_key": self.__api_key,
            "username": self.__username,
            "password": self.__password,
            "notify_url": self.__notify_url
        }
    
    def reg_card(self, **kwargs):
        req = RegCardRequest(**kwargs).with_access_token(
            **self.__configs).to_dict()
        resp = self.__base_client.service.partnerRegisterCardIPS(req)
        
        return helpers.serialize_object(resp)

upay_client = UpayClient(
    **settings.UPAY_SERVICE.get('uclient')
)