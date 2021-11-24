def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 2}
		if obj[0]>1:
			return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
