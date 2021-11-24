def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[0]>2:
			return 'True'
		elif obj[0]<=2:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
