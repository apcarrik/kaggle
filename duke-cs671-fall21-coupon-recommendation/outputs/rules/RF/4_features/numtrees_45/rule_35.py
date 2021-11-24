def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9641, "depth": 2}
		if obj[2]>2:
			# {"feature": "Distance", "instances": 16, "metric_value": 0.896, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]>2:
				return 'True'
			else: return 'True'
		elif obj[2]<=2:
			return 'False'
		else: return 'False'
	elif obj[0]>3:
		return 'False'
	else: return 'False'
