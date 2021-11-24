def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9799, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 149, "metric_value": 0.9447, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 55, "metric_value": 0.9883, "depth": 2}
		if obj[1]<=4:
			return 'False'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
