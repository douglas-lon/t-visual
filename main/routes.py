from flask import render_template, request
from main import app
import pickle
import json

@app.route('/predict/', methods=['POST'])
def predict():
	data = json.loads(request.data.decode('utf8'))

	with open('./main/modelo.pkl', 'rb') as file:
		model = pickle.load(file)
	
		data = json.loads(request.data.decode('utf8'))
		result = apiHandleData(data)
		result = list(result.values())
		predict = model.predict([result])
		
	return str(predict)

@app.route('/resultado/',  methods=["GET", "POST"])
def resultado():
	if request.method == 'POST':

		with open('./main/modelo.pkl', 'rb') as file:
			model = pickle.load(file)
	
		formData = request.form
		json_result = dict(formData)
		result = handleData(json_result)
		result = list(result.values())
		predict = model.predict([result])

		mensagem = ''

		if predict == 1:
			mensagem = 'O paciente POSSUI tendência de problemas cardíacos'
		else:
			mensagem = 'O paciente NÃO POSSUI tendência de problemas cardíacos'

		return f"<h1> {mensagem} <h2>"

def apiHandleData(data):
	
	new ={
		"age": int(data['age']),
		"sex": int(handle_char(data['sex'], ['M', 'F'])),
		"chestPain": int(handle_char(data['chestPain'], ['TA', 'ATA', 'NAP', 'ASY'])),
		"restingBP": int(data['restingBP']),
		"cholesterol": int(data['cholesterol']),
		"fastingBS": 1 if int(data['fastingBS']) >= 120 else 0,
		"restingECG": int(handle_char(data['restingECG'], ['Normal', 'ST', 'LVH'])),
		"maxHR": int(data['maxHR']),
		"exerciseAngina": int(handle_char(data['exerciseAngina'], ['N', 'Y'])),
		"oldPeak": float(data['oldPeak']),
		"stSlope": int(handle_char(data['stSlope'], ['Up','Flat', 'Down'])) ,
	}
	
	return new

def handleData(data):
	
	new ={
		"age": int(data['idade']),
		"sex": int(handle_char(data['sexo'], ['M', 'F'])),
		"chestPain": int(handle_char(data['tipoDor'], ['TA', 'ATA', 'NAP', 'ASY'])),
		"restingBP": int(data['pressaoSanguinea']),
		"cholesterol": int(data['colesterolSerico']),
		"fastingBS": 1 if int(data['acucarSangue']) >= 120 else 0,
		"restingECG": int(handle_char(data['eletrocardiogramaRepouso'], ['Normal', 'ST', 'LVH'])),
		"maxHR": int(data['frequenciaCardiacaMax']),
		"exerciseAngina": int(handle_char(data['anginaExercicio'], ['N', 'Y'])),
		"oldPeak": float(data['depressaoST']),
		"stSlope": int(handle_char(data['inclinacaoST'], ['Up','Flat', 'Down'])) ,
	}
	
	return new
				
def handle_char(match,values):
	for i, x in enumerate(values):
		if match == x:
			return i