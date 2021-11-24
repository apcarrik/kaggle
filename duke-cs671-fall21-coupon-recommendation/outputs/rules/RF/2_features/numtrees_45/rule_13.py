def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=0:
			return 'True'
		elif obj[1]>0:
			return 'False'
		else: return 'False'
	else: return 'False'
