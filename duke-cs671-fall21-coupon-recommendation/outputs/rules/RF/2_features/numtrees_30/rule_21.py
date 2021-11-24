def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 22, "metric_value": 0.976, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=4:
			return 'False'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
