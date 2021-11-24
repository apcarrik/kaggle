def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 31, "metric_value": 0.9932, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
