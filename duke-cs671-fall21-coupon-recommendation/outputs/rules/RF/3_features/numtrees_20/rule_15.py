def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]<=11:
		# {"feature": "Coupon", "instances": 39, "metric_value": 0.9612, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>11:
		# {"feature": "Coupon", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
