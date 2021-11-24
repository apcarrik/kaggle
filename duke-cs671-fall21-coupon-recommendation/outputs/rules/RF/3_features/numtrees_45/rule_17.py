def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 17, "metric_value": 0.9774, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=6:
				return 'True'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		return 'False'
	else: return 'False'
