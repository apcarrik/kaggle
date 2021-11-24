def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.9427, "depth": 2}
		if obj[2]>0:
			# {"feature": "Distance", "instances": 24, "metric_value": 0.9183, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Education", "instances": 8, "metric_value": 1.0, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=0:
			return 'False'
		else: return 'False'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]>1:
				return 'False'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
