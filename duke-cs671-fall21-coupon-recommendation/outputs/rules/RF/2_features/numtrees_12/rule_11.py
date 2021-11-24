def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[1]<=4:
		# {"feature": "Coupon", "instances": 82, "metric_value": 0.9724, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'True'
		else: return 'True'
	elif obj[1]>4:
		return 'True'
	else: return 'True'
