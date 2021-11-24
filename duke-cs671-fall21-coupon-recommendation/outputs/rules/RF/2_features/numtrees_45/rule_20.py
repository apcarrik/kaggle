def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
