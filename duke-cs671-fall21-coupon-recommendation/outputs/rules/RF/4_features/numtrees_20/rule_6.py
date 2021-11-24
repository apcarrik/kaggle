def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 36, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=19:
			# {"feature": "Education", "instances": 33, "metric_value": 0.8454, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 26, "metric_value": 0.7063, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>19:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Education", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>6:
			return 'False'
		else: return 'False'
	else: return 'False'
