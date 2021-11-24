def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 94, "metric_value": 0.9948, "depth": 2}
		if obj[1]>1:
			return 'False'
		elif obj[1]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 33, "metric_value": 0.9673, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
