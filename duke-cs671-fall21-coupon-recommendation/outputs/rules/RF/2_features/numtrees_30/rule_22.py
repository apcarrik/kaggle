def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>2:
		# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]<=2:
		# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
