def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]>2:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[1]<=1:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		elif obj[1]>1:
			return 'True'
		else: return 'True'
	elif obj[0]<=2:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=1:
				return 'False'
			elif obj[3]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
