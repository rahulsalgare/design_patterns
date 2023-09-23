from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsButton(Button):
    def paint(self):
        print('Windows Button')


class MacButton(Button):
    def paint(self):
        print('Mac Button')


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


class WindowsCheckbox(Checkbox):
    def paint(self):
        print('Windows Checkbox')


class MacCheckbox(Checkbox):
    def paint(self):
        print('Mac Checkbox')


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class WinFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()


class MACFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class Application:

    def __init__(self, factory: GUIFactory):
        self.__button: Button
        self.__checkbox: Checkbox
        self.factory = factory

    def create_ui(self):
        self.__button = self.factory.create_button()
        self.__checkbox = self.factory.create_checkbox()

    def paint(self):
        self.__button.paint()
        self.__checkbox.paint()


def read_application_config_file():
    return {'OS': 'Windows'}


class ApplicationConfigurator:
    def main(self):
        config = read_application_config_file()

        if config['OS'] == "Windows":
            factory = WinFactory()
        elif config['OS'] == "Mac":
            factory = MACFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        app = Application(factory)
        app.create_ui()
        app.paint()


if __name__ == '__main__':
    configurator = ApplicationConfigurator()
    configurator.main()
