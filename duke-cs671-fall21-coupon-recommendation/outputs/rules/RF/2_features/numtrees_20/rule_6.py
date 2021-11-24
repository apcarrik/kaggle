def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 40, "metric_value": 0.971, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
