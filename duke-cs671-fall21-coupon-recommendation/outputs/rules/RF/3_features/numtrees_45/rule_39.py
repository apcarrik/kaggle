def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[2]<=13:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>13:
			# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
