def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.9751, "depth": 2}
		if obj[0]>1:
			# {"feature": "Distance", "instances": 24, "metric_value": 0.9183, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 22, "metric_value": 0.8454, "depth": 4}
				if obj[2]<=14:
					return 'True'
				elif obj[2]>14:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		return 'True'
	else: return 'True'
