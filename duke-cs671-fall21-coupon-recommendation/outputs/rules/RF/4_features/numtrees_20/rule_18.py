def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9183, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 40, "metric_value": 0.8113, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 35, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 30, "metric_value": 0.7838, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[1]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[2]>1:
			# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[3]>1:
				return 'False'
			elif obj[3]<=1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>2:
					return 'False'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
