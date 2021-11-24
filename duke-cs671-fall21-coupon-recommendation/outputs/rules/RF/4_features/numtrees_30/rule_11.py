def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[3]>1:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.8113, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>7:
			return 'False'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[0]>0:
			return 'True'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	else: return 'True'
