def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.971, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 56, "metric_value": 0.9059, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 53, "metric_value": 0.9245, "depth": 3}
			if obj[2]>2.1430499949798465:
				# {"feature": "Distance", "instances": 44, "metric_value": 0.8757, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=2.1430499949798465:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[2]>4:
			# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=4:
			# {"feature": "Education", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
