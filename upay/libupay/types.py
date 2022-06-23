from uuid import uuid4
from hashlib import md5
from dataclasses import dataclass


@dataclass
class RegCardRequest:
    card_cvv: str
    card_number: str
    card_exp_date: str
    card_holder_name: str
    holder_phone_number: str
    
    version: str = 1
    api_key: str = None
    notify_url: str = None
    access_token: str = None
    
    def with_access_token(self, username, password, api_key, notify_url):
        """AccessToken generator MD5(username+CardNumber+CardExDate+CardCVV+password)"""
        self.api_key = api_key
        self.notify_url = notify_url
        self.access_token = md5(
            f"{username}{self.card_number}{self.card_exp_date}{self.card_cvv}{password}"
            .encode("utf-8")).hexdigest()

        return self
    
    def to_dict(self):
        return {
            "Lang": "ru",
            "CardCVV": self.card_cvv,
            "Version": self.version,
            "NotifyUrl": self.notify_url,
            "CardNumber": self.card_number,
            "CardExDate": self.card_exp_date,
            "AccessToken": self.access_token,
            "StPimsApiPartnerKey": self.api_key,
            "CardHolderName": self.card_holder_name,
            "PhoneNumber": self.holder_phone_number,
        }


@dataclass
class CreateHoldRequest:
    amount: int
    card_token: str

    api_key: str = None
    region_id: str = None
    notify_url: str = None
    service_id: int = None
    hold_minute: int = None
    access_token: str = None
    subregion_id: str = None
    personal_account: str = None

    def with_access_token(self, username, password, api_key, notify_url):
        """AccessToken generator MD5(username+CardToken+ServiceId+personalAccount+AmountWithtiyin+password)"""
        self.service_id = 729
        self.hold_minute = 60
        self.api_key = api_key
        self.personal_account = "907377447"
        self.notify_url = None
        self.access_token = md5(
            f"{username}{self.card_token}{self.service_id}{self.personal_account}{self.amount}{password}"
            .encode("utf-8")).hexdigest()
    
        return self

    def to_dict(self):
        return {
            "Lang": "ru",
            "Version": 1,
            "HoldMinute": 60,
            "RegionId": None,
            "ServiceId": 729,
            "SubRegionId": None,
            "CardToken": self.card_token,
            "AmountInTiyin": self.amount,
            "PersonalAccount": 907377447,
            "NotifyUrl": self.notify_url,
            "AccessToken": self.access_token,
            "StPimsApiPartnerKey": self.api_key,
        }


@dataclass
class PayHoldRequest:
    amount: int
    hold_id: str

    trx_id: str = None
    api_key: str = None
    notify_url: str = None
    access_token: str = None

    def with_access_token(self, username, password, api_key, notify_url):
        """AccessToken generator MD5(username+HoldId+PartnerTrxId+password)"""
        self.trx_id = str(uuid4())
        self.api_key = api_key
        self.notify_url = notify_url
        self.access_token = md5(
            f"{username}{self.hold_id}{self.trx_id}{password}".encode(
                "utf-8")).hexdigest()

        return self

    def to_dict(self):
        return {
            "Lang": "ru",
            "Version": 1,
            "HoldId": self.hold_id,
            "PartnerTrxId": self.trx_id,
            "AccessToken": self.access_token,
            "StPimsApiPartnerKey": self.api_key
        }


@dataclass
class CheckHoldRequest:
    _type: str
    target: str

    api_key: str = None
    access_token: str = None

    def with_access_token(self, username, password, api_key, notify_url):
        """AccessToken generator MD5(username+Target+password)"""
        self.api_key = api_key
        self.notify_url = notify_url
        self.access_token = md5(
            f"{username}{self.target}{password}".encode("utf-8")).hexdigest()

        return self

    def to_dict(self):
        return {
            "Lang": "ru",
            "Version": 1,
            "Type": self._type,
            "Target": self.target,
            "AccessToken": self.access_token,
            "StPimsApiPartnerKey": self.api_key
        }


@dataclass
class CancelHoldRequest:
    hold_id: str

    api_key: str = None
    access_token: str = None

    def with_access_token(self, username, password, api_key, notify_url):
        """AccessToken generator MD5 (username + HoldId + password)"""
        self.api_key = api_key
        self.notify_url = notify_url
        self.access_token = md5(
            f"{username}{self.hold_id}{password}".encode("utf-8")).hexdigest()

        return self

    def to_dict(self):
        return {
            "Lang": "ru",
            "HoldId": self.hold_id,
            "AccessToken": self.access_token,
            "StPimsApiPartnerKey": self.api_key
        }