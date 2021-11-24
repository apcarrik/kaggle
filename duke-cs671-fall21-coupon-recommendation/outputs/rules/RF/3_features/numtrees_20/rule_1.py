def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 28, "metric_value": 0.8113, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.684, "depth": 3}
			if obj[2]<=7:
				return 'True'
			elif obj[2]>7:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[2]>4:
				return 'False'
			elif obj[2]<=4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 2}
		if obj[1]<=4:
			# {"feature": "Occupation", "instances": 22, "metric_value": 0.9024, "depth": 3}
			if obj[2]<=14:
				return 'False'
			elif obj[2]>14:
				return 'False'
			else: return 'False'
		elif obj[1]>4:
			return 'True'
		else: return 'True'
	else: return 'False'
