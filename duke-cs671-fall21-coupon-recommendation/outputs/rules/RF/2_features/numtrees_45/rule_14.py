def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=1:
			return 'True'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
