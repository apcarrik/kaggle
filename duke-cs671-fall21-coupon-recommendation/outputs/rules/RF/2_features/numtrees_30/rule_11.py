def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.9481, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
