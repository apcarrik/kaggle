def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Education", "instances": 82, "metric_value": 0.9931, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 63, "metric_value": 0.9587, "depth": 3}
			if obj[2]<=7:
				return 'True'
			elif obj[2]>7:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 3}
			if obj[2]<=19:
				return 'False'
			elif obj[2]>19:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 45, "metric_value": 0.9389, "depth": 2}
		if obj[2]<=14:
			# {"feature": "Education", "instances": 39, "metric_value": 0.9766, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>14:
			return 'False'
		else: return 'False'
	else: return 'False'
