def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 27, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 24, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
