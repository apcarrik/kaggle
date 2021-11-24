def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]<=12:
		# {"feature": "Coupon", "instances": 43, "metric_value": 0.9103, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 40, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=1:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]>1:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.7219, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>12:
		# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 2}
		if obj[3]>1:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[3]<=1:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
