def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 101, "metric_value": 0.9116, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 26, "metric_value": 0.7793, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
