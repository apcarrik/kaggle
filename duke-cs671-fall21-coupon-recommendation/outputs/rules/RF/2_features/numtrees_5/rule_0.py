def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9916, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 148, "metric_value": 0.9569, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 56, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
