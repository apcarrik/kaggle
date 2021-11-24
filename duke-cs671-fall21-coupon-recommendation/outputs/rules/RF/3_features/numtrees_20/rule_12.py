def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 42, "metric_value": 0.9934, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 40, "metric_value": 0.9837, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
