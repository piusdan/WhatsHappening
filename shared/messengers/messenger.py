from dataclasses import dataclass


@dataclass
class MessengerSetting():
    key: str
    service_name: str

@dataclass
class MessageConsumerSetting():
    listen_keys: [str]
    service_name: str

@dataclass
class BlobMessengerSetting(MessengerSetting):
    container_name: str = ""

    def __post_init__(self):
        self.container_name = self.service_name.lower()



class Messenger():
    def send_message(self, messenger_setting: MessengerSetting, data: any):
        raise NotImplementedError


