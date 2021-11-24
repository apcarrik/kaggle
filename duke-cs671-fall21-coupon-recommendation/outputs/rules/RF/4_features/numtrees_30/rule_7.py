def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.8997, "depth": 2}
		if obj[2]<=13:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>13:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Education", "instances": 15, "metric_value": 0.8366, "depth": 2}
		if obj[1]>1:
			return 'False'
		elif obj[1]<=1:
			# {"feature": "Occupation", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=7:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>7:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
