def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 2}
		if obj[2]>1:
			# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 3}
			if obj[1]>0:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0]>2:
					return 'True'
				elif obj[0]<=2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[3]>2:
		return 'True'
	else: return 'True'
