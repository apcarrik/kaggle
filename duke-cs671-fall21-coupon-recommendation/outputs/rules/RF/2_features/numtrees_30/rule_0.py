def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 29, "metric_value": 0.9576, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
