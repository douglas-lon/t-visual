# Rodando em [http://douglasbr.pythonanywhere.com/predict/](http://douglasbr.pythonanywhere.com/predict/)

Aceita json com os seguintes parâmetros:<br>

    {
		"age": int,
		"sex": ['M', 'F'],
		"chestPain": ['TA', 'ATA', 'NAP', 'ASY'],
		"restingBP": int,
		"cholesterol": int,
		"fastingBS": int,
		"restingECG": ['Normal', 'ST', 'LVH'],
		"maxHR": int,
		"exerciseAngina": ['N', 'Y'],
		"oldPeak": float,
		"stSlope": ['Up','Flat', 'Down'] ,
	}

Retorna:

 	0 = Negativo
  	1 = Positivo
