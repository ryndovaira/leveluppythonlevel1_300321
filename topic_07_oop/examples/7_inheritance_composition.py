class Organ:
    """
    Класс Organ
    Поля:
        is_healthy - здоров или нет
        mass_g - масса (г)
    """

    def __init__(self,
                 is_healthy: bool,
                 mass_g: float):
        self.healthy = is_healthy
        self.mass_g = mass_g


class Heart(Organ):
    """
    Класс Heart
    Поля:
        blood_pressure - кровяное давление (тип tuple)
    Методы:
        listen_to - печатает различные звуки (здоровый и болезненный вариант)
    """

    def __init__(self,
                 is_healthy,
                 mass_g: float,
                 blood_pressure: tuple):

        super().__init__(is_healthy, mass_g)
        self.blood_pressure = blood_pressure

    def listen_to(self):
        if self.healthy:
            print("tok-tok-tok")
        else:
            print("bam-bam-bam")


class Eye(Organ):
    """
    Класс Eye
    Поля:
        visual_acuity - острота зрения (1.0 - идеально)
        colour - цвет глаз (строка)
    Методы:
        read_text - "читает" текст с учетом остроты зрения и здоровья
    """

    def __init__(self,
                 is_healthy: bool,
                 mass_g: int,
                 visual_acuity: float,
                 colour: str):

        super().__init__(is_healthy, mass_g)
        self.visual_acuity = visual_acuity
        self.colour = colour

    def read_text(self, text):
        if not self.healthy:
            return "I can't read!"
        elif self.visual_acuity == 1:
            return text
        else:
            return text[::2]


class Body:
    """
    Класс Body
    Поля:
        height_cm - высота (в см)
        age - возраст (годы)
    Методы:
        is_should_have_support - нужна ли помощь
    """

    def __init__(self,
                 l_eye_params: tuple,
                 r_eye_params: tuple,
                 h_params: tuple,
                 height: float,
                 age: int):
        self.eyes = (Eye(*l_eye_params),
                     Eye(*r_eye_params))
        self.heart = Heart(*h_params)
        self.height = height
        self.age = age

    def is_should_have_support(self):
        # если есть хотя бы 2 "проблемных" пункта, то нужна помощь

        problem_counter = 0

        for eye in self.eyes:
            if not eye.healthy or abs(eye.visual_acuity - 1.0) > 3.0:
                problem_counter += 1

        if not self.heart.healthy or abs(self.heart.blood_pressure[0] - self.heart.blood_pressure[1]) > 80:
            problem_counter += 1

        if self.age > 55:
            problem_counter += 1

        return problem_counter >= 2


if __name__ == '__main__':
    left_eye_params = (True, 10, 1.0, 'green')
    right_eye_params = (True, 11, 1.0, 'blue')
    heart_params = (False, 500, (120, 80))

    body = Body(left_eye_params, right_eye_params, heart_params, 180, 56)

    print(body.is_should_have_support())
