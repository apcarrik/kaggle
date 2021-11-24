def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[0]>2:
			return 'True'
		elif obj[0]<=2:
			return 'False'
		else: return 'False'
	else: return 'True'
