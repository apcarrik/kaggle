def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.5586, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.7793, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>1:
		return 'True'
	else: return 'True'
