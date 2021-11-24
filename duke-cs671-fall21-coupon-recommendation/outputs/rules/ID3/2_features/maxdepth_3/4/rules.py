def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 8148, "metric_value": 0.4751, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 5867, "metric_value": 0.4695, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 2281, "metric_value": 0.4856, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
