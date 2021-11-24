def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9576, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.9403, "depth": 3}
			if obj[0]>2:
				# {"feature": "Education", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]<=2:
				# {"feature": "Education", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[1]<=1:
					return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[3]>2:
		return 'False'
	else: return 'False'
