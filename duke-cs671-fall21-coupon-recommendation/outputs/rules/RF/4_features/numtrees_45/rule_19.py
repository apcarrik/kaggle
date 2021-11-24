def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 3}
			if obj[2]<=18:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					return 'False'
				else: return 'False'
			elif obj[2]>18:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			return 'False'
		else: return 'False'
	elif obj[3]>2:
		return 'False'
	else: return 'False'
