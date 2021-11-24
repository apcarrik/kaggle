def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9931, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 147, "metric_value": 0.9717, "depth": 2}
		if obj[1]>1:
			return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 57, "metric_value": 0.9819, "depth": 2}
		if obj[1]<=4:
			return 'False'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
