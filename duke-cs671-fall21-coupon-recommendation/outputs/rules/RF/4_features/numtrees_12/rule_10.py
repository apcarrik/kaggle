def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 56, "metric_value": 0.9241, "depth": 2}
		if obj[2]<=20:
			# {"feature": "Distance", "instances": 53, "metric_value": 0.9414, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 40, "metric_value": 0.8813, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[1]>1:
					return 'True'
				elif obj[1]<=1:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[2]>20:
			return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Education", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Distance", "instances": 19, "metric_value": 0.9819, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]>3:
				return 'True'
			else: return 'True'
		elif obj[2]>10:
			# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
