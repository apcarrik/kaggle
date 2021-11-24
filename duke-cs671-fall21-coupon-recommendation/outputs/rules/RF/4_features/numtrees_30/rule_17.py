def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 2}
		if obj[2]<=17:
			# {"feature": "Education", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.6723, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>17:
			return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.8454, "depth": 2}
		if obj[2]<=14:
			return 'False'
		elif obj[2]>14:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
