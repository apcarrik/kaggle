def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Education", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[1]<=2:
				return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>12:
			return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[1]>0:
			return 'False'
		elif obj[1]<=0:
			return 'True'
		else: return 'True'
	else: return 'False'
