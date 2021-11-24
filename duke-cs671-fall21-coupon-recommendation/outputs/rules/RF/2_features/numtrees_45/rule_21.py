def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>2:
		# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[0]<=2:
		# {"feature": "Education", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
