def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[2]<=9:
		# {"feature": "Education", "instances": 31, "metric_value": 0.9629, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 20, "metric_value": 1.0, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[0]<=2:
				return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>9:
		return 'True'
	else: return 'True'
