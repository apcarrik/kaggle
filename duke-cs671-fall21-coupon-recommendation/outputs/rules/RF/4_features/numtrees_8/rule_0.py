def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 127, "metric_value": 0.9899, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Coupon", "instances": 119, "metric_value": 0.9975, "depth": 2}
		if obj[0]>1:
			# {"feature": "Distance", "instances": 88, "metric_value": 0.976, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 79, "metric_value": 0.9579, "depth": 4}
				if obj[2]<=8.354430379746836:
					return 'True'
				elif obj[2]>8.354430379746836:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[2]<=6:
					return 'False'
				elif obj[2]>6:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=1:
			# {"feature": "Distance", "instances": 31, "metric_value": 0.9383, "depth": 3}
			if obj[3]>1:
				# {"feature": "Occupation", "instances": 19, "metric_value": 0.7425, "depth": 4}
				if obj[2]>1:
					return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[2]>5:
					return 'True'
				elif obj[2]<=5:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[1]>3:
		return 'True'
	else: return 'True'
