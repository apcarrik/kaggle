def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[2]>12:
		return 'True'
	else: return 'True'
