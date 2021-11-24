def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Education", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>12:
		return 'True'
	else: return 'True'
