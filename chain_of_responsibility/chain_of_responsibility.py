from abc import ABC, abstractmethod


class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self):
        pass


class Component(ComponentWithContextualHelp):
    def __init__(self, tooltip_text):
        self.tooltip_text = tooltip_text
        self.container: Container = None

    def show_help(self):
        if self.tooltip_text:
            print('Tooltip text', self.tooltip_text)
        else:
            self.container.show_help()


class Container(Component):
    def __init__(self):
        self.children: list[Component] = []

    def add_child(self, child: Component):
        self.children.append(child)
        child.container = self


class Button(Component):
    pass


class Panel(Container):
    def __init__(self, tooltip_text=None, modal_help_text=None):
        super().__init__()
        self.modal_help_text = modal_help_text

    def show_help(self):
        if self.modal_help_text:
            print('Panel modal help text', self.modal_help_text)
        else:
            super().show_help()


class Dialog(Container):
    def __init__(self, tooltip_text=None, wiki_page_url=None):
        super().__init__()
        self.wiki_page_url = wiki_page_url

    def show_help(self):
        if self.wiki_page_url:
            print('Opening the wiki page...', self.wiki_page_url)
        else:
            super().show_help()


# Client code
class Application:
    def create_ui(self):
        dialog = Dialog('Budget reports', 'http://wiki.com')
        panel = Panel(modal_help_text='This panel does...')
        ok = Button('ok')
        ok.tooltip_text = 'This is an OK button that...'
        cancel = Button('cancel')
        panel.add_child(ok)
        panel.add_child(cancel)
        dialog.add_child(panel)
        return dialog

    def on_f1_key_press(self):
        component = self.get_component_at_mouse_coords()
        component.show_help()

    def get_component_at_mouse_coords(self):
        return self.create_ui()


if __name__ == "__main__":
    app = Application()
    app.on_f1_key_press()
