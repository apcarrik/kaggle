def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 127, "metric_value": 1.0, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 85, "metric_value": 0.9831, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 42, "metric_value": 0.9183, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
