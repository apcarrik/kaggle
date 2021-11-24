def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[1]>1:
		# {"feature": "Coupon", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[0]>0:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.9544, "depth": 3}
			if obj[2]<=16:
				# {"feature": "Distance", "instances": 22, "metric_value": 0.9024, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[2]>16:
				return 'True'
			else: return 'True'
		elif obj[0]<=0:
			return 'True'
		else: return 'True'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.7219, "depth": 2}
		if obj[2]>3:
			# {"feature": "Distance", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[3]>1:
				# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 4}
				if obj[0]>2:
					return 'True'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			elif obj[3]<=1:
				# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[0]>2:
					return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=3:
			return 'True'
		else: return 'True'
	else: return 'True'
