def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.995, "depth": 2}
		if obj[2]>5:
			# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 3}
			if obj[1]<=4:
				return 'False'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		elif obj[2]<=5:
			# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[2]<=5:
				return 'False'
			elif obj[2]>5:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
