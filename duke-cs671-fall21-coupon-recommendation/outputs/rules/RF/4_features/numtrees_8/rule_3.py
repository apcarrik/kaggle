def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9946, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 102, "metric_value": 0.9721, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Distance", "instances": 97, "metric_value": 0.9827, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 88, "metric_value": 0.9624, "depth": 4}
				if obj[2]>1.7055695319855237:
					return 'True'
				elif obj[2]<=1.7055695319855237:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[2]<=21:
					return 'False'
				elif obj[2]>21:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 25, "metric_value": 0.9044, "depth": 2}
		if obj[1]>0:
			# {"feature": "Distance", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[3]>1:
				return 'False'
			elif obj[3]<=1:
				# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[2]>8:
					return 'False'
				elif obj[2]<=8:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
