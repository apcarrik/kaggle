def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 20, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Distance", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[2]<=6:
					return 'False'
				elif obj[2]>6:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[2]<=6:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[2]<=16:
			# {"feature": "Education", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>16:
			return 'True'
		else: return 'True'
	else: return 'False'
