def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.6723, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.258, "depth": 2}
		if obj[2]>1:
			return 'True'
		elif obj[2]<=1:
			# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>10:
			return 'True'
		else: return 'True'
	else: return 'True'
