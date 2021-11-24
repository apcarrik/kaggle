def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 46, "metric_value": 0.9877, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
