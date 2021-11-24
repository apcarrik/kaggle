def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]>1:
		# {"feature": "Education", "instances": 17, "metric_value": 0.7871, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 3}
			if obj[2]<=5:
				# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[2]>5:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]<=1:
					return 'True'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3]>1:
				return 'False'
			elif obj[3]<=1:
				# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1]<=0:
					return 'False'
				elif obj[1]>0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>12:
			return 'True'
		else: return 'True'
	else: return 'False'
