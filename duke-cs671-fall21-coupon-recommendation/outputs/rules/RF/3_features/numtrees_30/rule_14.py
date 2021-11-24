def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 27, "metric_value": 0.951, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 17, "metric_value": 0.9975, "depth": 3}
			if obj[2]<=11:
				return 'True'
			elif obj[2]>11:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
