def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Occupation", "instances": 15, "metric_value": 0.3534, "depth": 3}
			if obj[2]<=6:
				return 'True'
			elif obj[2]>6:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>3:
			# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]<=4:
				return 'False'
			elif obj[2]>4:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[3]>1:
			return 'False'
		elif obj[3]<=1:
			# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=12:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
