def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 78, "metric_value": 0.9981, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
