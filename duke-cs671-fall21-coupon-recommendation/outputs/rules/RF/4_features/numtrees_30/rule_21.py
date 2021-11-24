def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]>2:
		# {"feature": "Occupation", "instances": 22, "metric_value": 0.9457, "depth": 2}
		if obj[2]<=14:
			# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>14:
			return 'True'
		else: return 'True'
	elif obj[0]<=2:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 2}
		if obj[2]<=9:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]>9:
			return 'False'
		else: return 'False'
	else: return 'False'
