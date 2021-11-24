def findDecision(obj): #obj[0]: Coupon, obj[1]: Education
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[1]<=3:
			return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'True'
	else: return 'True'
