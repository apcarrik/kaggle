def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.8498, "depth": 2}
		if obj[2]<=4:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=3:
				return 'False'
			elif obj[0]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>4:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[0]<=3:
				return 'False'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>3:
		# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[2]>5:
			return 'True'
		elif obj[2]<=5:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=3:
				return 'False'
			elif obj[0]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
