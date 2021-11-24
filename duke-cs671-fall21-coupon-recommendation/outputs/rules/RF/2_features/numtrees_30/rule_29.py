def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 24, "metric_value": 0.8709, "depth": 2}
		if obj[1]>1:
			return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
