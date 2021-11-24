def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
