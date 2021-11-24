def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=14:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>14:
		return 'False'
	else: return 'False'
