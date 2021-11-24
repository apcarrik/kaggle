def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 60, "metric_value": 0.9871, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 25, "metric_value": 0.9044, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
