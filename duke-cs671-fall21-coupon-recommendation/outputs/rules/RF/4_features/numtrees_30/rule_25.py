def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.9799, "depth": 3}
			if obj[2]>1:
				# {"feature": "Distance", "instances": 21, "metric_value": 0.9984, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[2]<=1:
				return 'True'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		return 'False'
	else: return 'False'
