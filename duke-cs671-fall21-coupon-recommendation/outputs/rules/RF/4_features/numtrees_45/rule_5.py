def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.4262, "depth": 1}
	if obj[3]<=1:
		return 'True'
	elif obj[3]>1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[2]<=5:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[2]>5:
			return 'True'
		else: return 'True'
	else: return 'True'
