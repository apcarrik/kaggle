def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 28, "metric_value": 0.8631, "depth": 2}
		if obj[1]>1:
			return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[1]<=0:
			return 'False'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
