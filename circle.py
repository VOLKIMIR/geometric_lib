import math


def area(r):
    '''
    Возращает площадь окружности на основе её радиуса r.

        Параметры:
            r (float): радиус окружности.

        Возращаемое значение:
            float: площадь окружности, вычисляемая по формуле -> math.pi * r * r
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возращает периметр окружности на основе её радиуса r.

        Параметры:
            r (float): радиус окружности.

        Возращаемое значение:
            float: периметр окружности, вычисляемый по формуле -> 2 * math.pi * r
    '''
    return 2 * math.pi * r

