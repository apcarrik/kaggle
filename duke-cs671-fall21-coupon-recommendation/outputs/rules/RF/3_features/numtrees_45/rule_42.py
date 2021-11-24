def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 16, "metric_value": 1.0, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
