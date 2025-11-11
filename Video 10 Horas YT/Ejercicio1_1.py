#Diferencia en porcentaje entre el curso actual y los otros.
#Datos iniciales
promedio_otros_cursos = 4 * 60
minimo_otros_cursos = 2.5 * 60
maximo_otros_cursos = 7 * 60
grabacion_cruda_otros_cursos = 5 * 60

minimo_este_curso = 1.5 * 60
grabacion_cruda_este_curso = 3.5 * 60

#Calculos
#Diferencia en porcentaje entre el curso actual y el otro mas rapido
porcentaje_contra_el_mas_rapido = ((minimo_este_curso - minimo_otros_cursos) / minimo_otros_cursos) * 100

#Diferencia en porcentaje entre el curso actual y el otro mas lento
porcentaje_contra_el_mas_lento = ((minimo_este_curso - maximo_otros_cursos) / maximo_otros_cursos) * 100

#Diferencia en porcentaje entre el curso actual y el otro mas lento
porcentaje_contra_el_promedio = ((minimo_este_curso - promedio_otros_cursos) / promedio_otros_cursos) * 100

#Guardar en una lista la primera parte del ejercicio
ejercicio_a = []
ejercicio_a.extend([porcentaje_contra_el_mas_rapido,porcentaje_contra_el_mas_lento,porcentaje_contra_el_promedio])

#Segunda parte del ejercicio:
material_reducido_otros_cursos = ((promedio_otros_cursos - grabacion_cruda_otros_cursos) / grabacion_cruda_otros_cursos) * 100

material_reducido_este_curso = ((minimo_este_curso - grabacion_cruda_este_curso) / grabacion_cruda_este_curso) * 100

#Guardar en una lista la segunda parte del ejercicio
ejercicio_b = []
ejercicio_b.extend([material_reducido_otros_cursos,material_reducido_este_curso])

#Tercera parte del ejercicio
#Cambiar de valor el porcentaje negativo del primer elemento a positivo, para realizar las demas operaciones
ejercicio_a[0] = ejercicio_a[0] - (ejercicio_a[0] + ejercicio_a[0])

minutos = 10 * 60
minutos_equivalentes_otros = ((minutos * ejercicio_a[0]) / 100) + minutos
minutos_a_horas = minutos_equivalentes_otros / 60
horas_contra_el_mas_rapido = minutos_a_horas

#Cambiar de valor el porcentaje negativo del primer elemento a positivo, para realizar las demas operaciones
ejercicio_a[2] = ejercicio_a[2] - (ejercicio_a[2] + ejercicio_a[2])

minutos_equivalentes_promedio = ((minutos * ejercicio_a[2]) / 100) + minutos
minutos_a_horas_de_promedio = minutos_equivalentes_promedio / 60
horas_contra_el_promedio = minutos_a_horas_de_promedio

#10 horas de este curso equivalente al mas rapido
minutos_menos_porcentaje_mas_rapido = (minutos * ejercicio_a[0]) / 100 - minutos
#Cambio de negativo a positivo
minutos_menos_porcentaje_mas_rapido = minutos_menos_porcentaje_mas_rapido - (minutos_menos_porcentaje_mas_rapido + minutos_menos_porcentaje_mas_rapido)
horas_contra_el_mas_rapido_3 = minutos_menos_porcentaje_mas_rapido / 60

#10 horas de este curso equivalente el promedio
minutos_menos_porcentaje_promedio = (minutos * ejercicio_a[2]) / 100 - minutos
#Cambio de negativo a positivo
minutos_menos_porcentaje_promedio = minutos_menos_porcentaje_promedio - (minutos_menos_porcentaje_promedio + minutos_menos_porcentaje_promedio)
horas_contra_el_promedio_3 = minutos_menos_porcentaje_promedio / 60

#Guardar en una lista la tercera parte del ejercicio
ejercicio_c = []
ejercicio_c.extend([horas_contra_el_mas_rapido,horas_contra_el_promedio,horas_contra_el_mas_rapido_3,horas_contra_el_promedio_3])

#Resultados
print(ejercicio_a)
print(ejercicio_b)
print(ejercicio_c)