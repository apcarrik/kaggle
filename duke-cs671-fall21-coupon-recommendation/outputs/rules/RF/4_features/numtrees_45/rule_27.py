def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 1}
	if obj[2]<=7:
		# {"feature": "Education", "instances": 17, "metric_value": 0.9367, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[0]>2:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]>7:
		return 'True'
	else: return 'True'
