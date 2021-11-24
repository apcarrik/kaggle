def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[1]>1:
			return 'False'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	else: return 'False'
