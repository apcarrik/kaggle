def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
