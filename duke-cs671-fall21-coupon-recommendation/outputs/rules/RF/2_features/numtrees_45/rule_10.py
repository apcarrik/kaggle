def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 8, "metric_value": 1.0, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'True'
