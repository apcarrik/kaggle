def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 79, "metric_value": 0.9971, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]<=2:
			return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'True'
