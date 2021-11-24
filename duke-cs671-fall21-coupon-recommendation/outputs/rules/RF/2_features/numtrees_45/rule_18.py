def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0]<=3:
			return 'False'
		elif obj[0]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
