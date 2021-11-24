def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9883, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 148, "metric_value": 0.9519, "depth": 2}
		if obj[2]<=7.547297297297297:
			# {"feature": "Education", "instances": 93, "metric_value": 0.8691, "depth": 3}
			if obj[1]<=3:
				return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>7.547297297297297:
			# {"feature": "Education", "instances": 55, "metric_value": 0.9998, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 56, "metric_value": 0.9666, "depth": 2}
		if obj[1]<=4:
			# {"feature": "Occupation", "instances": 54, "metric_value": 0.951, "depth": 3}
			if obj[2]<=7:
				return 'False'
			elif obj[2]>7:
				return 'True'
			else: return 'True'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
