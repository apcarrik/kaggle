def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 21, "metric_value": 0.7919, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
