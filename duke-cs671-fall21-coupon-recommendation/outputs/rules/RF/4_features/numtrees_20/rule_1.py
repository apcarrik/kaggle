def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[1]>1:
		# {"feature": "Occupation", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.9911, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Distance", "instances": 10, "metric_value": 1.0, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Distance", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[2]>10:
			# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0]>1:
				# {"feature": "Distance", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3]<=1:
					return 'False'
				elif obj[3]>1:
					return 'False'
				else: return 'False'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=1:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.8555, "depth": 2}
		if obj[2]>4:
			# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 3}
			if obj[0]>1:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=1:
				# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>1:
					return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=4:
			# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 3}
			if obj[0]<=3:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
