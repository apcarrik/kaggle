def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[2]<=10:
				return 'True'
			elif obj[2]>10:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=2:
			return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=7:
				return 'False'
			elif obj[2]>7:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
