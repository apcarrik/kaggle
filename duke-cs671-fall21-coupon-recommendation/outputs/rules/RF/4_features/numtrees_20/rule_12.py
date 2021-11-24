def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>5:
		# {"feature": "Distance", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coupon", "instances": 26, "metric_value": 0.9957, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[1]>1:
					return 'False'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>2:
					return 'False'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=5:
		# {"feature": "Coupon", "instances": 21, "metric_value": 0.8631, "depth": 2}
		if obj[0]<=3:
			return 'True'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
