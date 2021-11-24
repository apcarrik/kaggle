def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Education", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[0]>3:
				return 'False'
			elif obj[0]<=3:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[0]>2:
				return 'True'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>12:
		return 'True'
	else: return 'True'
