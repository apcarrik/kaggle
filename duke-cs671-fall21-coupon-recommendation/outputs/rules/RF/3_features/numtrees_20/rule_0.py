def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 40, "metric_value": 0.9544, "depth": 2}
		if obj[2]<=14:
			# {"feature": "Education", "instances": 34, "metric_value": 0.9774, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>14:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[2]<=4:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[2]>4:
			return 'False'
		else: return 'False'
	else: return 'False'
