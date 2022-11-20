# TODO 3.1: Creo la clase 'QuizBrain' que tendra dos atributos:
#  a)Tendra un atributo 'numero_pregunta' que va a mantener un registro de la pregunta en la que el usuario esta actualmente.
#  Vamos a usar ese numero para pasar por la lista de preguntas, que sepasara a este objeto 'QuizBrain' cuando se inicialice.
#  b)El segundo metodo sera 'lista_preguntas', que sacara la pregunta de la lista, dependiendo del numero de pregunta actual
#  en el que nos encontremos


class QuizBrain:
  def __init__(self, p_lista):
    self.numero_pregunta = 0
    self.score = 0
    self.lista_preguntas = p_lista


  # TODO 3.3: Bucle que termina cuando se terminan las preguntas
  def tienes_mas_preguntas(self):
    return self.numero_pregunta < len(self.lista_preguntas)


  # TODO 3.2: Metodo para realizar la siguiente pregunta.
  #  a) Va a conseguir la pregunta actual

  def p_siguiente(self):
    p_actual = self.lista_preguntas[self.numero_pregunta]
    self.numero_pregunta += 1
    r_usuario = input(f'Q.{self.numero_pregunta}: {p_actual.texto} (True/False): ') #guardo respuesta de usuario para usar en 'chequear_respuesta'
    self.chequar_respuesta(r_usuario, p_actual.respuesta)

  # TODO 3.4: Verificar y contar si la respuesta es correcta o incorrecta

  def chequar_respuesta(self, r_usuario, r_correcta):
    if r_usuario.lower() == r_correcta.lower():
      self.score += 1
      print('SI, es Correcto 👍')
    else:
      print(f'NO, es {r_correcta} 👎')


    print(f'Tu score es de {self.score}/{self.numero_pregunta}')
    print('\n')