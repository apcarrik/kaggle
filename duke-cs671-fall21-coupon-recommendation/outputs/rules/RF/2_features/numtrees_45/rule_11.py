def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 19, "metric_value": 0.998, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
