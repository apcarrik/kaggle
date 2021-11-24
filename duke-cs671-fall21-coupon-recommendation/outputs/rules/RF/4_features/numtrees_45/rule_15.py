def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]>4:
		# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 2}
		if obj[1]>1:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]<=1:
			return 'False'
		else: return 'False'
	elif obj[2]<=4:
		return 'True'
	else: return 'True'
