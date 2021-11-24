def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[0]<=1:
			return 'False'
		elif obj[0]>1:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
