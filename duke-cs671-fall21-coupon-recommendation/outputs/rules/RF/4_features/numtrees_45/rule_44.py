def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[2]<=12:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>12:
				return 'True'
			else: return 'True'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[2]>2:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]>2:
		return 'False'
	else: return 'False'
