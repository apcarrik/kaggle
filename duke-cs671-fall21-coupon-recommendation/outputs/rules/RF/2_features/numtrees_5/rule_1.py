def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9989, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 151, "metric_value": 0.9732, "depth": 2}
		if obj[1]>0:
			return 'True'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 53, "metric_value": 0.8836, "depth": 2}
		if obj[1]<=4:
			return 'False'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
