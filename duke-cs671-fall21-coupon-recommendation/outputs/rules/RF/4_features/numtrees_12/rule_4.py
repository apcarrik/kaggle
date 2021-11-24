def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[0]>1:
		# {"feature": "Distance", "instances": 66, "metric_value": 0.9024, "depth": 2}
		if obj[3]>1:
			# {"feature": "Occupation", "instances": 42, "metric_value": 0.9737, "depth": 3}
			if obj[2]<=9:
				# {"feature": "Education", "instances": 29, "metric_value": 0.8936, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]>9:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Education", "instances": 24, "metric_value": 0.65, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.5586, "depth": 4}
				if obj[2]<=7:
					return 'True'
				elif obj[2]>7:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Occupation", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[2]>2:
					return 'False'
				elif obj[2]<=2:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
