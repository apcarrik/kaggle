def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[2]<=14:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.8813, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 25, "metric_value": 0.795, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>14:
		return 'False'
	else: return 'False'
