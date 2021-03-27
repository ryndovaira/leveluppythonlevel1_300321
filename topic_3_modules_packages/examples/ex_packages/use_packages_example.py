import topic_3_modules_packages.examples.ex_packages.sound as sound
import topic_3_modules_packages.examples.ex_packages.sound.effects.echo as echo
from topic_3_modules_packages.examples.ex_packages.sound.filters import TYPE
from sound.formats import FORMAT   # Относительный импорт (не рекомендован)

print(__file__)

# print(topic_3_modules_packages.examples.ex_packages.sound.NAME)
print(sound.NAME)

print(sound.effects.echo)
print(echo.ECHO)
print(TYPE)
print(FORMAT)
