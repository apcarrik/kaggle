def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9802, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 92, "metric_value": 0.8991, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 35, "metric_value": 0.8981, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
