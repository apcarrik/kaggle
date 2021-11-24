def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[0]>0:
				return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
