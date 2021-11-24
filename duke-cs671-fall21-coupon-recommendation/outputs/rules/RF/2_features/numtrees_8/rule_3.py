def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9838, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 92, "metric_value": 0.9503, "depth": 2}
		if obj[1]>1:
			return 'True'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 35, "metric_value": 0.9852, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
