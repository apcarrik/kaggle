def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 85, "metric_value": 0.9555, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 55, "metric_value": 0.8921, "depth": 2}
		if obj[0]>2:
			return 'True'
		elif obj[0]<=2:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 30, "metric_value": 1.0, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	else: return 'False'
