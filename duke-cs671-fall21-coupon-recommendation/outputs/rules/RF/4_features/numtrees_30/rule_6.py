def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 24, "metric_value": 0.9544, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[2]<=17:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>17:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[2]<=9:
				return 'True'
			elif obj[2]>9:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 2}
		if obj[2]>4:
			# {"feature": "Distance", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[3]>1:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0]>3:
					return 'False'
				elif obj[0]<=3:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]<=4:
			return 'False'
		else: return 'False'
	else: return 'False'
