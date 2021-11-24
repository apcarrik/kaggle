def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 204, "metric_value": 0.9774, "depth": 1}
	if obj[2]<=7.529411764705882:
		# {"feature": "Coupon", "instances": 127, "metric_value": 0.9309, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 107, "metric_value": 0.856, "depth": 3}
			if obj[1]<=4:
				return 'True'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 20, "metric_value": 0.8813, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]>7.529411764705882:
		# {"feature": "Coupon", "instances": 77, "metric_value": 0.9989, "depth": 2}
		if obj[0]<=3:
			# {"feature": "Education", "instances": 50, "metric_value": 0.9954, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]>3:
			# {"feature": "Education", "instances": 27, "metric_value": 0.951, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
