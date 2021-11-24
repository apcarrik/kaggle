def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 65, "metric_value": 0.9077, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 49, "metric_value": 0.8346, "depth": 3}
			if obj[2]<=14:
				return 'True'
			elif obj[2]>14:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 16, "metric_value": 1.0, "depth": 3}
			if obj[2]>4:
				return 'False'
			elif obj[2]<=4:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[2]<=16:
				return 'False'
			elif obj[2]>16:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
