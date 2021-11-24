def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>2:
		# {"feature": "Education", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[1]>2:
			return 'True'
		else: return 'True'
	elif obj[2]<=2:
		return 'False'
	else: return 'False'
