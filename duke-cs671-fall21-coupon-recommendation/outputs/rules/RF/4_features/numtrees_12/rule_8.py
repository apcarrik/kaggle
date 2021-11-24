def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 68, "metric_value": 0.9975, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 65, "metric_value": 0.9998, "depth": 3}
			if obj[2]>0:
				# {"feature": "Distance", "instances": 64, "metric_value": 0.9993, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.6723, "depth": 2}
		if obj[2]<=11:
			# {"feature": "Distance", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[1]>1:
					return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>11:
			return 'False'
		else: return 'False'
	else: return 'False'
