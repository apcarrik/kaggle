def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coupon", "instances": 31, "metric_value": 0.9992, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 29, "metric_value": 0.9923, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
