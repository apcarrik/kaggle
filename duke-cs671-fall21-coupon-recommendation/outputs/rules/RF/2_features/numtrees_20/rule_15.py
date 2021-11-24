def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Education", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.9745, "depth": 2}
		if obj[0]>0:
			return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Coupon", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
