def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9996, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 87, "metric_value": 0.9838, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Education", "instances": 64, "metric_value": 0.9284, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>10:
			# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 40, "metric_value": 0.8813, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Education", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>6:
			# {"feature": "Education", "instances": 18, "metric_value": 0.65, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
