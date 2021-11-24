def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.8767, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>1:
		# {"feature": "Coupon", "instances": 24, "metric_value": 0.995, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
