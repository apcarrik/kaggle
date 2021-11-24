def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[2]<=7.141176470588236:
		# {"feature": "Coupon", "instances": 58, "metric_value": 0.9784, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 44, "metric_value": 0.9024, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 31, "metric_value": 0.9629, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>7.141176470588236:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.9183, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
