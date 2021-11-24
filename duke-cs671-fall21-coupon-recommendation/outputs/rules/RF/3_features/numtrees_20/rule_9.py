def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 43, "metric_value": 0.9103, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 34, "metric_value": 0.8338, "depth": 3}
			if obj[2]<=11:
				return 'True'
			elif obj[2]>11:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[2]>2:
				return 'False'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
