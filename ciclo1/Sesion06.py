###########################################
# Semestre : 2019-1
# Curso : Fundamentos de Programacion
# Sesion : 06
#
# En esta session se ve la creacion de
# funciones personalizadas
#
###########################################

def suma(a, b):
    '''
    Esta funcion permita realizar la suma
    de 2 numeros
    :param a: primer valor
    :param b: segundo valor
    :return:
    '''
    t = a + b
    return int(t)


if __name__ == '__main__':
    a = 4
    b = 5
    s = suma(a,b)
    #print("la suma de %f mas  %f  es %f ", a, b, s)



