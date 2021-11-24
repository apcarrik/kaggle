def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.6962, "depth": 2}
		if obj[2]<=6:
			# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>6:
			return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
