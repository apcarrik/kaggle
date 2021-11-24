def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 70, "metric_value": 0.9518, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 15, "metric_value": 0.7219, "depth": 2}
		if obj[1]<=3:
			return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
