def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 55, "metric_value": 0.9979, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.65, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
