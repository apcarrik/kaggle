def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9656, "depth": 1}
	if obj[0]>0:
		# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[2]<=6:
					return 'True'
				elif obj[2]>6:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[3]>2:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
