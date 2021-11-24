def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]<=10:
		# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 2}
		if obj[3]>1:
			# {"feature": "Education", "instances": 10, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[2]>10:
		return 'False'
	else: return 'False'
