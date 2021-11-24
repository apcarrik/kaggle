def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 69, "metric_value": 0.9446, "depth": 2}
		if obj[1]<=4:
			return 'True'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
