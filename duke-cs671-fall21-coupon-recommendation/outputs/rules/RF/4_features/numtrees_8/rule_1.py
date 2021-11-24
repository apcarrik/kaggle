def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Distance", "instances": 91, "metric_value": 0.9747, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Occupation", "instances": 76, "metric_value": 0.9495, "depth": 3}
			if obj[2]<=16:
				# {"feature": "Education", "instances": 74, "metric_value": 0.9353, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>16:
				return 'False'
			else: return 'False'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[2]<=12:
					return 'False'
				elif obj[2]>12:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 36, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 28, "metric_value": 0.9666, "depth": 3}
			if obj[2]<=11:
				# {"feature": "Distance", "instances": 25, "metric_value": 0.9896, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[2]>11:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]<=11:
				return 'False'
			elif obj[2]>11:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
