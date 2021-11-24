def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Education", "instances": 24, "metric_value": 0.9799, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[2]<=13:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[2]>13:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 3}
			if obj[2]>1:
				return 'True'
			elif obj[2]<=1:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=2:
					return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[3]>2:
		# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]>6:
					return 'False'
				elif obj[2]<=6:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
