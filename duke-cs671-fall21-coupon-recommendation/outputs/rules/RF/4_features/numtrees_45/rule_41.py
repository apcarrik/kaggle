def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[1]>0:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.9403, "depth": 2}
		if obj[0]>2:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=6:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		elif obj[0]<=2:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.5917, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[2]<=6:
			return 'False'
		elif obj[2]>6:
			# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
