def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 47, "metric_value": 0.9918, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 45, "metric_value": 0.9968, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
