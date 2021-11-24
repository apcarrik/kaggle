def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=0:
		# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 2}
		if obj[0]<=3:
			return 'False'
		elif obj[0]>3:
			return 'True'
		else: return 'True'
	elif obj[1]>0:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[0]>3:
			return 'False'
		elif obj[0]<=3:
			return 'False'
		else: return 'False'
	else: return 'False'
