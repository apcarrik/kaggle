def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 35, "metric_value": 0.8631, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
