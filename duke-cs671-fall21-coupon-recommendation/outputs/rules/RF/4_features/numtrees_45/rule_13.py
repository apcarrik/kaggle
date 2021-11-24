def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]<=16:
		# {"feature": "Distance", "instances": 21, "metric_value": 0.9984, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 4}
				if obj[0]>1:
					return 'True'
				elif obj[0]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				# {"feature": "Coupon", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=3:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>16:
		return 'True'
	else: return 'True'
