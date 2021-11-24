def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.7554, "depth": 1}
	if obj[2]>1:
		# {"feature": "Distance", "instances": 22, "metric_value": 0.684, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 21, "metric_value": 0.5917, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.7219, "depth": 4}
				if obj[0]<=3:
					return 'True'
				elif obj[0]>3:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[2]<=1:
		return 'False'
	else: return 'False'
