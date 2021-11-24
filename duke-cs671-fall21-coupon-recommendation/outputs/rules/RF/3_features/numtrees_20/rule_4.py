def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[1]<=4:
		# {"feature": "Occupation", "instances": 49, "metric_value": 0.9973, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Coupon", "instances": 39, "metric_value": 0.9995, "depth": 3}
			if obj[0]>1:
				return 'False'
			elif obj[0]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>12:
			# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]>4:
		return 'True'
	else: return 'True'
