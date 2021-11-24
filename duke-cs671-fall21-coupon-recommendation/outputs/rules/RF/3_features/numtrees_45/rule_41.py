def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[2]>3:
				return 'True'
			elif obj[2]<=3:
				return 'False'
			else: return 'False'
		elif obj[0]>3:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0]<=2:
			return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]>6:
				return 'True'
			elif obj[2]<=6:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
