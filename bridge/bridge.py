from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def is_enabled(self):
        pass

    @abstractmethod
    def enable(self):
        pass

    @abstractmethod
    def disable(self):
        pass

    @property
    @abstractmethod
    def volume(self):
        pass

    @volume.setter
    @abstractmethod
    def volume(self, percent):
        pass

    @property
    @abstractmethod
    def channel(self):
        pass

    @channel.setter
    @abstractmethod
    def channel(self, channel):
        pass


class Tv(Device):
    def __init__(self):
        self._volume = 0
        self._channel = 0
        self._enabled = False

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, channel):
        self._channel = channel

    def is_enabled(self):
        return self._enabled

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False


class RemoteControl:
    def __init__(self, device):
        self._device: Device = device

    def toggle_power(self):
        if self._device.is_enabled():
            self._device.disable()
        else:
            self._device.enable()

    def volume_down(self):
        self._device.volume -= 1

    def volume_up(self):
        self._device.volume += 1

    def channel_down(self):
        self._device.channel -= 1

    def channel_up(self):
        self._device.channel += 1


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self._device.volume = 0


if __name__ == '__main__':
    tv = Tv()
    remote = RemoteControl(tv)
    print(tv.is_enabled())
    remote.toggle_power()
    print(tv.is_enabled())

    print(tv.volume)
    remote.volume_up()
    remote.volume_up()
    remote.volume_up()
    remote.volume_up()
    print(tv.volume)
