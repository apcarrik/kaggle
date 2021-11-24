def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[2]>2:
		# {"feature": "Distance", "instances": 37, "metric_value": 0.9868, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 30, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 11, "metric_value": 0.8454, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=2:
		# {"feature": "Distance", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[3]>1:
			return 'True'
		elif obj[3]<=1:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
