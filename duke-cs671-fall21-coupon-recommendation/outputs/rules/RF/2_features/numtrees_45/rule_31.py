def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
