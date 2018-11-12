from os import system, path
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data')
def data():
	year = request.args.get('year')
	states = request.args.get('states')
	whereFrom = request.args.get('from')
	dataFile = year + ('-data.json')

	SITE_ROOT = path.realpath(path.dirname(__file__))
	data_json_url = path.join(SITE_ROOT, 'static', dataFile)
	data = json.load(open(data_json_url))

	if states == 'All':
		if whereFrom == 'All':
			# We'll show each county line eminateing to the the center of the states from the center of the county
			responseData = data
		elif whereFrom == 'None':
			# We'll show one line from SF to the the center of the states
			responseData = {
				"Bay Area" : {
					"from" : {
						"LAT": data['San Francisco']['from']['LAT'],
						"LONG": data['San Francisco']['from']['LONG']
					},
					"to" : {}
				}
			}
			for county, countyValues in data.items():
				for state, stateValue in countyValues['to'].items():
					if responseData['Bay Area']['to'].get(state, None) is None:
						responseData['Bay Area']['to'][state] = {
							'amount': stateValue['amount'],
							'LAT': stateValue['LAT'],
							'LONG': stateValue['LONG']
						}
					else:
						responseData['Bay Area']['to'][state]['amount'] += stateValue['amount']
		else:
			responseData = {
				whereFrom : {
					"from" : {
						"LAT" : data[whereFrom]['from']['LAT'],
						"LONG" : data[whereFrom]['from']['LONG']
					},
					"to" : {}
				}
			}

			responseData[whereFrom]['to'] = data[whereFrom]['to']

	# Return response
	response = app.response_class(
		response=json.dumps(responseData),
		status=200,
		mimetype='application/json'
	)
	return response




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)