def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9637, "depth": 1}
	if obj[2]<=7.517647058823529:
		# {"feature": "Coupon", "instances": 58, "metric_value": 0.9124, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 50, "metric_value": 0.8555, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>7.517647058823529:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.999, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 26, "metric_value": 0.9957, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
