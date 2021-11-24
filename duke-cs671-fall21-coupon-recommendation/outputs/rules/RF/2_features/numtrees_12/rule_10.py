def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 66, "metric_value": 0.9024, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
