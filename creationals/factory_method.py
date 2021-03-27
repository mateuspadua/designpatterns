from abc import ABC, abstractmethod


class LanguageAbstract(ABC):
    @abstractmethod
    def translate(self) -> str:
        pass


class Portuguese(LanguageAbstract):
    translations = {"dog": "cachorro", "squirrel": "esquilo"}

    def translate(self, msg):
        return self.translations.get(msg)


class Spanish(LanguageAbstract):
    translations = {"dog": "perro", "squirrel": "ardilla"}

    def translate(self, msg):
        return self.translations.get(msg)


class French(LanguageAbstract):
    translations = {"dog": "chien", "squirrel": "écureuil"}

    def translate(self, msg):
        return self.translations.get(msg)


class LanguageFactory:
    def __init__(self):
        self._builders = {}

    def register_builder(self, key, builder):
        self._builders[key] = builder

    def create(self, key, **kwargs) -> LanguageAbstract:
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder(**kwargs)


factory = LanguageFactory()
factory.register_builder("portuguese", Portuguese)
factory.register_builder("spanish", Spanish)
factory.register_builder("french", French)

portuguese = factory.create("portuguese")
spanish = factory.create("spanish")
french = factory.create("french")

print(f"Em português: {portuguese.translate('squirrel')}")
print(f"Em espanhol: {spanish.translate('squirrel')}")
print(f"Em francês: {french.translate('squirrel')}")
