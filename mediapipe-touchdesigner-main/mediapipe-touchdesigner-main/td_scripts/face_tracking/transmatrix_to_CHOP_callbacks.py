# me - this DAT
# scriptOp - the OP which is cooking

import json
import numpy as np

# press 'Setup Parameters' in the OP to call this function to re-create the parameters.

# called whenever custom pulse parameter is pushed
def onPulse(par):
	return

def onCook(scriptOp):
	scriptOp.clear()
	scriptOp.numSamples = 1
	scriptOp.appendChan('m00')
	scriptOp.appendChan('m10')
	scriptOp.appendChan('m20')
	scriptOp.appendChan('m30')
	scriptOp.appendChan('m01')
	scriptOp.appendChan('m11')
	scriptOp.appendChan('m21')
	scriptOp.appendChan('m31')
	scriptOp.appendChan('m02')
	scriptOp.appendChan('m12')
	scriptOp.appendChan('m22')
	scriptOp.appendChan('m32')
	scriptOp.appendChan('m03')
	scriptOp.appendChan('m13')
	scriptOp.appendChan('m23')
	scriptOp.appendChan('m33')

	if(op('in1').text != "" and parent().parent().par.Transformationmatricies == True):
		rawdata = json.loads(op('in1').text)
			
		# digits = scriptOp.parent().digits -1
		# print("digits: " +str(digits))
		# print(str(len(rawdata['faceResults']['faceLandmarks'])))
		if not len(rawdata):
			return
		# Check to see if we have a face
		if(len(rawdata['faceLandmarkResults']) > 0 and rawdata['faceLandmarkResults']['facialTransformationMatrixes']):
			scriptOp.numSamples = len(rawdata['faceLandmarkResults']['facialTransformationMatrixes'])
			i = 0
			# Iterate through each detected face
			for transmatricies in rawdata['faceLandmarkResults']['facialTransformationMatrixes']:
				# print(transmatricies["data"])
				print("")
				scriptOp['m00'][i] = transmatricies["data"][0]
				scriptOp['m10'][i] = transmatricies["data"][1]
				scriptOp['m20'][i] = transmatricies["data"][2]
				scriptOp['m30'][i] = transmatricies["data"][3]
				scriptOp['m01'][i] = transmatricies["data"][4]
				scriptOp['m11'][i] = transmatricies["data"][5]
				scriptOp['m21'][i] = transmatricies["data"][6]
				scriptOp['m31'][i] = transmatricies["data"][7]
				scriptOp['m02'][i] = transmatricies["data"][8]
				scriptOp['m12'][i] = transmatricies["data"][9]
				scriptOp['m22'][i] = transmatricies["data"][10]
				scriptOp['m32'][i] = transmatricies["data"][11]
				scriptOp['m03'][i] = transmatricies["data"][12]
				scriptOp['m13'][i] = transmatricies["data"][13]
				scriptOp['m23'][i] = transmatricies["data"][14]
				scriptOp['m33'][i] = transmatricies["data"][15]
				i += 1
		return

	# No faces detected, so make a 0 filled CHOP
	# print("no transMatricies")
	scriptOp.copyNumpyArray(np.zeros((16,1),np.float32))
	return

def onSetupParameters(scriptOp):
	"""Auto-generated by Component Editor"""
	# manual changes to anything other than parJSON will be	# destroyed by Comp Editor unless doc string above is	# changed

	TDJSON = op.TDModules.mod.TDJSON
	parJSON = """
	{}
	"""
	parData = TDJSON.textToJSON(parJSON)
	TDJSON.addParametersFromJSONOp(scriptOp, parData, destroyOthers=True)