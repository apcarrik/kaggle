def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 46, "metric_value": 0.9781, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Coupon", "instances": 22, "metric_value": 0.8454, "depth": 3}
			if obj[0]>0:
				return 'True'
			elif obj[0]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=1:
		# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[0]>2:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		elif obj[0]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
