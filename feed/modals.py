from abc import ABC, abstractmethod


class Modal(ABC):
    PRIMARY = '-primary'
    SECONDARY = '-secondary'
    SUCCESS = '-success'
    DANGER = '-danger'
    WARNING = '-warning'
    INFO = '-info'
    LIGHT = '-light'
    DARK = '-dark'

    @property
    @abstractmethod
    def auth_items(self):
        pass

    @property
    @abstractmethod
    def non_auth_items(self):
        pass

    @property
    @abstractmethod
    def items(self):
        pass

    def __init__(self, iscreator):
        super().__init__()
        self.iscreator = iscreator


class Button:
    def __init__(
        self,
        outline=True,
        color=Modal.PRIMARY,
        text='Button',
        text_style=None,
        link='#',
    ):
        self._outline = outline
        self._color = color
        self._text = text
        self._text_style = text_style
        self._link = link

    @property
    def outline(self):
        return '-outline' if self._outline else ''

    @property
    def color(self):
        return self._color

    @property
    def text(self):
        return self._text

    @property
    def text_style(self):
        return self._text_style if self._text_style is not None else ''

    @property
    def link(self):
        return self._link

    def __repr__(self):
        return f'{self.text} button'


class PostModal(Modal):
    _creator_items = (
        Button(text='Edit'),
        Button(text='Copy link', color=Modal.SUCCESS),
        Button(text='Delete', color=Modal.DANGER),
    )

    _non_creator_items = (
        Button(text='Copy link', color=Modal.SUCCESS),
    )

    def __init__(self, iscreator=False):
        super().__init__(iscreator=iscreator)

    @property
    def auth_items(self):
        return self._creator_items

    @property
    def non_auth_items(self):
        return self._non_creator_items

    @property
    def items(self):
        return self.auth_items if self.iscreator else self.non_auth_items
