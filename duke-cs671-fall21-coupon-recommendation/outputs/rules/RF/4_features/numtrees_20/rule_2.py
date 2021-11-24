def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[2]<=7:
		# {"feature": "Distance", "instances": 31, "metric_value": 0.8238, "depth": 2}
		if obj[3]>1:
			# {"feature": "Coupon", "instances": 17, "metric_value": 0.6723, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>3:
				# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[3]<=1:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]>7:
		# {"feature": "Education", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[0]>2:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
