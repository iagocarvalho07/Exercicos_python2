import math
an = float(input('digite o angulo que voçe deseja '))
seno = math.sin(math.radians(an))
print('o angulo de {} tem o SENO de {} '.format(an, seno))
cos = math.cos(math.radians(an))
print('o angulo {} tem o coseno de {} '.format(an, cos))
tan = math.tan(math.radians(an))
print(' o angulo {} tem a tangente de {} '.format(an, tan))

