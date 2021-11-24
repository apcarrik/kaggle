def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[1]<=3:
		# {"feature": "Occupation", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[2]<=8:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[0]>1:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		elif obj[2]>8:
			return 'True'
		else: return 'True'
	elif obj[1]>3:
		return 'False'
	else: return 'False'
