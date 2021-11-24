def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 42, "metric_value": 0.9587, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	else: return 'False'
