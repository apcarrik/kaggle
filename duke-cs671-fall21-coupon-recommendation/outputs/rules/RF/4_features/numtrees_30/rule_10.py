def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 31, "metric_value": 0.9383, "depth": 2}
		if obj[2]<=8:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.8281, "depth": 3}
			if obj[0]>0:
				# {"feature": "Education", "instances": 20, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=0:
					return 'True'
				elif obj[1]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>8:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 3}
			if obj[0]>2:
				# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[0]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[3]>2:
		return 'False'
	else: return 'False'
