def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[2]<=13:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.8524, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		elif obj[2]>13:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[2]<=10:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[2]>10:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[0]>3:
			return 'True'
		else: return 'True'
	else: return 'True'
