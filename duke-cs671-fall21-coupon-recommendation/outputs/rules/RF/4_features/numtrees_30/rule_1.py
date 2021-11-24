def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[2]>1:
		# {"feature": "Coupon", "instances": 30, "metric_value": 0.971, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=0:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'True'
				else: return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
