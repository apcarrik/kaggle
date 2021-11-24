def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9989, "depth": 1}
	if obj[0]<=3:
		# {"feature": "Occupation", "instances": 86, "metric_value": 0.9749, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Education", "instances": 69, "metric_value": 0.9986, "depth": 3}
			if obj[1]>0:
				# {"feature": "Distance", "instances": 45, "metric_value": 0.9825, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[1]<=0:
				# {"feature": "Distance", "instances": 24, "metric_value": 0.8709, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>10:
			# {"feature": "Distance", "instances": 17, "metric_value": 0.5226, "depth": 3}
			if obj[3]>1:
				# {"feature": "Education", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[1]<=2:
					return 'True'
				elif obj[1]>2:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>3:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.9474, "depth": 2}
		if obj[2]>2:
			# {"feature": "Distance", "instances": 38, "metric_value": 0.8997, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Education", "instances": 36, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					return 'False'
				else: return 'False'
			elif obj[3]>2:
				return 'False'
			else: return 'False'
		elif obj[2]<=2:
			return 'True'
		else: return 'True'
	else: return 'False'
