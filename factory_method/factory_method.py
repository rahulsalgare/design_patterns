from abc import ABC, abstractmethod


class Dialog(ABC):
    @abstractmethod
    def create_button(self):
        pass

    def render(self):
        button = self.create_button()
        button.on_click()
        button.render()


class WindowDialog(Dialog):
    def create_button(self):
        return WindowsButton()


class WebDialog(Dialog):
    def create_button(self):
        return HTMLButton()


class Button(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self):
        pass


class WindowsButton(Button):
    def render(self):
        print('Windows Button')

    def on_click(self):
        print('Windows button clicked')


class HTMLButton(Button):
    def render(self):
        print('HTML Button')

    def on_click(self):
        print('HTML Button clicked')


def client_class(config: str):
    if config == "Windows":
        dialog = WindowDialog()
    elif config == "Web":
        dialog = WebDialog()
    else:
        raise Exception("Error! Unknown configuration")

    return dialog


if __name__ == '__main__':
    config = "Windows"
    dialog = client_class(config)
    dialog.render()
