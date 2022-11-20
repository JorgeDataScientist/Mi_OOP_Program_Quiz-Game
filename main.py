from question_model import Preguntas
from data import question_data
from quiz_brain import QuizBrain

# NOTA: Leccion Nro 17

# TODO 2: Crear un Banco de preguntas. Una vez terminado, debe contener una lista de objeros de preguntas

banco_preguntas = []
for pregunta in question_data:
  texto_de_preguntas = pregunta['text']
  respuesta_de_pregunta = pregunta['answer']
  nueva_pregunta = Preguntas(p_texto= texto_de_preguntas, p_respuesta= respuesta_de_pregunta) #llamo a la funcion "Preguntas" y le paso los argumentos
  banco_preguntas.append(nueva_pregunta)

# print(len(banco_preguntas))
# print(banco_preguntas)

# TODO 3: realizar la pregunta al usuario, pedirle la respuesta y realizar la siguiente pregunta,

quiz = QuizBrain(banco_preguntas)

while quiz.tienes_mas_preguntas():
  quiz.p_siguiente()

print('El Quiz ha sido completado')
print(f'Tu Score es: {quiz.score}/{len(banco_preguntas)}')