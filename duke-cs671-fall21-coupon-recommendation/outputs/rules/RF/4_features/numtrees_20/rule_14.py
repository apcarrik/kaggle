def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Distance", "instances": 32, "metric_value": 0.9972, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 3}
			if obj[2]<=16:
				# {"feature": "Education", "instances": 19, "metric_value": 0.8997, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[2]>16:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[2]<=19:
				# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[1]<=3:
					return 'True'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[2]>19:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8315, "depth": 2}
		if obj[2]>3:
			# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=3:
			# {"feature": "Education", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
