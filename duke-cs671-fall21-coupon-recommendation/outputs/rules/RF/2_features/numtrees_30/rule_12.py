def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 22, "metric_value": 0.976, "depth": 2}
		if obj[0]<=2:
			return 'True'
		elif obj[0]>2:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
