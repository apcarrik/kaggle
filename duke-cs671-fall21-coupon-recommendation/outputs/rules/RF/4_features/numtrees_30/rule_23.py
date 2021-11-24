def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[2]>3:
		# {"feature": "Education", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=3:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[1]<=1:
			return 'False'
		elif obj[1]>1:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
