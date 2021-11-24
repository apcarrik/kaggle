def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]>1:
		# {"feature": "Occupation", "instances": 12, "metric_value": 1.0, "depth": 2}
		if obj[2]<=9:
			# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		elif obj[2]>9:
			# {"feature": "Coupon", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0]<=3:
				return 'True'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]<=1:
		# {"feature": "Occupation", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[2]<=7:
			return 'True'
		elif obj[2]>7:
			# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]<=4:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
