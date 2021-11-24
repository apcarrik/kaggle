def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9978, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 94, "metric_value": 0.9734, "depth": 2}
		if obj[2]<=11:
			# {"feature": "Education", "instances": 75, "metric_value": 0.9183, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 39, "metric_value": 0.9957, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Distance", "instances": 36, "metric_value": 0.7107, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>11:
			# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 33, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.8691, "depth": 3}
			if obj[2]<=13:
				# {"feature": "Distance", "instances": 27, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>13:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	else: return 'False'
