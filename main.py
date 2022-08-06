from translate import Translator

from greetings import greetings


translator = Translator(to_lang='pt')

for greeting in greetings:
    print(translator.translate(greeting).capitalize())
