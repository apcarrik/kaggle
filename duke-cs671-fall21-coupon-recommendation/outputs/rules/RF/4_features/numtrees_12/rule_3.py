def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 85, "metric_value": 0.9831, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Coupon", "instances": 71, "metric_value": 0.9582, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 59, "metric_value": 0.9238, "depth": 3}
			if obj[2]>2:
				# {"feature": "Education", "instances": 41, "metric_value": 0.965, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=2:
				# {"feature": "Education", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[2]<=14:
				# {"feature": "Education", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[1]<=3:
					return 'False'
				elif obj[1]>3:
					return 'True'
				else: return 'True'
			elif obj[2]>14:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>2:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]>1:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=3:
					return 'False'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>7:
			return 'False'
		else: return 'False'
	else: return 'False'
