def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[2]<=7:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[3]<=2:
				return 'True'
			elif obj[3]>2:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]>1:
					return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>7:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[1]<=2:
			return 'False'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[2]>2:
				return 'False'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
