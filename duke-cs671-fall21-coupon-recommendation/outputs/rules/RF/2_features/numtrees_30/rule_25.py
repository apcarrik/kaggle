def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.9544, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'False'
	else: return 'False'
