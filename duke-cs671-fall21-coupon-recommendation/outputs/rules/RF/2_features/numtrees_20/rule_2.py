def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 41, "metric_value": 0.8722, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
