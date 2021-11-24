def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 46, "metric_value": 0.9321, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Distance", "instances": 33, "metric_value": 0.9834, "depth": 3}
			if obj[3]>1:
				# {"feature": "Occupation", "instances": 21, "metric_value": 0.9183, "depth": 4}
				if obj[2]>2:
					return 'False'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[2]<=12:
					return 'False'
				elif obj[2]>12:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[2]<=6:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 39, "metric_value": 0.8905, "depth": 2}
		if obj[0]>1:
			# {"feature": "Occupation", "instances": 31, "metric_value": 0.7706, "depth": 3}
			if obj[2]<=10:
				# {"feature": "Distance", "instances": 24, "metric_value": 0.65, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>10:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[2]<=6:
				# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
