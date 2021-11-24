def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
