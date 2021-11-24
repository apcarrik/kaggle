def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 127, "metric_value": 0.987, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 91, "metric_value": 0.9355, "depth": 2}
		if obj[0]>1:
			return 'True'
		elif obj[0]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 36, "metric_value": 0.9436, "depth": 2}
		if obj[0]<=3:
			return 'False'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
