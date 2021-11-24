def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Education", "instances": 51, "metric_value": 0.9997, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 44, "metric_value": 0.9865, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.9072, "depth": 3}
			if obj[2]<=6:
				return 'True'
			elif obj[2]>6:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
