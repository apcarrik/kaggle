def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 167, "metric_value": 0.9838, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 37, "metric_value": 0.909, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
