def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 60, "metric_value": 0.8813, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 25, "metric_value": 0.9896, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	else: return 'False'
