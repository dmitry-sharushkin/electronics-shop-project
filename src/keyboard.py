from src.item import Item


class MixinLanguage:
    LANGUAGES = {
        'EN': 'RU',
        'RU': 'EN'
    }

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language in self.LANGUAGES:
            self._language = self.LANGUAGES[self._language]
        return self


class Keyboard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self._language = 'EN'
