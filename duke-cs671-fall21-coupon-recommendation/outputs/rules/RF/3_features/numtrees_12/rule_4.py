def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[2]>0:
		# {"feature": "Education", "instances": 82, "metric_value": 0.9983, "depth": 2}
		if obj[1]<=4:
			# {"feature": "Coupon", "instances": 80, "metric_value": 0.9959, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	elif obj[2]<=0:
		return 'True'
	else: return 'True'
