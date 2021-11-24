def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 34, "metric_value": 0.7335, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.8404, "depth": 2}
		if obj[0]<=2:
			return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
