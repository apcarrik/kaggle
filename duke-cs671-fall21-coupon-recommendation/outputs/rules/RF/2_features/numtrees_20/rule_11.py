def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9971, "depth": 2}
		if obj[1]<=1:
			return 'True'
		elif obj[1]>1:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
