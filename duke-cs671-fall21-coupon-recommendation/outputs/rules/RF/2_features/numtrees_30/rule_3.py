def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.874, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 20, "metric_value": 0.6098, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 14, "metric_value": 1.0, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
