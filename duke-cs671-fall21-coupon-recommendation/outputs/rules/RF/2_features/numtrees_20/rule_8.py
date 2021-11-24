def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 41, "metric_value": 0.9262, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
