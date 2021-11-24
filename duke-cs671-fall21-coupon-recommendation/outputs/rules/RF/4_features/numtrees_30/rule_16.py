def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 22, "metric_value": 0.994, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 21, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[2]<=5:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>5:
			return 'False'
		else: return 'False'
	else: return 'False'
