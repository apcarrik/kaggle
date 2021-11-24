def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=1:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 12, "metric_value": 0.65, "depth": 3}
			if obj[2]<=6:
				return 'True'
			elif obj[2]>6:
				# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=0:
			return 'False'
		else: return 'False'
	elif obj[1]>1:
		# {"feature": "Occupation", "instances": 9, "metric_value": 0.7642, "depth": 2}
		if obj[2]>2:
			return 'False'
		elif obj[2]<=2:
			return 'True'
		else: return 'True'
	else: return 'False'
